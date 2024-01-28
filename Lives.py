'''
Author: Richard Zhang

Date: XX June 2022

Description:
The lives sprite for the bullet hell game I create
'''

import pygame
import random

class Lives(pygame.sprite.Sprite):
    '''An mutatable text Label Sprite subclass'''
    def __init__(self, message, x_y_pos):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("curlz", 64)
        self.text = str(message)
        self.counter = int(message)
        self.pos = x_y_pos
     	
    def setText(self, message):
        '''Mutator for text to be displayed on the label.'''
        self.text = "Lives: " + str(message)

    def decrease_counter(self):
        '''decrements the counter by 1'''
        self.counter -= 1

    def update(self):
        '''Render and center the label text on each Refresh.'''
        self.setText(str(self.counter))
        self.image = self.font.render(self.text, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.top = self.pos[0]
        self.rect.left = self.pos[1]
