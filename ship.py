import pygame


class Ship():
    """start the player and gives their initial position"""
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # load the player image
        self.image = pygame.image.load("images/player.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each player in the low part of the screnn
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # accept  a float value to move the player
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the position of the player according to the mov flag"""
        # update the value of the center of the player
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update the object rect according to self.center
        self.rect.centerx = self.center

    def blitme(self):
        """show the player in the actual position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center the police"""
        self.center = self.screen_rect.centerx
