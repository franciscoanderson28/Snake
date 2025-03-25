#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image

from code.Entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = list[Entity] = []
        self.background = pygame.image.load(f'./asset/')

    def run(self, ):
        pass
