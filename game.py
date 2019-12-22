import pygame
import random
import math
from pygame import mixer

pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#background Image
background = pygame.image.load('background.png')

# Title and Icon
pygame.display.set_caption("Catching Bananas")
icon = pygame.image.load('monkey.png')
pygame.display.set_icon(icon)

# Font
score_value = 0
font = pygame.font.Font('OpenSans-Regular.ttf',32)

textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('OpenSans-Regular.ttf', 64)

# Background Sound
mixer.music.load('bgm.mp3')
mixer.music.play(-1)

# Player
playerImg = pygame.image.load('basket.png')
playerX = 370
playerY = 480
playerX_change = 0

# Banana
bananaImg = []
bananaX = []
bananaY = []
bananaY_change = []
num_of_bananas = random.randint(2,5)

for i in range(num_of_bananas):
	bananaImg.append(pygame.image.load('banana.png'))
	bananaX.append(random.randint(0, 736)) 
	bananaY.append(random.randint(0,20))
	bananaY_change.append(5)


def player(x, y):
	screen.blit(playerImg, (x, y))

def banana(x, y, i):
	screen.blit(bananaImg[i], (x, y))

def isCollision(bananaX, bananaY, playerX, playerY):
	distance = math.sqrt((math.pow(bananaX-playerX,2)) + (math.pow(bananaY - playerY,2)))
	
	if distance < 27:
		return True
	else:
		return False

def show_score(x, y):
	score = font.render(' Score : ' + str(score_value), True, (255,255,255))
	screen.blit(score, (x, y))

def game_over_text():
	over_text = over_font.render( "GAME OVER", True, (255,255,255))
	screen.blit(over_text, (200, 255))


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
				playerX_change = 15
			if event.key == pygame.K_LEFT:
				playerX_change = -15
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
	for i in range(num_of_bananas):
		
	#Game over
		if bananaY[i] > 600:
			for j in range(num_of_bananas):
				bananaY[j] = 2000
			game_over_text()
			break

		if bananaY[i] <= 600:
			bananaY_change[i] = random.randint(1, 5)
			bananaY[i] += bananaY_change[i]

		# Collision
		collision = isCollision(bananaX[i], bananaY[i], playerX, playerY)
		if collision:
			bananaX[i] = random.randint(0, 735)
			bananaY[i] = 0
			score_value += 1
		banana(bananaX[i], bananaY[i], i)


	player(playerX, playerY)
	show_score(textX, textY)
	pygame.display.update()
