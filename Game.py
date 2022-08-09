import pygame
import time

from Apple import Apple
from Snake import Snake
from pygame.locals import *


class Game:

    RES = [1000, 700]
    COR = [0, 0, 0]

    TAMANHO = 40

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(self.RES)
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def start(self):
        self.snake.move()
        self.apple.draw()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.aumentar_tamanho()
            self.apple.move()

        for i in range(1, self.snake.comprimento):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game over"

        if not (0 <= self.snake.x[0] <= self.RES[0] and 0 <= self.snake.y[0] <= self.RES[1]):
            raise "Game over"

    def is_collision(self, x1, y1, x2, y2):
        if x2 - 2 <= x1 and x1 < x2 + self.TAMANHO:
            if y2 - 2 <= y1 and y1 < y2 + self.TAMANHO:
                return True
        return False

    def show_game_over(self):
        self.surface.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 30)
        line = font.render("GG! :(", True, (255, 255, 255))
        self.surface.blit(line, (10, 15))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)


    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_SPACE:
                        pause = False

                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.start()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(0.1)
