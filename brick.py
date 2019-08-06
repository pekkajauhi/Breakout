import pygame
from pygame.sprite import Sprite
import random

class Brick(Sprite):
    """A class to represent a single brick."""

    def __init__(self, bo_settings, screen, row_number):
        """Initialize the brick and set it's starting position."""
        super(Brick, self).__init__()
        self.screen = screen
        self.bo_settings = bo_settings

        # Create a ball rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, bo_settings.brick_width, bo_settings.brick_height)
        self.rect.x = 0
        self.rect.y = self.rect.height*3

        if row_number == 0 or row_number == 8:
            self.color = bo_settings.hard_brick_color
        else:
            color = random.choice(bo_settings.brick_color)
            self.color = color

        if self.color == bo_settings.hard_brick_color:
            self.brick_health = bo_settings.hard_brick_health
        else:
            self.brick_health = bo_settings.brick_health

    def draw_brick(self):
        """Draw the ball to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
