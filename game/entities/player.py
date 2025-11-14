import pygame
from game.core import BaseState, logger
from .entities import Entities


class Player(BaseState):
    def __init__(self, game=None):
        super().__init__(Entities.PLAYER, game)

    def startup(self):
        pass

    def cleanup(self):
        pass

    def get_event(self, event: pygame.event.Event):
        pass

    def draw(self, screen: pygame.Surface):
        pass

    def update(self, screen: pygame.Surface, dt: float):
        pass
