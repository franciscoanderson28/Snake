import pygame
from code.Const import CELL_NUMBER, CELL_SIZE, COLOR_WHITE, COLOR_ORANGE


class Level:
    def __init__(self, level_num=1):
        self.level_num = level_num
        self.load_music()

    #Music Level
    def load_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(f'asset/Level{self.level_num}.wav')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def draw_score(self, screen, score, fruit_image, game_font):
        SCORE_LABEL_COLOR = (255, 215, 0)
        SCORE_VALUE_COLOR = (255, 255, 255)
        label_surface = game_font.render("Score: ", True, SCORE_LABEL_COLOR)
        value_surface = game_font.render(str(score), True, SCORE_VALUE_COLOR)
        label_pos = (20, 20)
        value_pos = (20 + label_surface.get_width(), 20)
        screen.blit(label_surface, label_pos)
        screen.blit(value_surface, value_pos)


    def change_level(self, new_level):
        self.level_num = new_level
        self.load_music()