#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.examples.grid import Game

from code.Const import WIDTH, HEIGHT, MENU_OPTION, COLOR_BLACK, COLOR_ORANGE, COLOR_WHITE
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self, ):

        pygame.init()
        self.window = pygame.display.set_mode(size=(WIDTH, HEIGHT))
        pygame.display.set_caption('Snake Ice')
        self.font = pygame.font.SysFont("Lucida Sans Typewriter", 60)

    def show_game_over(self, score):
        self.window.fill(COLOR_BLACK)
        texts = [
            self.font.render("GAME OVER", True, COLOR_ORANGE),
            self.font.render(f"Score: {score}", True, COLOR_WHITE),
            self.font.render("Press ENTER", True, COLOR_WHITE)
        ]
        for i, text in enumerate(texts):
            self.window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 100 + i * 80))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "QUIT"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting = False
        return "MENU"

    def run(self):
        while True:
            # Menu
            menu = Menu(self.window)
            option = menu.run()

            if option == "START":
                # Jogo principal
                level = Level(self.window)
                result = level.run()

                # Game Over
                if result == "GAME_OVER":
                    action = self.show_game_over(level.score)
                    if action == "QUIT":
                        break

            elif option == "EXIT":
                break

        pygame.quit()



