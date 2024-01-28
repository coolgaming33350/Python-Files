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
					sender_index = self.clients.index(client)
					sender_nickname = self.nicknames[sender_index]
					formatted_message = f"{sender_nickname}: {message}"
					self.broadcast_message_to_clients(formatted_message, client)
			except:
				index = self.clients.index(client)
				self.clients.remove(client)
				client.close()
				nickname = self.nicknames[index]
				self.broadcast_message_to_clients(f'{nickname} has left the chat.', client)
				print(f'{nickname} has left the chat.')
				self.nicknames.remove(nickname)
				self.update_clients_listbox()
				break


	def kick_client(self):
		selected_index = self.clients_listbox.curselection()
		if selected_index:
			selected_index = int(selected_index[0])  # Convert to integer
			if 0 <= selected_index < len(self.clients):  # Check index bounds
				selected_client = self.clients[selected_index]
				selected_client_nickname = self.nicknames[selected_index]

				selected_client.send("You have been kicked by the admin".encode('utf-8'))
				selected_client.close()

				del self.clients[selected_index]
				del self.nicknames[selected_index]

				self.update_clients_listbox()
				self.broadcast_message_to_clients(f"{selected_client_nickname} has been kicked by the admin", None)


	def broadcast_message(self, message):
			formatted_message = f"Server: {message}"
			for client in self.clients:
				client.send(formatted_message.encode('utf-8'))

	def broadcast_message_to_clients(self, message, sender):
		for client in self.clients:
			if client != sender:
				client.send(message.encode('utf-8'))

	def update_clients_listbox(self):
		self.clients_listbox.delete(0, tk.END)
		for nickname, client in zip(self.nicknames, self.clients):
			address = client.getpeername()[0]
			self.clients_listbox.insert(tk.END, f"{nickname} ({address})")

if __name__ == "__main__":
	server_gui = ServerGUI()
