import pygame
import sys

class Player:
    def __init(self, pos, size):
        self.pos = pos
        self.size = size

class Object:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

    def update(self, dt, speed):
        self.pos[1] += speed * dt
        self.rect = pygame.rect.Rect(tuple(self.pos), tuple(self.size))

    def render(self, surf):
        pygame.draw.rect(surf, (255, 255, 255), self.rect)

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Pygame Game :D')
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()

        self.object_list = []
        self.object_list.append(Object([50, 50], [10, 10]))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))

            dt = self.clock.tick(60) / 1000

            for obj in self.object_list:
                obj.update(dt, 50)
                obj.render(self.screen)

            pygame.display.update()

Game().run()