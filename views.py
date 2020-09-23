import sys
import pygame
from random import *
from models import Labyrinthe, MacGyver
from models import Gardien, Objets
from variables import *

pygame.init()
screen = pygame.display.set_mode((15*sp_size, 15*sp_size))


def game():

	currentgame = True

	# call every class of model file 
	Lab = Labyrinthe(lab, sp_size)
	Lab.init_lab()
	macgyver = MacGyver(lab, sp_size)
	gardien = Gardien(sp_size)
	ether1 = Objets(lab, sp_size, ether)
	tube_plastique1 = Objets(lab, sp_size, tube_plastique)
	seringue1 = Objets(lab, sp_size, seringue)
	pygame.display.flip()
	
	

	while currentgame:

		#display all sprite of the game 
		screen.blit(gardien.image, (gardien.rect.x, gardien.rect.y))
		screen.blit(macgyver.image, (macgyver.rect.x, macgyver.rect.y))
		screen.blit(ether1.image, (ether1.pos))
		screen.blit(tube_plastique1.image, (tube_plastique1.pos))
		screen.blit(seringue1.image, (seringue1.pos))

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
				# victory condition
				if gardien.rect.x == macgyver.rect.x and gardien.rect.y == macgyver.rect.y :
					screen.blit(pygame.image.load('ressource/screen_win.png'), (0*sp_size, 0*sp_size))

		pygame.display.flip() #update window endlessly as long as currentgame is True




game()



