import pygame
from pygame.locals import *


def draw_block():
    surface.fill((110, 100, 5))
    surface.blit(block, (block_x, block_y))
    pygame.display.update()


if __name__ == "__main__":
    # init pygame
    pygame.init()
    # configurar tamanho
    surface = pygame.display.set_mode((1000, 600))
    # cor
    surface.fill((110, 100, 5))

    block = pygame.image.load("resources/block.jpg").convert()
    block_x, block_y = 100, 100

    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == pygame.K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == pygame.K_RIGHT:
                    block_x += 10
                    draw_block()
                if event.key == pygame.K_LEFT:
                    block_x -= 10
                    draw_block()
            elif event.type == pygame.QUIT:
                run = False
