#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from abc import ABC, abstractmethod

from code.Const import GRID_SIZE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.position = position
        self.surf = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.rect = self.surf.get_rect(topleft=position)

    @abstractmethod
    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

