'''
Author: Richard Zhang

Date: XX June 2022

Description:
The Boss sprite for the bullet hell game I create
'''

import pygame
import random
import Projectile

class Boss(pygame.sprite.Sprite):
    '''class that simulates a boss'''
    def coin_flip(self):
        '''random number generator that generates either 1 or -1'''
        if(random.randint(0,1)):
            return 1
        return -1

    def __init__(self, screen):
        '''initializer for boss object'''
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.offset = 150
        self.image = pygame.image.load("boss.jpg")
        self.image = pygame.transform.scale(self.image, (256, 192))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_width() // 2
        self.rect.centery = 50
        self.randomcounter = 30*5
        self.speed = 3
        self.dx = random.randint(int(self.speed * 0.8), self.speed) * self.coin_flip()
        self.dy = random.randint(int(self.speed * 0.8), self.speed) * self.coin_flip()
        self.buffer = 0
        self.bullets = 4
        self.mask = pygame.mask.from_surface(self.image)

    def increaseSpeed(self):
        '''increases the self.speed variable by a factor of 1.5'''
        self.speed *= 1.5
        self.speed = int(self.speed)
        if(self.speed > 30):
            self.speed = 30
        self.bullets *= 2
        if(self.bullets == 32):
            self.bullets = 32

    def spawnProjectiles(self):
        '''creates a projectiles list in a circular shape and returns it'''
        randbullets = self.bullets
        startingangle = random.randint(0, 360 // randbullets - 1)
        obj_arr = []
        for i in range(randbullets):
            obj_arr.append(Projectile.Projectile(self.screen, startingangle + i*(360/randbullets), \
            self.speed ** 0.5, (self.rect.centerx, self.rect.centery)))
        print()
        return obj_arr

    def update(self):
        '''update boss object method'''
        if self.buffer > 0:
            self.buffer -= 1
        else:
            self.rect.centerx += self.dx
            self.rect.centery += self.dy
            self.randomcounter -= 1
            if(self.randomcounter == 0):
                self.randomcounter = 30*5
                self.dx = random.randint(-self.speed, self.speed)
                self.dy = random.randint(-self.speed, self.speed)
                self.buffer = 30 * 1
            if(self.rect.left < 0):
                self.rect.left = 0
                self.dx = -self.dx
            if(self.rect.right > self.screen.get_width()):
                self.rect.right = self.screen.get_width()
                self.dx = -self.dx
            if(self.rect.top < self.offset):
                self.rect.top = 0
                self.dy = -self.dy
            if(self.rect.bottom > self.screen.get_height() - self.offset):
                self.rect.bottom = self.screen.get_height() - self.offset
                self.dy = -self.dy

