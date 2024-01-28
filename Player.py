'''
Author: Richard Zhang

Date: XX June 2022

Description:
The Player sprite for the bullet hell game I create
'''

import pygame
import random

class Player(pygame.sprite.Sprite):
    '''class that simulates a player'''

    def __init__(self, screen):
        '''initializer for player object'''
        pygame.sprite.Sprite.__init__(self)
        self.offset = 150
        self.screen = screen
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = screen.get_width() // 2
        self.rect.centery = screen.get_height() - 50
        self.tempx = self.rect.centerx
        self.tempy = self.rect.centery
        self.speed = 4
        self.unshrink_timer = -1
        self.flash = 0
        self.flashframes = []
        for i in range(6):
            for j in range(1,11):
                if(i%2 == 0):
                    self.flashframes.append(255 * (1-j/10))
                else:
                    self.flashframes.append(255 * (j/10))

    def getSpeed(self):
        return self.speed

    def increaseSpeed(self):
        '''increases the self.speed variable by a factor of 1.5'''
        self.speed *= 1.2
        self.speed = self.speed
        if(self.speed > 20):
            self.speed = 20

    def move_up(self):
        '''move up function'''
        self.rect.centery -= self.speed

    def move_down(self):
        '''move down function'''
        self.rect.centery += self.speed

    def move_left(self):
        '''move left function'''
        self.rect.centerx -= self.speed

    def move_right(self):
        '''move right function'''
        self.rect.centerx += self.speed

    def flicker(self):
        '''function that starts a "flicker" effect (or initiates it)'''
        self.flash = 60

    def shrink(self):
        '''function that shrinks your character'''
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (48, 48))
        tempx = self.rect.centerx
        tempy = self.rect.centery
        self.rect = self.image.get_rect()
        self.rect.centerx = tempx
        self.rect.centery = tempy
        self.mask = pygame.mask.from_surface(self.image)
        self.unshrink_timer = 3 * 30

    def unshrink(self):
        '''function that unshrinks your character'''
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (128, 128))
        tempx = self.rect.centerx
        tempy = self.rect.centery
        self.rect = self.image.get_rect()
        self.rect.centerx = tempx
        self.rect.centery = tempy
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        '''update player object method'''
        # check for wall collision
        if(self.rect.left < 0):
            self.rect.left = 0
        if(self.rect.right > self.screen.get_width()):
            self.rect.right = self.screen.get_width()
        if(self.rect.top < 0):
            self.rect.top = 0
        if(self.rect.bottom > self.screen.get_height() - self.offset):
            self.rect.bottom = self.screen.get_height() - self.offset

        # flicker effect when hit
        if(self.flash != 0):
            self.image.set_alpha(self.flashframes[self.flash-1])
            self.flash -= 1
        # check for shrinking
        if(self.unshrink_timer == 0):
            self.unshrink()
        if self.unshrink_timer >= 0:
            self.unshrink_timer -= 1

