import pygame

from game.core import BaseState, Colors, logger
from game.states import States
from game.widgets import Player

class Night1(BaseState):
    def __init__(self, game=None):
        super().__init__(States.NIGHT_1, game)
        self.player = None
        
    def startup(self):
        pygame.display.set_caption("Night 1")
        self.player = Player(self.game.screen.get_size())

    def get_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.done = True
            self.next = States.MENU
        self.player.handle_event(event)

    def draw(self, screen: pygame.Surface):
        screen.fill(Colors.KHAKI)
        self.player.draw(screen)

    def update(self, screen, dt):
        self.player.update(dt)
