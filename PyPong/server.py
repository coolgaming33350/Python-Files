import socket
import threading

clients = []
ready_players = 0
pos = 0


def handle_client(client_socket):
    global ready_players

    try:
        data = client_socket.recv(1024).decode()
        clients.append(client_socket)
        print(f"Received: {data} from {addr}")

        if data == 'ready':
            ready_players += 1

            print(ready_players)
            if ready_players == 2:
                print("All players are ready. Game can start now.")

            while True:
                client_socket.send(f'{pos}')


    except Exception as e:
        print(f"Error: {e}")
    finally:
        clients.remove(client_socket)
        client_socket.close()
        print(f"Connection with {addr} closed")


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.104'
port = 44444
server_socket.bind((host, port))
server_socket.listen(2)

print(f'Server is listening on {host}:{port}')

while True:
    client_socket, addr = server_socket.accept()
    print(f"Got connection from {addr}")

    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
