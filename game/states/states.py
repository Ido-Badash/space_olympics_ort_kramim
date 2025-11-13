from enum import Enum


class States(str, Enum):
    SPLASH_SCREEN = "Splash Screen"
    MENU = "Menu"
    PAUSE_MENU = "Pause Menu"
    CREDITS = "Credits"
