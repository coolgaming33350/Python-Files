import socket
import threading
import random

nickname = str(random.randint(0,10000000))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.0.104', 5555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('An error occurred')
            client.close()
            break

def write():
    while True:
        message = str(f'random.randint(0,10000000000000000000000000000000000)e')
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
