'''
Author: Richard Zhang

Date: XX June 2022

Description:
The "shrink" sprite for the bullet hell game I create
'''

import pygame
import random

class ShrinkUI(pygame.sprite.Sprite):
    '''A shrinkui screen subclass'''
    def __init__(self, screen):
        '''initializer for projectile object'''
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("shrink_icon.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.cd = 0
        self.rect.top = 825
        self.rect.left = 1150
        self.warning = pygame.mixer.Sound("hit.wav")

    def pressed(self):
        self.cd = 8*30

    def update(self):
        if(self.cd > 0):
            self.cd -= 1
            self.image.set_alpha(150)
        else:
            self.image.set_alpha(255)

        if(self.cd == 6 * 30):
            self.warning.play()

    def cd_over(self):
        return self.cd == 0

