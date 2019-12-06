import pygame

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512 
WHITE = (255, 255, 255)

def Play_Game():
	global screen, clock

	crashed = False
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed =True

		screen.fill(WHITE)
		pygame.display.update()
		clock.tick(60)
	pygame.quit()	

def Start_Game():
	global screen , clock
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Catching')
	clock = pygame.time.Clock()
	Play_Game()
def main():
	Start_Game()

main()
