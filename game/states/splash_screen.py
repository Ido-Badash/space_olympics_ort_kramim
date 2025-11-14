from game.core import BaseState, logger, Colors
import pygame
from .states import States
from game.utils import clamp_alpha, mid_pos
from game.ui import FadeTransition  # assuming you saved it here


class SplashScreen(BaseState):
    def __init__(self, game=None):
        super().__init__(States.SPLASH_SCREEN, game)

        # --- text fade ---
        self.base_font_ratio = 4
        self.sizing_speed = 1
        self.text_transition = FadeTransition()

        # --- black screen fade ---
        self.fade_transition = FadeTransition(
            size=(self.game.width, self.game.height),
        )

    def startup(self):
        pygame.display.set_caption("Splash")
        self.base_font_ratio = 4
        self.text_transition.startup()
        self.fade_transition.startup()

    def cleanup(self):
        pass

    def get_event(self, event: pygame.event.Event):
        pass

    def draw(self, screen: pygame.Surface):
        # background
        screen.fill(Colors.PLATINUM)

        # text
        text_size = min(self.game.width, self.game.height) // self.base_font_ratio
        text_surf, text_rect = self.game.font.render(
            "Splash", Colors.DARK_GREEN, size=text_size
        )
        text_surf.set_alpha(self.text_transition.alpha)
        screen.blit(text_surf, mid_pos(self.game.size, text_rect))

        # black overlay fade
        self.fade_transition.draw(screen)

    def update(self, screen: pygame.Surface, dt: float):
        # update text alpha
        self.text_transition.update(dt)
        self.base_font_ratio += self.sizing_speed * dt

        # update black fade
        self.fade_transition.set_size(self.game.size)
        self.fade_transition.update(dt)

        # switch state when both fades are done
        if self.fade_transition.is_done():
            self.game.sm.set_state(States.MENU)
