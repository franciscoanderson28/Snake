import pygame
import sys
from pygame.math import Vector2
from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, CELL_NUMBER, MENU_OPTION
from code.Fruit import Fruit
from code.Level import Level
from code.Menu import Menu
from code.Score import Score
from code.Snake import Snake


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('GAME SNAKE')
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.fruit = Fruit()
        self.level = Level()

        # Carrega os assets
        self.fruit_image = pygame.image.load('asset/cherry.png').convert_alpha()
        self.background_image = pygame.image.load('asset/Level1.png').convert()
        self.background_image = pygame.transform.scale(self.background_image,
                                                       (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game_font = pygame.font.Font('asset/PoetsenOne-Regular.ttf', 25)

        self.SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.SCREEN_UPDATE, 150)
        self.game_active = False

    def show_menu(self):
        menu = Menu(self.screen)
        return menu.run()

    def run(self):
        while True:
            score = Score(self.show_menu)
            option = self.show_menu()
            if option == "START":
                self.game_active = True
                self.reset_game()
                self.game_loop()
            elif option == "SCORE":
                score.show_score()
            elif option == "EXIT":
                pygame.quit()
                sys.exit()

    def game_loop(self):
        while self.game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == self.SCREEN_UPDATE:
                    self.update()
                if event.type == pygame.KEYDOWN:
                    self.handle_input(event.key)
                    if event.key == pygame.K_ESCAPE:  # Volta ao menu
                        self.game_active = False
                        return
                self.screen.blit(self.background_image, (0, 0))
                self.draw_elements()
                pygame.display.update()
                self.clock.tick(60)

    def reset_game(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.level = Level()

    def handle_input(self, key):
        if key == pygame.K_UP and self.snake.direction.y != 1:
            self.snake.direction = Vector2(0, -1)
        if key == pygame.K_DOWN and self.snake.direction.y != -1:
            self.snake.direction = Vector2(0, 1)
        if key == pygame.K_LEFT and self.snake.direction.x != 1:
            self.snake.direction = Vector2(-1, 0)
        if key == pygame.K_RIGHT and self.snake.direction.x != -1:
            self.snake.direction = Vector2(1, 0)

    def update(self):
        self.snake.move()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw(self.screen, self.fruit_image, CELL_SIZE)
        self.snake.draw(self.screen, CELL_SIZE)
        self.level.draw_score(
            self.screen,
            (len(self.snake.body) - 3) * 10,
            self.fruit_image,
            self.game_font
        )

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_food_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < CELL_NUMBER or not 0 <= self.snake.body[0].y < CELL_NUMBER:
            self.game_over()

        for block in self.snake.body[1:]:
            if self.snake.body[0] == block:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()
