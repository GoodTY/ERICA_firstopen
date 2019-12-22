import pygame
import random
import math

pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#background Image
background = pygame.image.load('background.png')

# Title and Icon
pygame.display.set_caption("Catching Bananas")
icon = pygame.image.load('monkey.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('basket.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('banana.png')
enemyX = random.randint(0, 800) 
enemyY = 0
enemyY_change = 5


def player(x,y):
	screen.blit(playerImg, (x, y))

def enemy(x, y):
	screen.blit(enemyImg, (x, y))

def isCollision(enemyX, enemyY, playerX, playerY):
	distance = math.sqrt((math.pow(enemyX-playerX,2)) + (math.pow(enemyY - playerY,2)))
	
	if distance < 27:
		return True
	else:
		return False

# Game Loop
running = True
while running:
	# 빨강 초록 파랑
	screen.fill((0,0,0))
	screen.blit(background, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		# if keastroke is pressed check whether its right or left
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				playerX_change = 10
			if event.key == pygame.K_LEFT:
				playerX_change = -10
		if event.type == pygame.KEYUP:
			if event.type == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

	# Player Movement
	playerX += playerX_change

	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736

	# Enemy Movement
	enemyY += enemyY_change

	if enemyY >= 736:
		enemyY_change = -0.3
		enemyY += enemyY_change

	# Collision
	collision = isCollision(enemyX, enemyY, playerX, playerY)
	if collision:
		print(score)
		enemyX = random.randint(0, 735)
		enemyY = 0

	player(playerX, playerY)
	enemy(enemyX, enemyY)

	pygame.display.update()
