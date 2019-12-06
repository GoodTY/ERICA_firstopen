import pygame

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512 
WHITE = (255, 255, 255)

def Basket(x,y):
	global screen, basket
	screen.blit(basket , (x,y))

def Play_Game():
	global screen, clock, basket

	x = SCREEN_WIDTH * 0.5
	y = SCREEN_HEIGHT * 0.05
	x_change = 0
	# start position, only move x

	crashed = False
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
		x += x_change

		screen.fill(WHITE)
		pygame.display.update()
		clock.tick(60)
		basket(x,y)
	pygame.quit()	

def Start_Game():
	global screen , clock, basket

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Catching')
	basket = pygame.image.load('basket.png')

	clock = pygame.time.Clock()
	Play_Game()

Start_Game()
