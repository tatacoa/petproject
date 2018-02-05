'''
file doc
'''
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from rabbit import Rabbit


def run_game():
    '''
    start the game and build an screen object
    '''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Rabbit in Tierpark")

    # create a player
    ship = Ship(ai_settings, screen)
    # create a group to store the bullets
    bullets = Group()
    rabbits = Group()
    # create a familiy of rabbits
    gf.create_fleet(ai_settings, screen, ship, rabbits)

    # start the inicial loop of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_rabbits(ai_settings, rabbits)
        gf.update_screen(ai_settings, screen, ship, rabbits, bullets)


run_game()
