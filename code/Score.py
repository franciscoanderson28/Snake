import sys
from datetime import datetime
import pygame
from pygame import Surface, Rect, font, KEYDOWN, K_RETURN, K_BACKSPACE
from pygame.font import Font
from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_GOLD, COLOR_WHITE, SCORE_POS, MENU_OPTION, COLOR_ORANGE
from code.DBProxy import DBProxy

class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.background = pygame.image.load('./asset/Score.jpg').convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(self.background, (0, 0))
            self.score_text(70, 'TOP 5 SCORE', COLOR_ORANGE, SCORE_POS['Title'])
            self.score_text(30, 'NAME           SCORE                          DATE   ', COLOR_GOLD, SCORE_POS['Label'])

            db_proxy = DBProxy('DBScore')
            list_score = db_proxy.retrieve_top5()
            db_proxy.close()

            for play_score in list_score:
                id_, name, score, date = play_score
                self.score_text(20, f'                 {name}                           {score:05d}                                  {date}', COLOR_WHITE,
                                SCORE_POS[list_score.index(play_score)])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            pygame.display.flip()
    def save(self, score):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        name = ''
        db_proxy = DBProxy('DBScore')
        while True:
            self.window.blit(self.background, (0, 0))
            self.score_text(55, 'GAME OVER', COLOR_GOLD, SCORE_POS['Title'])
            text = 'Enter Your Name (4 Characters):'
            self.score_text(30, text, COLOR_WHITE, SCORE_POS['EnterName'])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        db_proxy.close()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4 and event.unicode.isalpha():
                            name += event.unicode.upper()

            self.score_text(30, name, COLOR_WHITE, SCORE_POS['Name'])
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('asset/PoetsenOne-Regular.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    return current_datetime.strftime("%d/%m/%Y %H:%M:%S")
