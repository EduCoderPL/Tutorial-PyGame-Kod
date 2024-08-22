import pygame
from pygame.locals import *
from constants import *
import random

class Enemy:
    def __init__(self, x, y, width, height, color=(100, 100, 100)):
        self.x = x
        self.y = y
        self.xVel = 0
        self.yVel = 0

        self.width = width
        self.height = height
        self.xAcc = random.uniform(-1, 1)
        self.yAcc = random.uniform(-1, 1)

        self.color = color

        self.rect = Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.xVel += self.xAcc
        self.yVel += self.yAcc

        self.yVel += 0.1

        self.xVel *= 0.98
        self.yVel *= 0.98

        self.x += self.xVel
        self.y += self.yVel

        if self.x < 0:
            self.x = 0
            self.xVel *= -1
            self.xAcc = random.uniform(-1, 1)
            self.yAcc = random.uniform(-1, 1)

        if self.y < 0:
            self.y = 0
            self.yVel *= -1
            self.xAcc = random.uniform(-1, 1)
            self.yAcc = random.uniform(-1, 1)

        if self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width
            self.xVel *= -1
            self.xAcc = random.uniform(-1, 1)
            self.yAcc = random.uniform(-1, 1)

        if self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            self.yVel *= -1
            self.xAcc = random.uniform(-1, 1)
            self.yAcc = random.uniform(-1, 1)

        self.rect = Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            self.rect
        )