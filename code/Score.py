import pygame
from pygame import Surface, Rect, font

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_GOLD, COLOR_WHITE


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.background = pygame.image.load('./asset/Score.png').convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))




    def show_score(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(self.background, (0, 0))
        while True:

            pygame.display.flip()





    def save_score(self):
        pass