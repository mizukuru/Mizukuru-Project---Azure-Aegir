'''
Author: Richard Zhang

Date: XX June 2022

Description:
The projectile sprite for the bullet hell game I create
'''

import pygame
import random
import math

class Projectile(pygame.sprite.Sprite):
    '''class that simulates a projectile'''
    def __init__(self, screen, angle, speed, startingpos):
        '''initializer for projectile object'''
        pygame.sprite.Sprite.__init__(self)
        self.offset = 150
        self.screen = screen
        self.angle = angle
        self.speed = speed * 1.2
        self.image = pygame.image.load("projectile1.png")
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect()
        #self.rect = self.rect.inflate(-16, -16)
        self.rect.center = startingpos
        #print(angle, end= ', ')
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        '''update projectile object method'''
        if(self.rect.left < 0):
            self.kill()
        if(self.rect.right > self.screen.get_width()):
            self.kill()
        if(self.rect.top < 0):
            self.kill()
        if(self.rect.bottom > self.screen.get_height() - self.offset):
            self.kill()


        self.rect.centerx += self.speed * math.sin(math.radians(self.angle))
        self.rect.centery += self.speed * math.cos(math.radians(self.angle))

