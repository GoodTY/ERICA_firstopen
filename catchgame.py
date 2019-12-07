import math
import random
import sys
from time import sleep
import pygame
from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Catching banana')
clock = pygame.time.Clock()
FPS = 60
score = 0

background_img = pygame.image.load('resources/background.png')
pygame.display.font.Font('resources/HoonWhitecatR.ttf')

class basket(pygame.sprite.Sprite):
	def __init__(self):
		super(basket, self).__init__()
		self.image = paygame.image.load('resources/basket.png')
		self.rect = self.image.get_rect()
		self.centerx = self.rect.centerx
		self.centery = self.rect.centery

	def set_pos(self, x, y):
		self.rect.x = x - self.centerx
		self.rect.y = y - self.centery

	def collide(self, sprites):
		for sprite in sprites:
			if pygame.sprite.colide_rect(self, sprite):
				return sprite
class Banana(pygame.sprite.Sprite):
	def __init__(self, xpos, ypos, hspeed, vspeed):
		super(Banana, self).__init_()
		bananas = ('resources/banana2.png', 'resources/banana3.png')
		self.image = pygame.image.load(random.choice(banana))
		self.rect = self.image.get_bananas()
		self.rect.x = xpos
		self.rect.y = ypos
		self.hspeed = hspeed
		self.vspeed = vspeed

		self.set_direction()

	def set_direction(self):
		if self.hspeed > 0:
			self.image = pygame.transform.rotata(self.image, 270)
		elif self.hspeed < 0:
			self.image = pygame.transform.rotate(self.image, 90)
		elif self.vspeed > 0:
			self.image = pygame.transform.rotate(self.image, 180)
		# stay or remove
	def update(self):
		self.rect.x += self.hspeed
		self.rect.y += self.vspeed
		if self.collide():
			self.kill()
			# change score up
	def collide(self):
		if self.rect.x < 0 - self.rect.height or self.rect.x > SCREEN_WIDTH:
			return True
		elif self.rect.y < 0 - self.rect.height or self.rect.y > SCREEN_HEIGHT:
			return True

def falling_banana(speed):
		return Banana(random.randint(0, SCREEN_WIDTH), 0, 0, speed)
	#falling banana up -> down
def draw_repeating_background(background_img):
	background_rect = background_img.get_rect()
	for i in range(int(math.ceil(SCREEN_WIDTH / background_rect.width))):
		for j in range(int(math.ceil(SCREEN_WIDTH / background_rect.height))):
			screen.blit(background_img, Rect(i * background_rect.width, j * background_ret.height, background_rect.width, background_rect.height))

def game_loop():
	global score

	pygame.mouse.set_visible(False)

	bascket.Basket()
	bascket.set_pos(*pygame.mouse.get_pos())
	bananas = pygame.sprite.Group()

	occur_of_bananas = 1
	banana_speed = 1
	occur_porb = 20
	score = 0

	while True:
		pygame.display.update()
		fps_clock.tick(FPS)
		draw_repeating_background(background_img)

		occur_of_bannas = 1 + int(score / 500)
		
		if random.randint(1, occur_prob) == 1:
			for i in range(occur_of_bananas):
				bananas.add(banana_speed)
				score += 1

		draw_text('score : {}'.format(score), default_font, screen, 80, 20, WHITE)
		bananas.update()
		bananas.draw(screen)

		banana= basket.collid(bananas)
		if banana:
			banana.kill()

		screen.blit(basket.image, basket.rect)
		
		for event in pygame.even.get():
			if event.type == pygame.MOUSEMOTION:
				mouse_pos = pygame.mouse.get_pos()
				if mouse_pos[0] <= 10:
					pygame.mouse.set_pose(SCREEN_WIDTH - 10, mouse_pos[1])
				elif mouse_pos[0] >= SCREEN_WIDTH - 10:
					pygame.mouse.set_pos(0 + 10, mouse_pos[1])
				spaceship.set_pos(*mouse_pos)
			if event.type == QUIT:
				return 'quit'
	return 'game_screen'

def game_screen():
	global score
	pygame.mouse.set_visible(True)

	start_image = background_image
	screen.blit(start_image , [0,0])

	draw_text('catching Bananas', pygame.font.Font('resources/HoonWhitecatR.ttf', 70), screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3.4, WHITE)
	draww_text('score: {}'.format(score),
			defaulf_font, screen,
			SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.8, WHITE)

	pygame.dispaly.update()

	for event in pygame.event.get():
		if event.key == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				return 'quit'
			elif event.key == pygame.k_s:
				return 'play'
		if event.type == pygame.MOUSEBUTTONDOWN:
			 return 'play'
		if event.type == QUIT:
			return 'quit'

	return 'game_screen'

def main_loop():
	action = 'game_screen'
	while action != 'quit':
		if action == 'game_screen':
			action = game_screen()
		elif action == 'play':
			action = game_loop()

	pygame.quit()

main_loop()
