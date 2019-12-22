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

# Score
score_value = 0
font = pygame.font.Font('OpenSans-Regular.ttf',32)

textX = 10
textY = 10

def show_score(x, y):
	score = font.render("Score :" + str(score_value),True, (255,255,255))
	screen.blit(score, (x, y))
# Player
playerImg = pygame.image.load('basket.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
	enemyImg.append(pygame.image.load('banana.png'))
	enemyX.append(random.randint(0, 800)) 
	enemyY.append(0)
	enemyY_change.append(5)


def player(x,y):
	screen.blit(playerImg, (x, y))

def enemy(x, y, i):
	screen.blit(enemyImg[i], (x, y))

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
			if event.key == pygame.K_RIGHT:
				playerX_change = 0
			elif event.key == pygame.K_LEFT:
				playerX_change = 0
	# Player Movement
	playerX += playerX_change

	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736

	# Enemy Movement
	for i in range(num_of_enemies):
		if enemyY[i] <= 736:
			enemyY_change[i] = 1
			enemyY[i] += enemyY_change[i]
		# Collision
		collision = isCollision(enemyX[i], enemyY[i], playerX, playerY)
		if collision:
			enemyX[i] = random.randint(0, 735)
			enemyY[i] = 0
			score += 1
		enemy(enemyX[i], enemyY[i], i)



	player(playerX, playerY)
	show_score(textX, textY)
	pygame.display.update()
