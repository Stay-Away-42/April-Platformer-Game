# I'll work on this - Jaime

import pygame

titleFont = pygame.font.Font("freesansbold.ttf", 72)
menuFont = pygame.font.Font("freesansbold.ttf", 48)

backgroundPic = pygame.image.load("menu.png").convert()
backgroundPic = pygame.transform.scale(backgroundPic, (1000, 600))

pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)


def text(text, font, color, surface, x, y, center=True):
    to = font.render(text, True, color)
    tr = to.get_rect()
    if center:
        tr.center = (x, y)
    else:
        tr.topleft = (x, y)


def start():
    print("start")


def options():
    print("option")
