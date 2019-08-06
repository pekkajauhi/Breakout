import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from paddle import Paddle
from ball import Ball
from brick import Brick
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    # Initialize pygame, settings and screen object.
    pygame.init()
    bo_settings = Settings()
    screen = pygame.display.set_mode((bo_settings.screen_width, bo_settings.screen_height))
    pygame.display.set_caption("Breakout")

    # Make the Play button.
    play_button = Button(bo_settings, screen, "Play")

    # Make a paddle, ball and a group of bricks.
    paddle = Paddle(screen, bo_settings)
    ball = Ball(screen, bo_settings, paddle)
    bricks = Group()

    # Create the bricks
    gf.create_bricks(bo_settings, screen, bricks)

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(bo_settings)
    sb = Scoreboard(bo_settings, screen, stats)

    clock = pygame.time.Clock()

    # Start the main loop for the game.
    while True:
        gf.check_events(ball, paddle, bo_settings, screen, bricks, stats, play_button)

        if stats.game_active:
            paddle.update()
            ball.update()
            gf.check_ball_hits_paddle(ball, paddle, bo_settings)
            gf.check_ball_hits_brick(paddle, ball, bricks, bo_settings, screen, stats, sb)
            gf.check_edges(paddle, ball, bo_settings, stats)
        gf.update_screen(bo_settings, screen, paddle, ball, bricks, stats, sb, play_button)

        clock.tick(50)
        #print(clock.get_fps())

run_game()
