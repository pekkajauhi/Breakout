
import pygame
from pygame.sprite import Sprite


class Paddle(Sprite):

    def __init__(self, screen, bo_settings):
        """Initialize the paddle and set its starting position."""
        super(Paddle, self).__init__()
        self.screen = screen
        self.bo_settings = bo_settings

        # Create a paddle rect.
        self.rect = pygame.Rect(0, 0, bo_settings.paddle_width, bo_settings.paddle_height)
        self.screen_rect = screen.get_rect()

        # Put the padlle at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 50

        # Store a decimal value for the paddle's center
        self.center = float(self.rect.centerx)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False

        self.color = bo_settings.paddle_color

    def update(self):
        """Update the paddle's position based on the movement flag."""
        # Update the paddle's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.bo_settings.paddle_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.bo_settings.paddle_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def draw_paddle(self):
        """Draw the paddle to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def center_paddle(self):
        self.center = self.screen_rect.centerx
