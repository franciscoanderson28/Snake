import random
import pygame
from pygame.math import Vector2
from code.Const import CELL_NUMBER


class Fruit:
    def __init__(self):
        self.randomize()

    def draw(self, screen, fruit_image, cell_size):
        fruit_rect = pygame.Rect(
            int(self.pos.x * cell_size),
            int(self.pos.y * cell_size),
            cell_size,
            cell_size
        )
        screen.blit(fruit_image, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)