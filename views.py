import sys
import pygame
from models import Labyrinthe, MacGyver
from variables import *

pygame.init()
screen = pygame.display.set_mode((15*sp_size, 15*sp_size))


def game():

	currentgame = True

	# event management and display game elements
	Lab = Labyrinthe(lab, sp_size)
	Lab.init_lab()
	macgyver = MacGyver(lab, sp_size)

	while currentgame:

		screen.blit(macgyver.image, (macgyver.rect.x, macgyver.rect.y))
				
		for event in pygame.event.get(): #pygame.event.get() : event list keyboard and mouse
			if event.type == pygame.QUIT:
				sys.exit() # method  allows close window, exit game
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					macgyver.move_right()
				elif event.key == pygame.K_LEFT:
					macgyver.move_left()
				elif event.key == pygame.K_UP:
					macgyver.move_up()
				elif event.key == pygame.K_DOWN:
					macgyver.move_down()
				Lab.init_lab()
		pygame.display.flip() #update window endlessly as long as currentgame is True




game()



