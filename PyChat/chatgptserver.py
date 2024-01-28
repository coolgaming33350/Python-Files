import socket
import threading
import tkinter as tk

class ServerGUI:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '0.0.0.0'
        self.port = 5555
        self.clients = []
        self.nicknames = []

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
            print(f"Connection from {address}")

            nickname = client.recv(1024).decode('utf-8')
            self.clients.append(client)
            self.nicknames.append(nickname)

            self.clients_listbox.insert(tk.END, f"{nickname} ({address[0]})")

            threading.Thread(target=self.handle_client, args=(client,)).start()

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message.startswith('/kick'):
                    # Implement kick functionality
                    pass
                elif message.startswith('/broadcast'):
                    # Implement broadcast functionality
                    pass
                else:
                    # Handle regular messages
                    pass
            except:
                # Handle client disconnect
                pass

    def kick_client(self):
        selected_index = self.clients_listbox.curselection()
        if selected_index:
            selected_client = self.clients[int(selected_index[0])]
            # Implement kick functionality for selected client

    def broadcast_message(self):
        message = self.broadcast_entry.get()
        if message:
            # Implement broadcast message functionality
            pass

if __name__ == "__main__":
    server_gui = ServerGUI()
