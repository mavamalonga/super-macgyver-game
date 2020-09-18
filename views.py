import sys
import pygame
from models import Labyrinthe
from variables import *

pygame.init()


def game():

	currentgame = True

	# event management and display game elements
	while currentgame:
		Lab = Labyrinthe(lab, sp_size)
		Lab.init_lab()
		pygame.display.flip()

		for event in pygame.event.get(): #pygame.event.get() : event list keyboard and mouse
			if event.type == pygame.QUIT:
				sys.exit() # method  allows close window, exit game

		pygame.display.flip()

"""
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT and macgyver.rect.x < 470:
					macgyver.move_right()
				elif event.key == pygame.K_LEFT and macgyver.rect.x > 0:
					macgyver.move_left()
				elif event.key == pygame.K_UP and macgyver.rect.y > 0:
					macgyver.move_up()
				elif event.key == pygame.K_DOWN and macgyver.rect.y < 260:
					macgyver.move_down()
			pygame.display.flip() #update window endlessly as long as currentgame is True
"""



game()



