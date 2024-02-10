import socket
import pygame

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

who_running = 'Carter'
if who_running == 'Carter':
    host = '192.168.0.104'
elif who_running == 'Samuel':
    host = '174.27.172.190'
elif who_running == 'SamuelAtHome':
    host = '192.168.1.251'
else:
    host = '0.0.0.0'

port = 44444
client_socket.connect((host, port))
client_socket.send('ready'.encode())

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong Online')

font = pygame.font.Font(None, 36)

while True:
    pos = client_socket.recv(1024).recv(1024).decode()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    test_rect = pygame.rect.Rect(pos, pos, pos, pos)
    pygame.draw.rect(screen, (255, 0, 0), test_rect)

    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.display.flip()

    # You can send player information here, for example:
    # player_info = {'name': 'Player1', 'score': 100}
    # client_socket.send(str(player_info).encode())
