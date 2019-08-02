class Settings():
    """A class to store all settings for Breakout."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Paddle settings
        self.paddle_width = self.screen_width/5
        self.paddle_height = self.screen_height/28
        self.paddle_color = (100, 100, 100)
        self.paddle_speed_factor = 3

        # Ball settings
        self.ball_width = 20
        self.ball_height = 20
        self.ball_color = (10, 125, 125)
        self.ball_velocity = -1
        self.ball_angle = 1

        # Brick settings
        self.brick_height = self.screen_height/20
        self.brick_width = self.screen_width/6
        self.hard_brick_color = (100, 100, 100)
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        lightblue = (148, 189, 255)
        lightpurple = (255, 102, 255)
        lightgreen = (0, 204, 102)
        greyish = (153, 153, 102)
        reddish = (255, 51, 0)
        #self.brick_color = [lightblue, lightpurple, lightgreen, greyish, reddish, self.hard_brick_color]
        self.brick_color = [self.hard_brick_color]
        self.soft_brick_colors = [lightblue, lightpurple, lightgreen, greyish, reddish]
        self.brick_health = 1
        self.hard_brick_health = 2
