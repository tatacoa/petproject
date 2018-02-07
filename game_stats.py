class GameStats():
    """store game stats"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.polices_left = self.ai_settings.police_limit
