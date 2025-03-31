import pygame
from code.Const import CELL_NUMBER, CELL_SIZE, COLOR_WHITE, COLOR_GOLD


class Level:
    def __init__(self, level_num=1):
        self.level_num = level_num
        self.load_assets()

    def load_assets(self):
        # Carrega música
        pygame.mixer.music.stop()
        pygame.mixer.music.load(f'asset/Level{self.level_num}.wav')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        self.fruit_image = pygame.image.load(f'asset/fruit{self.level_num}.png').convert_alpha()  # load fruit level
        self.background_image = pygame.image.load(f'asset/Level{self.level_num}.png').convert() # load background level
        self.background_image = pygame.transform.scale(
            self.background_image,(CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE)
        )

    def draw_score(self, screen, score, game_font):
        label_surface = game_font.render("Score: ", True, COLOR_GOLD)
        value_surface = game_font.render(str(score), True, COLOR_WHITE)
        label_pos = (20, 20)
        value_pos = (20 + label_surface.get_width(), 20)
        screen.blit(label_surface, label_pos)
        screen.blit(value_surface, value_pos)

    def change_level(self, new_level):
        self.level_num = new_level
        self.load_assets()

    def get_fruit_image(self):
        return self.fruit_image

    def get_background_image(self):
        return self.background_image
