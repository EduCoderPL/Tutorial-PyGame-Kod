# Import biblioteki PyGame
import pygame
from pygame.locals import *
from constants import *
import random
import time

from player import Player
from enemy import Enemy
from text import Text

pygame.init()

DEFAULT_FONT = pygame.font.SysFont("arial", 48)
BIG_FONT = pygame.font.SysFont("arial", 144)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# GRACZ
player = Player(200, 100, 100, 100)

# ENEMY
enemies = []

for i in range(1000):
    x = random.randint(100, SCREEN_WIDTH - 200)
    y = random.randint(100, SCREEN_HEIGHT - 200)

    width = random.randint(50, 200)
    height = random.randint(50, 200)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    enemies.append(Enemy(x, y, width, height, color))

score = 0
startTime = time.time()

textScore = Text(f"Score: {score}", (150, 50), DEFAULT_FONT)

textTime = Text(f"Time: {(time.time() - startTime)}", (1700, 50), DEFAULT_FONT)
textYouWon = Text("YOU WON", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), BIG_FONT)

run = True
while run:

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()

    # PLAYER
    if keys[K_d]:
        player.xVel += player.acceleration
    if keys[K_a]:
        player.xVel -= player.acceleration
    if keys[K_w]:
        player.yVel -= player.acceleration
    if keys[K_s]:
        player.yVel += player.acceleration

    player.update()

    # ENEMY
    for enemy in enemies:
        enemy.update()

        if player.rect.colliderect(enemy.rect):
            enemies.remove(enemy)
            score += 1

    screen.fill(COLOR_BLACK)

    for enemy in enemies:
        enemy.draw(screen)

    player.draw(screen)

    textScore.draw(screen, f"Score: {score}")

    if len(enemies) <= 0:
        textTime.draw(screen)
        textYouWon.draw(screen)
    else:
        textTime.draw(screen, f"Time: {(time.time() - startTime):.2f}")


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()