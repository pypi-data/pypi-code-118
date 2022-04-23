# -*- coding: utf-8 -*-
"""
Module initializing screen object and screen values.
"""
import pygame
from .path import *

# Change neuropsydia.screen to "__main__" When building API documentation. This is to avoid sphinx to run this code, otherwise the documentations fails to be built. "neuropsydia.screen" to make it work.

if __name__ == "myNeuropsydia.screen":

    pygame.display.set_icon(pygame.image.load(Path.logo() + 'icon.png'))
    screen = pygame.display.set_mode((0,0), pygame.SRCALPHA | pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)

    pygame.display.set_caption('Neuropsydia')
    screen_width, screen_height = screen.get_size()
    monitor_diagonal = 24  # inch

else:
    print('OOPS')
    print(__name__)
    screen = "Placeholder"
    screen_width, screen_height = 0, 0
    monitor_diagonal = 24