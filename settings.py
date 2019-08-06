class Settings():
    """A class to store all settings for Breakout."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Paddle settings
        self.paddle_width = self.screen_width/6
        self.paddle_height = self.screen_height/28
        self.paddle_color = (100, 100, 100)

        # Ball settings
        self.ball_width = 20
        self.ball_height = 20
        self.ball_color = (10, 125, 125)
        self.ball_limit = 3

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
        self.brick_color = [lightblue, lightpurple, lightgreen, greyish, reddish, self.hard_brick_color]
        #self.brick_color = [self.hard_brick_color]
        self.soft_brick_colors = [lightblue, lightpurple, lightgreen, greyish, reddish]
        self.brick_health = 1
        self.hard_brick_health = 2

        # How quickly the game speeds up
        self.speedup_scale = 1.2
        # How quickly the point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.paddle_speed_factor = 15
        self.ball_speed_factor = 6
        self.ball_velocity = -6
        self.ball_angle = 6

        # Scoring
        self.brick_points = 50

    def increase_speed(self):
        """Increase speed and score settings."""
        self.paddle_speed_factor *= self.speedup_scale
        self.ball_speed_factor *= self.speedup_scale
        self.ball_velocity *= self.speedup_scale
        self.ball_angle *= self.speedup_scale

        self.brick_points = int(self.brick_points * self.score_scale)
        print(self.brick_points)
