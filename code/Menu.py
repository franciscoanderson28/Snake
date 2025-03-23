#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIDTH, COLOR_ORANGE, COLOR_WHITE, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/MenuS.wav')
        pygame.mixer_music.play(-1)
        #while True:
        self.window.blit(source=self.surf, dest=self.rect)
        self.menu_text(100, 'SNAKE ICE', COLOR_ORANGE, ((WIDTH / 2), 200))

        for i in range(len(MENU_OPTION)):
            self.menu_text(80, MENU_OPTION[i], COLOR_WHITE, ((WIDTH / 2), 400 + 70 * i))
        pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
