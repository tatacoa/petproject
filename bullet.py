import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """a class that rules the player bullets"""

    def __init__(self, ai_settings, screen, police):
        """create an object to shoot the bullest from the object"""
        super(Bullet, self).__init__()
        self.screen = screen

        # create a rect in (0, 0), and define the rigth position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = police.rect.centerx
        self.rect.top = police.rect.top

        # store the bullet position as float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """"Move the bullet in the screen"""
        # update bullet position
        self.y -= self.speed_factor
        # update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
