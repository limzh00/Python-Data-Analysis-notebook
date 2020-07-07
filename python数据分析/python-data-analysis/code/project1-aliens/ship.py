import pygame as pg 
import numpy as np
import math

#################### DO NOT MODIFY THESE ###################
class Ship():
    def __init__(self, screen):
        '''Initialize a ship and set its initial position.'''
        self.screen = screen
        self.image = pg.image.load('img/ship1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''Draw self.ship at the position'''
        self.screen.blit(self.image, self.rect)

