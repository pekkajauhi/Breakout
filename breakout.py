import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from paddle import Paddle
from ball import Ball
from brick import Brick
import game_functions as gf

def run_game():
    # Initialize pygame, settings and screen object.
    pygame.init()
    bo_settings = Settings()
    screen = pygame.display.set_mode((bo_settings.screen_width, bo_settings.screen_height))
    pygame.display.set_caption("Breakout")

    # Make a paddle, ball and a group of bricks.
    paddle = Paddle(screen, bo_settings)
    ball = Ball(screen, bo_settings, paddle)
    bricks = Group()

    # Create the bricks
    gf.create_bricks(bo_settings, screen, bricks)

    # Start the main loop for the game.
    while True:
        gf.check_events(paddle)
        paddle.update()
        ball.update()
        gf.check_ball_hits_paddle(ball, paddle)
        gf.check_ball_hits_brick(ball, bricks, bo_settings)
        gf.check_edges(ball, bo_settings)
        gf.update_screen(bo_settings, screen, paddle, ball, bricks)

run_game()
