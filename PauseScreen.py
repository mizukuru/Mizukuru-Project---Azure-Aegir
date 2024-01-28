'''
Author: Richard Zhang

Date: XX June 2022

Description:
The pause screen sprite for the bullet hell game I create
'''

import pygame
import random

class PauseScreen(pygame.sprite.Sprite):
    '''A pause screen subclass'''
    def __init__(self, screen):
        '''initializer for projectile object'''
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("pausescreen.png")
        self.image = pygame.transform.scale(self.image, (1280, 800))
        self.image.set_alpha(170)
        self.rect = self.image.get_rect()

