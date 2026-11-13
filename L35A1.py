import math
import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set.mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('C:\Users\Admin\Downloads\5de8c751f589755d53f416625a89237d.png')

pygame.display.set_caption = ("Space Invader")
icon = pygame.image.load('C:\Users\Admin\Downloads\images (1).jpg')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('C:\Users\Admin\Downloads\rocket.webp')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('C:\Users\Admin\Downloads\alien png.jpg'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
        enemyX.
