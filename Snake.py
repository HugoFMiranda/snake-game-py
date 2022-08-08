import pygame


class Snake:

    COR = [0, 0, 0]
    TAMANHO = 40

    def __init__(self, surface, comprimento):
        self.parent_screen = surface
        self.comprimento = comprimento
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [self.TAMANHO] * comprimento
        self.y = [self.TAMANHO] * comprimento
        self.direction = ''

    def aumentar_tamanho(self):
        self.comprimento += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = 'esquerda'

    def move_right(self):
        self.direction = 'direita'

    def move_up(self):
        self.direction = 'cima'

    def move_down(self):
        self.direction = 'baixo'

    def draw(self):
        self.parent_screen.fill(self.COR)
        for i in range(self.comprimento):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move(self):

        for i in range(self.comprimento - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'cima':
            self.y[0] -= self.TAMANHO
            self.draw()
        elif self.direction == 'baixo':
            self.y[0] += self.TAMANHO
            self.draw()
        elif self.direction == 'esquerda':
            self.x[0] -= self.TAMANHO
            self.draw()
        elif self.direction == 'direita':
            self.x[0] += self.TAMANHO
            self.draw()
