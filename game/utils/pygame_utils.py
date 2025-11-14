import pygame
from pathlib import Path
from typing import Tuple


def load_sprite(path: str):
    p = Path(path)
    if p.exists():
        return pygame.image.load(path).convert_alpha()
    else:
        print(f"Warning: Sprite not found: {path}")
        return None


def mid_pos(screen_size: Tuple[int, int], rect: pygame.Rect) -> Tuple[int, int]:
    return (
        screen_size[0] // 2 - rect.w // 2,
        screen_size[1] // 2 - rect.h // 2,
    )
