import pygame


class Snake:
    COR = [110, 110, 5]
    SNAKE_X, SNAKE_Y = 100, 100
    MOVIMENTO_X = 10
    MOVIMENTO_Y = 10

    def __init__(self, surface):
        self.parent_screen = surface
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = self.SNAKE_X
        self.y = self.SNAKE_Y

    def move_left(self):
        self.x -= self.MOVIMENTO_X
        self.draw()

    def move_right(self):
        self.x += self.MOVIMENTO_X
        self.draw()

    def move_up(self):
        self.y -= self.MOVIMENTO_Y
        self.draw()

    def move_down(self):
        self.y += self.MOVIMENTO_Y
        self.draw()

    def draw(self):
        self.parent_screen.fill(self.COR)

        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()
