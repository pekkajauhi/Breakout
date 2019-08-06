import sys

import pygame
import random
from brick import Brick
from time import sleep

def check_events(ball, paddle, bo_settings, screen, bricks, stats, play_button):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                paddle.moving_right = True
            elif event.key == pygame.K_LEFT:
                paddle.moving_left = True
            elif event.key == pygame.K_q:
                with open('high_score.txt', 'w') as file_object:
                    file_object.write(str(stats.high_score))
                sys.exit()
            elif event.key == pygame.K_r:
                with open('high_score.txt', 'w') as file_object:
                    file_object.write(str(0))
                stats.high_score = 0

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                paddle.moving_right = False
            elif event.key == pygame.K_LEFT:
                paddle.moving_left = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ball, paddle, bo_settings, screen, bricks, stats, play_button, mouse_x, mouse_y)

def check_play_button(ball, paddle, bo_settings, screen, bricks, stats, play_button, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        bo_settings.initialize_dynamic_settings()
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Empty the list of bricks.
        bricks.empty()

        # Create  new bricks and center the ball.
        create_bricks(bo_settings, screen, bricks)
        ball.center_ball(bo_settings)
        paddle.center_paddle()

def check_edges(paddle, ball, bo_settings, stats):
    """Check if the ball hits edges"""
    if (ball.x + bo_settings.ball_width) > bo_settings.screen_width or ball.x < 0:
        ball.ball_angle = -ball.ball_angle
    if ball.y  < 0:
        ball.ball_velocity = -ball.ball_velocity
    if (ball.y + bo_settings.ball_height) > bo_settings.screen_height:
        #ball.ball_velocity = -ball.ball_velocity
        stats.balls_left -= 1
        if stats.balls_left > 0:
            ball.center_ball(bo_settings)
            paddle.center_paddle()
            sleep(0.5)
        else:
            print("Game Over!")
            stats.game_active = False
            pygame.mouse.set_visible(True)


def check_ball_hits_paddle(ball, paddle, bo_settings):
    """Check if ball hits the paddle."""
    if pygame.sprite.collide_rect(ball, paddle):
        ball.ball_velocity = -ball.ball_velocity
        ball.ball_angle = random.randint(-int(bo_settings.ball_speed_factor), int(bo_settings.ball_speed_factor))


def check_ball_hits_brick(paddle, ball, bricks, bo_settings, screen, stats, sb):
    """Check if ball hits a brick."""
    for brick in bricks.copy():
        if pygame.sprite.collide_rect(ball, brick):
            if ball.rect.left+5 >= brick.rect.right or ball.rect.right-5 <= brick.rect.left:
                ball.ball_angle = -ball.ball_angle
                brick.brick_health -= 1
                if brick.brick_health <= 0:
                    bricks.remove(brick)
                    stats.score += bo_settings.brick_points
                    sb.prep_score()
                else:
                    brick.color = random.choice(bo_settings.soft_brick_colors)
            else:
                ball.ball_velocity = -ball.ball_velocity
                brick.brick_health -= 1
                if brick.brick_health <= 0:
                    bricks.remove(brick)
                    stats.score += bo_settings.brick_points
                    sb.prep_score()
                else:
                    brick.color = random.choice(bo_settings.soft_brick_colors)
            check_high_score(stats, sb)
    if len(bricks) == 0:
        # Create new bricks.
        bo_settings.increase_speed()
        ball.center_ball(bo_settings)
        paddle.center_paddle()
        sleep(0.5)
        create_bricks(bo_settings, screen, bricks)


def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
        sb.prep_quit()


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
    brick = Brick(bo_settings, screen, row_number)
    brick_width = brick.rect.width
    brick.x = (brick_width + 1)  * brick_number
    brick.rect.x = brick.x
    brick.rect.y = 2 * brick.rect.height +  (brick.rect.height + 1) * row_number
    bricks.add(brick)

def create_bricks(bo_settings, screen, bricks):
    """Create full set of bricks."""
    # Create bricks and find the number of bricks in a row
    # Spacing between each brick is one pixel.
    brick = Brick(bo_settings, screen, 1)
    brick_width = brick.rect.width
    number_bricks_x = get_number_bricks_x(bo_settings, brick.rect.width)
    number_rows = get_number_rows(bo_settings, brick.rect.height)

    # Create all the bricks.
    for row_number in range(number_rows):
        for brick_number in range(number_bricks_x):
            create_brick(bo_settings, screen, bricks, brick_number, row_number)


def update_screen(bo_settings, screen, paddle, ball, bricks, stats, sb, play_button):
    """Update screen and flip to the new screen."""
    screen.fill(bo_settings.bg_color)
    paddle.draw_paddle()
    ball.draw_ball()
    for brick in bricks.sprites():
        brick.draw_brick()

    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
