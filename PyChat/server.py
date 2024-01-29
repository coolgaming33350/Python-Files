import socket
import threading
import tkinter as tk
import time

class ServerGUI:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '192.168.0.104'
        self.port = 5555
        self.clients = []
        self.nicknames = []
        self.message_timestamps = {}  # Store message timestamps for rate limiting
        self.rate_limit_interval = 0.25  # Rate limit interval in seconds

        self.root = tk.Tk()
        self.root.title("Chat Server")

        self.clients_label = tk.Label(self.root, text="Connected Clients:")
        self.clients_label.pack()

        self.clients_listbox = tk.Listbox(self.root, width=50)
        self.clients_listbox.pack()

        self.kick_button = tk.Button(self.root, text="Kick", command=self.kick_client)
        self.kick_button.pack()

        self.broadcast_label = tk.Label(self.root, text="Broadcast Message:")
        self.broadcast_label.pack()

        self.broadcast_entry = tk.Entry(self.root, width=50)
        self.broadcast_entry.pack()

        self.broadcast_button = tk.Button(self.root, text="Broadcast", command=self.broadcast_message)
        self.broadcast_button.pack()

        self.start_server()

    def start_server(self):
        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f"Server is listening on {self.host}:{self.port}")

        threading.Thread(target=self.accept_clients).start()

        self.root.mainloop()

    def accept_clients(self):
        while True:
            client, address = self.server.accept()

            # Ignore connections from specific IP addresses LEAVE THESE HERE DONT MESS WITH THEM
            if address[0] in ["172.17.0.2", "192.168.0.48"]:
                client.send("Hello from the server!".encode('utf-8'))
                client.close()
                continue

            # Receive the nickname from the client
            try:
                nickname = client.recv(1024).decode('utf-8')
            except Exception as e:
                print(f"Error receiving nickname from {address}: {str(e)}. Closing Connection!")
                client.close()
                continue

            # If the nickname is empty, close the connection and continue
            if not nickname:
                print(f"Connection from {address} without a nickname. Connection ignored.")
                client.close()
                continue

            print(f"Connection from {address}")
            # Add the client and nickname to the lists
            self.clients.append(client)
            self.nicknames.append(nickname)

            # Update the clients listbox
            self.clients_listbox.insert(tk.END, f"{nickname} ({address[0]})")

            # Send welcome message and notify other clients
            welcome_message = "Connected to the server."
            client.send(welcome_message.encode('utf-8'))

            join_message = f"{nickname} joined the server."
            self.broadcast_message_to_clients(join_message, client)

            # Start handling client messages in a separate thread
            threading.Thread(target=self.handle_client, args=(client,)).start()

            # Send the list of other clients to the newly connected client
            self.send_clients_list_to_client(client)

    def send_clients_list_to_client(self, target_client):
        client_list = ",".join([f"{nickname}" for nickname, client in zip(self.nicknames, self.clients)])
        target_client.send(f"/other_clients:{client_list}".encode('utf-8'))

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message.startswith('/kick'):
                    pass
                elif message.startswith('/broadcast'):
                    pass
                elif message.startswith('/get_other_clients'):
                    self.send_clients_list_to_client(client)
                else:
                    if self.check_rate_limit(client):
                        sender_index = self.clients.index(client)
                        sender_nickname = self.nicknames[sender_index]
                        formatted_message = f"{sender_nickname}: {message}"
                        self.broadcast_message_to_clients(formatted_message, client)
                    else:
                        client.send("Rate limit exceeded. Please wait before sending another message.".encode('utf-8'))
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                leave_message = f'{nickname} has left the chat.'
                self.broadcast_message_to_clients(leave_message, client)
                print(leave_message)
                self.nicknames.remove(nickname)
                self.update_clients_listbox()
                break

    def kick_client(self):
        selected_index = self.clients_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            if 0 <= selected_index < len(self.clients):
                selected_client = self.clients[selected_index]
                selected_client_nickname = self.nicknames[selected_index]

                selected_client.send("You have been kicked by the server owner. Reconnection has been disabled.".encode('utf-8'))
                selected_client.close()

                del self.clients[selected_index]
                del self.nicknames[selected_index]

                self.update_clients_listbox()
                kick_message = f"{selected_client_nickname} has been kicked by the admin"
                self.broadcast_message_to_clients(kick_message, None)

    def broadcast_message(self):
        message = self.broadcast_entry.get().strip()
        if message:
            formatted_message = f"Server: {message}"
            for client in self.clients:
                client.send(formatted_message.encode('utf-8'))
            self.broadcast_entry.delete(0, tk.END)

    def broadcast_message_to_clients(self, message, sender):
        for client in self.clients:
            if client != sender:
                client.send(message.encode('utf-8'))

    def update_clients_listbox(self):
        self.clients_listbox.delete(0, tk.END)
        for nickname, client in zip(self.nicknames, self.clients):
            address = client.getpeername()[0]
            if address != "172.17.0.2":
                self.clients_listbox.insert(tk.END, f"{nickname}")

    def check_rate_limit(self, client):
        current_time = time.time()
        if client in self.message_timestamps:
            last_message_time = self.message_timestamps[client]
            if current_time - last_message_time < self.rate_limit_interval:
                return False
        self.message_timestamps[client] = current_time
        return True

if __name__ == "__main__":
    server_gui = ServerGUI()
