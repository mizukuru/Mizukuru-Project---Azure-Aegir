'''
Author: Richard Zhang

Date: XX June 2022

Description:
The UI sprite for the bullet hell game I create
'''

import pygame
import random

class UI(pygame.sprite.Sprite):
    '''A pause screen subclass'''
    def __init__(self, screen):
        '''initializer for projectile object'''
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("ui.png")
        self.image = pygame.transform.scale(self.image, (1280, 150))
        self.rect = self.image.get_rect()
        self.rect.top = 800
        self.rect.left = 0
