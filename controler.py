import sys
from views import game
from pygame import *


def victory():
	screen.blit(pygame.image.load('ressource/screen_win.png'), (0*sp_size, 0*sp_size))
	for event in pygame.event.get():
		if event.type == pygame.K_e:
			sys.exit()
		elif event.type == pygame.K_SPACE:
				initialisation()

def initialisation():
	game()