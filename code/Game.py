#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIDTH, HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self, ):

        pygame.init()
        self.window = pygame.display.set_mode(size=(WIDTH, HEIGHT))
        pygame.display.set_caption('Snake Ice')

    def run(self, ):

        menu = Menu(self.window)
        menu.run()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()