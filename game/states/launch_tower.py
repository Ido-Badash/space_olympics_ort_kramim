import pygame
import gif_pygame
from game.core import BaseState
from game.ui import FadeTransition, Colors
from .states import States
from game.entities import Rocket
from game.utils import mid_pos


class LaunchTower(BaseState):
    def __init__(self, game=None):
        super().__init__(States.LAUNCH_TOWER, game)

        self.fade_transition = FadeTransition(
            size=(self.game.width, self.game.height),
            starting_alpha=255,
            ending_alpha=0,
        )

        self.bg_gif = gif_pygame.load(self.game.ss.get("launch_tower_bg_gif_path"))
        self.bg_gif_surf = None

        # --- text 1 ---
        self.text1_base_ratio = 20
        self.text1_rect = None
        self.text1_surf = None
        self.text1_pos = (0, 0)
        self.text1_color = (*Colors.WHITE, 240)

        # --- text 2 ---
        self.text2_base_ratio = 25
        self.text2_rect = None
        self.text2_surf = None
        self.text2_pos = (0, 0)
        self.text2_color = (*Colors.PLATINUM, 220)

        # --- text 3 ---
        self.text3_base_ratio = 30
        self.text3_rect = None
        self.text3_surf = None
        self.text3_pos = (0, 0)
        self.text3_color = (*Colors.CRIMSON, 200)

        # --- rockets ---
        r_size_ratio = (0.08, 0.20)  # width=8% of screen, height=20%

        self.rocket_weak = Rocket(
            size_ratio=r_size_ratio,
            x_ratio=0.20,
            speed=200,
            image_path="assets/images/rocket.png",
        )

        self.rocket_medium = Rocket(
            size_ratio=r_size_ratio,
            x_ratio=0.50,
            speed=350,
            image_path="assets/images/rocket.png",
        )

        self.rocket_strong = Rocket(
            size_ratio=r_size_ratio,
            x_ratio=0.80,
            speed=500,
            image_path="assets/images/rocket.png",
        )

    def startup(self):
        pygame.display.set_caption(self.name.value)
        self.fade_transition.startup()
        self.rocket_weak.startup()
        self.rocket_medium.startup()
        self.rocket_strong.startup()

    def cleanup(self):
        pass

    def get_event(self, event):
        self.rocket_weak.get_event(event)
        self.rocket_medium.get_event(event)
        self.rocket_strong.get_event(event)

    def draw(self, screen: pygame.Surface):
        # --- draw background ---
        screen.blit(self.bg_gif_surf, (0, 0))
        self.bg_gif._animate()

        # --- draw texts ---
        screen.blit(self.text1_surf, self.text1_pos)
        screen.blit(self.text2_surf, self.text2_pos)
        screen.blit(self.text3_surf, self.text3_pos)
        # TODO: Make a class called `TextLine``.
        # - text
        # - font
        # - color
        # - base ratio
        # - padding (all dirictions)
        # - position
        # - size
        # ? Will be used for the class `MultiLine`.

        # TODO: Make a class named `MultiLine` for pygame text.
        # - list[TextLine]
        # ? will handle the drawing + updating for each line in a stack.

        # --- draw rockets ---
        self.rocket_weak.draw(screen)
        self.rocket_medium.draw(screen)
        self.rocket_strong.draw(screen)

        # --- draw fade transition ---
        self.fade_transition.draw(screen)

    def update(self, screen, dt):
        # --- bg gif ---
        bg_frame, _ = self.bg_gif.get_current_frame_data()
        self.bg_gif_surf = pygame.transform.scale(bg_frame, self.game.size)

        self.fade_transition.set_size(self.game.size)
        self.fade_transition.update(dt)

        # --- text 1 ---
        self.text1_surf, self.text1_rect = self.game.font.render(
            "Artemis wants to test out some rockets",
            self.text1_color,
            size=self.game.size_depended(self.text1_base_ratio),
        )
        self.text1_rect.centerx = self.game.width // 2
        self.text1_pos = (
            self.text1_rect.x,
            self.text1_rect.y,
        )

        # --- text 2 ---
        self.text2_surf, self.text2_rect = self.game.font.render(
            "Find the strongest rocket so they can fly to the moon.",
            self.text2_color,
            size=self.game.size_depended(self.text2_base_ratio),
        )
        self.text2_rect.centerx = self.game.width // 2
        self.text2_pos = (
            self.text2_rect.x,
            self.text1_pos[1] + self.text1_rect.height + 12,
        )

        # --- text 3 ---
        self.text3_surf, self.text3_rect = self.game.font.render(
            "(Click the rockets to launch them)",
            self.text3_color,
            size=self.game.size_depended(self.text3_base_ratio),
        )
        self.text3_rect.centerx = self.game.width // 2
        self.text3_pos = (
            self.text3_rect.x,
            self.text2_pos[1] + self.text2_rect.height + 15,
        )

        # --- update rockets ---
        self.rocket_weak.update(screen, dt)
        self.rocket_medium.update(screen, dt)
        self.rocket_strong.update(screen, dt)
