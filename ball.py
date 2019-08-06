import pygame
import random


class Ball():
    """Initialize the ball and set it's position."""

    def __init__(self, screen, bo_settings, paddle):
        """Initialize the paddle and set its starting position."""
        super(Ball, self).__init__()
        self.screen = screen
        self.bo_settings = bo_settings

        # Create a ball rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, bo_settings.ball_width, bo_settings.ball_height)
        self.rect.centerx = paddle.rect.centerx
        self.rect.bottom = paddle.rect.top
        self.screen_rect = screen.get_rect()


        # Store the ball's position as a decimal value
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.color = bo_settings.ball_color
        self.ball_speed_factor = bo_settings.ball_speed_factor
        self.ball_velocity = bo_settings.ball_velocity
        self.ball_angle = bo_settings.ball_angle

    def update(self):
        """"Move the ball."""
        # Update the decimal position of the ball.
        self.y += self.ball_velocity
        self.x += self.ball_angle
        # Update the rect position
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ball(self, bo_settings):
        """Center the ball on the screen."""
        self.y = 400
        self.x = 500
        self.ball_velocity = bo_settings.ball_speed_factor
        self.ball_angle = 0


    def draw_ball(self):
        """Draw the ball to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
