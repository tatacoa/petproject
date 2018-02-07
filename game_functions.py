import sys
from time import sleep
import pygame
from bullet import Bullet
from rabbit import Rabbit


def check_keydown_events(event, ai_settings, screen, police, bullets):
    """respond to key actions"""
    if event.key == pygame.K_RIGHT:
        police.moving_right = True
    elif event.key == pygame.K_LEFT:
        police.moving_left = True
    elif event.key == pygame.K_SPACE:
        # create a new bullet
        fire_bullet(ai_settings, screen, police, bullets)


def fire_bullet(ai_settings, screen, police, bullets):
    """create new bullet"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, police)
        bullets.add(new_bullet)


def check_keyup_events(event, police):
    """respond to key actions"""
    if event.key == pygame.K_RIGHT:
        police.moving_right = False
    elif event.key == pygame.K_LEFT:
        police.moving_left = False


def check_events(ai_settings, screen, police, bullets):
    """response to keys and mouse movements"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, police, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, police)


def update_screen(ai_settings, screen, police, rabbits, bullets):
    """update the images in the screen"""
    # start the screen each time in the loop
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    police.blitme()
    rabbits.draw(screen)

    # keep the most recent screen visible
    pygame.display.flip()


def update_bullets(rabbits, bullets):
    """update the position of the bullets and clean old bullets"""
    # update bullet position
    bullets.update()
    pygame.sprite.groupcollide(bullets, rabbits,
                               True, True)
    # clean old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def get_number_rabbits_x(ai_settings, rabbit_width):
    """determine the number of rabbits in a line"""
    available_space_x = ai_settings.screen_width - \
        2 * rabbit_width
    number_rabbits_x = int(available_space_x /
                           (2 * rabbit_width))
    return number_rabbits_x


def create_rabbit(ai_settings, screen, rabbits, rabbit_number,
                  row_number):
    """create a rabbit"""
    rabbit = Rabbit(ai_settings, screen)
    rabbit_width = rabbit.rect.width
    rabbit.x = rabbit_width + 2 * rabbit_width * rabbit_number
    rabbit.rect.x = rabbit.x
    rabbit.rect.y = rabbit.rect.height + 2 * rabbit.rect.height\
        * row_number
    rabbits.add(rabbit)


def create_fleet(ai_settings, screen, police, rabbits):
    """create a family of rabbits"""
    """create rabbit and compute the number of rabbits
    per line """
    rabbit = Rabbit(ai_settings, screen)
    number_rabbits_x = get_number_rabbits_x(ai_settings,
                                            rabbit.rect.width)
    number_rows = get_number_rows(ai_settings, police.rect.height,
                                  rabbit.rect.height)

    # create a line of rabbits
    for row_number in range(number_rows):
        for rabbit_number in range(number_rabbits_x):
            create_rabbit(ai_settings, screen, rabbits,
                          rabbit_number, row_number)


def get_number_rows(ai_settings, police_height, rabbit_height):
    """compute the number of lines of rabbits"""
    available_space_y = (ai_settings.screen_height -
                         (3 * rabbit_height) - police_height)
    number_rows = int(available_space_y / (2 * rabbit_height))
    return number_rows


def check_family_edges(ai_settings, rabbits):
    """responds if a rabbit is on the edges"""
    for rabbit in rabbits.sprites():
        if rabbit.check_edges():
            change_family_direction(ai_settings, rabbits)
            break


def change_family_direction(ai_settings, rabbits):
    """descending and change direction"""
    for rabbit in rabbits.sprites():
        rabbit.rect.y += ai_settings.family_drop_speed
    ai_settings.family_direction *= -1


def police_hit(ai_settings, stats, screen, police, rabbits,
             bullets):
    if stats.polices_left > 0:
        stats.polices_left -= 1

        rabbits.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, police, rabbits)
        police.center_police()

        sleep(0.5)

    else:
        stats.game_active = False


def update_rabbits(ai_settings, stats, screen, police, rabbits,
                   bullets):
    check_family_edges(ai_settings, rabbits)
    rabbits.update()
    # verify collitions
    if pygame.sprite.spritecollideany(police, rabbits):
        print("Police Down")
        police_hit(ai_settings, stats, screen, police, rabbits,
                 bullets)
        check_rabbits_bottom(ai_settings, stats, screen, police,
                             rabbits, bullets)


def check_rabbits_bottom(ai_settings, stats, screen, police,
                         rabbits, bullets):
    screen_rect = screen.get_rect()
    for rabbit in rabbits.sprites():
        if rabbit.rect.bottom >= screen_rect.bottom:
            police_hit(ai_settings, stats, screen, police, rabbits,
                     bullets)
            break
