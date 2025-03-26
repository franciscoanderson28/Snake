#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame

#from Entity import Entity
from code.Const import WIDTH, GRID_SIZE, HEIGHT
from code.Entity import Entity


class Apple(Entity):
    def __init__(self):
        x = random.randint(0, (WIDTH//GRID_SIZE)-1) * GRID_SIZE
        y = random.randint(0, (HEIGHT//GRID_SIZE) - 1) * GRID_SIZE
        super().__init__("Apple", (x, y))
        self.surf = pygame.image.load('./asset/apple.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=(x, y))

    def move(self, ):
        pass

    def reposition(self, occupied_positions):
        available = [(x, y) for x in range(0, WIDTH, GRID_SIZE)
                     for y in range(0, HEIGHT, GRID_SIZE)
                     if (x, y) not in occupied_positions]
        if available:
            new_pos = random.choice(available)
            self.rect.topleft = new_pos