import sys

import pygame
import random
from brick import Brick

def check_events(paddle):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                paddle.moving_right = True
            elif event.key == pygame.K_LEFT:
                paddle.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                paddle.moving_right = False
            elif event.key == pygame.K_LEFT:
                paddle.moving_left = False

def check_edges(ball, bo_settings):
    """Check if the ball hits edges"""
    if (ball.x + bo_settings.ball_width) > bo_settings.screen_width or ball.x < 0:
        ball.ball_angle = -ball.ball_angle
    if (ball.y + bo_settings.ball_height) > bo_settings.screen_height or ball.y  < 0:
        ball.ball_velocity = -ball.ball_velocity


def check_ball_hits_paddle(ball, paddle):
    """Check if ball hits the paddle."""
    if pygame.sprite.collide_rect(ball, paddle):
        ball.ball_velocity = -ball.ball_velocity
        ball.ball_angle = random.randint(-2, 2)

def check_ball_hits_brick(ball, bricks, bo_settings):
    """Check if ball hits a brick."""
    for brick in bricks.copy():
        if pygame.sprite.collide_rect(ball, brick):
            if ball.rect.left+5 >= brick.rect.right or ball.rect.right-5 <= brick.rect.left:
                ball.ball_angle = -ball.ball_angle
                brick.brick_health -= 1
                if brick.brick_health <= 0:
                    bricks.remove(brick)
                else:
                    brick.color = random.choice(bo_settings.soft_brick_colors)
            else:
                ball.ball_velocity = -ball.ball_velocity
                brick.brick_health -= 1
                if brick.brick_health <= 0:
                    bricks.remove(brick)
                else:
                    brick.color = random.choice(bo_settings.soft_brick_colors)




def get_number_bricks_x(bo_settings, brick_width):
    """Determine the number of bricks that fit in a row"""
    available_space_x = bo_settings.screen_width
    number_bricks_x = int(available_space_x / (brick_width))
    return number_bricks_x

def get_number_rows(bo_settings, brick_height):
    """Determine the nuber of rows of bricks that fit on the screen."""
    available_space_y = (bo_settings.screen_height/1.75) - (2 * brick_height)
    number_rows = int(available_space_y/brick_height)
    return number_rows

def create_brick(bo_settings, screen, bricks, brick_number, row_number):
    """Create a brick and place it in the row"""
    brick = Brick(bo_settings, screen)
    brick_width = brick.rect.width
    brick.x = (brick_width + 1)  * brick_number
    brick.rect.x = brick.x
    brick.rect.y = 2 * brick.rect.height +  (brick.rect.height + 1) * row_number
    bricks.add(brick)

def create_bricks(bo_settings, screen, bricks):
    """Create full set of bricks."""
    # Create bricks and find the number of bricks in a row
    # Spacing between each brick is one pixel.
    brick = Brick(bo_settings, screen)
    brick_width = brick.rect.width
    number_bricks_x = get_number_bricks_x(bo_settings, brick.rect.width)
    number_rows = get_number_rows(bo_settings, brick.rect.height)

    # Create all the bricks.
    for row_number in range(number_rows):
        for brick_number in range(number_bricks_x):
            create_brick(bo_settings, screen, bricks, brick_number, row_number)


def update_screen(bo_settings, screen, paddle, ball, bricks):
    """Update screen and flip to the new screen."""
    screen.fill(bo_settings.bg_color)
    paddle.draw_paddle()
    ball.draw_ball()
    for brick in bricks.sprites():
        brick.draw_brick()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
