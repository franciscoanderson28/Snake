#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIDTH, HEIGHT, MENU_OPTION
from code.Menu import Menu


class Game:
    def __init__(self, ):

        pygame.init()
        self.window = pygame.display.set_mode(size=(WIDTH, HEIGHT))
        pygame.display.set_caption('Snake Ice')
        clock = pygame.time.Clock()

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

