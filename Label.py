'''
Author: Richard Zhang

Date: XX June 2022

Description:
The scorecounter sprite for the bullet hell game I create
'''

import pygame
import random

class Label(pygame.sprite.Sprite):
    '''An mutatable text Label Sprite subclass'''
    def __init__(self, message, x_y_pos, mode):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("curlz", 36)
        self.text = str(message)
        self.counter = int(message)
        self.pos = x_y_pos
        self.mode = mode
     	
    def setText(self, message):
        '''Mutator for text to be displayed on the label.'''
        if(self.mode):
            if(len(message) < 5):
                self.text = "SCORE: " + "0"*(5-len(message)) + message
            else:
                self.text = "SCORE: " + message
        else:
            if(len(message) < 5):
                self.text = "HISCORE: " + "0"*(5-len(message)) + message
            else:
                self.text = "HISCORE: " + message

    def setCounter(self, counter):
        '''mutator for counter variable'''
        self.counter = counter

    def increase_counter(self, increment):
        '''increments the counter by a certain amount'''
        self.counter += increment

    def getScore(self):
        '''accessor for counter variable (score)'''
        return self.counter

    def changePos(self, pos):
        '''changes the position of the label'''
        self.pos = pos

    def changeSize(self, size):
        '''changes the text font size of the label'''
        self.font = pygame.font.SysFont("curlz", size)

    def hardSetText(self, text):
        '''hard changes the text to a message'''
        self.text = text
        self.image = self.font.render(self.text, 1, (255, 255, 255))

    def update(self):
        '''Render and center the label text on each Refresh.'''
        self.setText(str(self.counter))
        self.image = self.font.render(self.text, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.top = self.pos[0]
        self.rect.left = self.pos[1]
