#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_ORANGE, COLOR_WHITE, MENU_OPTION, COLOR_YELLOW, SCREEN_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu1.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(100, 'SNAKE ICE', COLOR_ORANGE, ((SCREEN_WIDTH/ 2), 200))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(80, MENU_OPTION[i], COLOR_YELLOW, ((SCREEN_WIDTH / 2), 400 + 70 * i))
                else:
                    self.menu_text(80, MENU_OPTION[i], COLOR_WHITE, ((SCREEN_WIDTH / 2), 400 + 70 * i))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_RETURN:
                        pygame.mixer_music.stop()
                        return MENU_OPTION[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("asset/PoetsenOne-Regular.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
