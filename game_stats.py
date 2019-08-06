class GameStats():
    """Track game statistics for breakout."""
    def __init__(self, bo_settings):
        """Initialize statistics."""
        self.bo_settings = bo_settings
        self.reset_stats()

        # Start breakout in an inactive state
        self.game_active = False

        # High score should never be reset
        with open('high_score.txt') as file_object:
            contents = file_object.read()
        self.high_score = int(contents)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.balls_left = self.bo_settings.ball_limit
        self.score = 0
