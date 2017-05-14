import sys

import pygame

pygame.init()
colums, rows = 50, 50
cell_size = 10
size = width, height = colums * cell_size, rows * cell_size
screen ? pygame.display.set_mode(size)

while True:
    for event in pygam.event.get():
        if event.type == pygame.QUIT:
            sys.exit()