class Settings():
    """a class to store all the configutations of the game"""
    def __init__(self):
        """start the game configurations"""
        # Screen configuration
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (30, 154, 83)

        # police configuration
        self.police_speed_factor = 1.5
        self.police_limit = 3

        # bullets configuration
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Rabbit configuration
        self.rabbit_speed_factor = 1
        self.family_drop_speed = 10
        self.family_direction = 1
