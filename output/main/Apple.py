import pygame.image
import random

class Apple:

    COR = [0, 0, 0]
    TAMANHO = 40

    def __init__(self, surface):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = surface
        self.x = self.TAMANHO * 3
        self.y = self.TAMANHO * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 20) * self.TAMANHO
        self.y = random.randint(0, 16) * self.TAMANHO