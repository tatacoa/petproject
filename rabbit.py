import pygame
from pygame.sprite import Sprite


class Rabbit(Sprite):
    """a clas that represent a single rabbit"""

    def __init__(self, ai_settings, screen):
        """define the rabbit and the initial position"""
        super(Rabbit, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load an image for the rabbit at the top
        self.image = pygame.image.load('images/rabbit.png')
        self.rect = self.image.get_rect()

        # start new rabbits at the top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the rabbit position
        self.x = float(self.rect.x)

    def blitme(self):
        """actual position of the rabbit"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """"true if the rabbit is at the end of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move rabbits to the right or left"""
        self.x += (self.ai_settings.rabbit_speed_factor *
                   self.ai_settings.family_direction)
        self.rect.x = self.x
