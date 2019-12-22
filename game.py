import pygame
import random
import math
from pygame import mixer
from time import sleep

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
num_of_bananas = random.randint(2,3)
bananaImg = []
bananaX = []
bananaY = []
bananaY_change = []
for i in range(num_of_bananas):
	bananaImg.append(pygame.image.load('banana.png'))
	bananaX.append(random.randint(0, 736)) 
	bananaY.append(random.randint(0,70))
	bananaY_change.append(0)

# bomb
bombImg = pygame.image.load('bomb.png')
bombX = random.randint(0, 736)
bombY = 0
bombX_change = 0
bombY_change = -2

def bomb(x, y):
	screen.blit(bombImg, (x, y))

def player(x, y):
	screen.blit(playerImg, (x, y))

def banana(x, y, i):
	screen.blit(bananaImg[i], (x, y))

def isCollision1(bananaX, bananaY, playerX, playerY):
	distance = math.sqrt((math.pow(bananaX-playerX,2)) + (math.pow(bananaY - playerY,2)))
	
	if distance < 27:
		return True
	else:
		return False

def isCollision2(bombX, bombY, playerX, playerY):
	distance = math.sqrt((math.pow(bombX-playerX,2)) + (math.pow(bombY - playerY,2)))
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
	fps_clock = pygame.time.Clock()
	FPS = 60
	fps_clock.tick(FPS)

	# 빨강 초록 파랑
	screen.fill((0,0,0))
	screen.blit(background, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		# if keastroke is pressed check whether its right or left
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				playerX_change = 25
			if event.key == pygame.K_LEFT:
				playerX_change = -25
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				playerX_change = 0
			elif event.key == pygame.K_LEFT:
				playerX_change = 0

	# bomb Movement

	bombY_change = 4
	bombY += bombY_change

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
				bombY = 2000
			game_over_text()
			break

		if bananaY[i] <= 600:
			bananaY_change[i] = random.randint(1,6)
			bananaY[i] += bananaY_change[i]
	
		# Collision  banana player
		collision1 = isCollision1(bananaX[i], bananaY[i], playerX, playerY)
		if collision1:
			bananaX[i] = random.randint(0, 736)
			bananaY[i] = random.randint(0, 100)
			score_value += 1
		banana(bananaX[i], bananaY[i], i)

		# Collision bomb player
		collision2 = isCollision2(bombX, bombY, playerX, playerY)
		if collision2:
			for j in range(num_of_bananas):
				bananaY[j] = 2000
				bombY = 2000
			game_over_text()

		#not collision bomb
		if bombY > 600:
			bombY_change = 4
			bombX = random.randint(0, 736)
			bombY = 0
			bombY += bombY_change
		bomb(bombX, bombY)

	player(playerX, playerY)
	bomb(bombX, bombY)
	show_score(textX, textY)
	pygame.display.update()
