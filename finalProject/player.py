import pygame
from pygame.locals import *
from constants import *

class Player:

    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.xVel = 0
        self.yVel = 0

        self.width = width
        self.height = height
        self.acceleration = 1

        self.rect = Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.yVel += 0.1

        self.xVel *= 0.98
        self.yVel *= 0.98

        self.x += self.xVel
        self.y += self.yVel

        if self.x < 0:
            self.x = 0
            self.xVel *= -1

        if self.y < 0:
            self.y = 0
            self.yVel = 0

        if self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width
            self.xVel *= -1

        if self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            self.yVel = 0

        self.rect = Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            COLOR_RED,
            self.rect
        )
