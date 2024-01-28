'''
Author: Richard Zhang

Date: XX June 2022

Description:
The "sprint" sprite for the bullet hell game I create
'''

import pygame
import random

class SprintUI(pygame.sprite.Sprite):
    '''A sprintui screen subclass'''
    def __init__(self, screen):
        '''initializer for projectile object'''
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("sprint_icon.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.top = 825
        self.rect.left = 1025

    def pressed(self):
        self.image.set_alpha(150)

    def unpressed(self):
        self.image.set_alpha(255)

