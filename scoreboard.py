import pygame.font

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, bo_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bo_settings = bo_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.quit_font = pygame.font.SysFont(None, 30)

        # Prepare hte initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_quit()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.bo_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.bo_settings.bg_color)

        # Put the high score at top left oc the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = 20
        self.high_score_rect.top = 20

    def prep_quit(self):
        """Turn the command info into a rendered image."""

        quit_str = "Q - quit game"
        self.quit_image = self.quit_font.render(quit_str, True, self.text_color, self.bo_settings.bg_color)

        # Display the score at the top right of the screen.
        self.quit_rect = self.quit_image.get_rect()
        self.quit_rect.left = 20
        self.quit_rect.bottom = self.screen_rect.bottom -20

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.quit_image, self.quit_rect)
