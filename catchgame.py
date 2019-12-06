import pygame
import time

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512 
WHITE = (255, 255, 255)

def Start_Game():
	global screen , clock
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.dispaly.setcaption('Catching')
	clock = pygame.time.Clock()
	Playing_Game()
