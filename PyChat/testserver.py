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

        self.start_server()
    def start_server(self):
        self.server.bind(("192.168.0.104", 5555))
        self.server.listen()
        print(f"Server is listening on {self.host}:{self.port}")

        threading.Thread(target=self.accept_clients).start()



    def accept_clients(self):
        while True:
            client, address = self.server.accept()

            print(f"Connection from {address}")

            return True


if __name__ == "__main__":
    server_gui = ServerGUI()
