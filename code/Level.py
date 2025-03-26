#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image

from code.Apple import Apple
from code.Const import WIDTH, HEIGHT, FPS, COLOR_WHITE
from code.Entity import Entity
from code.Snake import Snake


class Level:
    def __init__(self, window):
        self.window = window
        self.snake = Snake()
        self.apple = Apple()
        self.score = 0
        self.font = pygame.font.SysFont('Lucida Sans Typewriter', 30)
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load('./asset/Level1.png').convert()
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

    def check_collisions(self):
        head = self.snake.body[0]

        # encontro com a maçã
        if head.colliderect(self.apple.rect):
            self.snake.grow_to += 1
            self.score += 10
            self.apple.reposition([(seg.x, seg.y) for seg in self.snake.body])

            # Colisão com paredes/corpo
        if (head.x < 0 or head.x >= WIDTH or
                head.y < 0 or head.y >= HEIGHT or
                any(head.colliderect(seg) for seg in self.snake.body[1:])):
            return True
        return False

    def run(self):
        running = True
        while running:
            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "QUIT"
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                        self.snake.change_direction(event.key)

            # Atualização
            self.snake.update()
            if self.check_collisions():
                return "GAME_OVER"

            # Renderização
            self.window.blit(self.background, (0, 0))
            self.apple.draw(self.window)
            self.snake.draw(self.window)

            # Placar
            score_text = self.font.render(f"Score: {self.score}", True, COLOR_WHITE)
            self.window.blit(score_text, (10, 10))

            pygame.display.flip()
            self.clock.tick(FPS)


