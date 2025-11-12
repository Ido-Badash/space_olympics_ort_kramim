import pygame
from typing import Tuple, Optional

class CollisionDetector:
    @staticmethod
    def check_aabb(rect_a: pygame.Rect, rect_b: pygame.Rect) -> bool:
        """Classic AABB collision check."""
        return (
            rect_a.x < rect_b.x + rect_b.width and
            rect_a.x + rect_a.width > rect_b.x and
            rect_a.y < rect_b.y + rect_b.height and
            rect_a.y + rect_a.height > rect_b.y
        )
        
    @staticmethod
    def get_overlap(rect_a: pygame.Rect, rect_b: pygame.Rect) -> Tuple[float, float]:
        """Calculate the overlap distance on both axes.
        
        Returns:
            Tuple of (overlap_x, overlap_y) - positive values indicate overlap amount"""
        pass
    
    @staticmethod
    def get_collision_normal(rect_a: pygame.Rect, rect_b: pygame.Rect) -> Tuple[int, int]:
        """
        (0, -1) = colliding from above (standing on platform).\n
        (0, 1)  = colliding from below (head hit ceiling).\n
        (-1, 0) = colliding from left.\n
        (1, 0)  = colliding from right.
        """
        
    @staticmethod
    def resolve_collision(body_a, body_b, normal: Optional[Tuple[int, int]] = None) -> Optional[str]:
        """
        Resolve collision between two physics bodies

        This separates the bodies and applies the right physics responses.
        """
        
    @staticmethod
    def check_one_way_platform(body_a, platform_rect: pygame.Rect, velocity_y: float) -> bool:
        """
        Special collision check for one way platforms (can jump through from below).
            
        Returns:
            True if should collide (landing from above), False if should pass through
        """
        pass
    
    @staticmethod
    def sweep_collision(start_pos: Tuple[float, float], 
                       end_pos: Tuple[float, float],
                       rect_size: Tuple[int, int],
                       obstacles: list) -> Optional[Tuple[float, float]]:
        """
        Continuous collision detection (prevents tunneling through thin objects).
        
        Uses line sweep to check if movement path intersects any obstacles.
        
        Returns:
            First collision point (x, y) or None if no collision
        """
        pass
        