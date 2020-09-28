
import sys
import pygame
from random import *
from models import Labyrinth, MacGyver
from models import Guardian, Objects
from variables import *

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((15*sp_size, 15*sp_size))


def game():

	current_game = True

	# call every class of model file 
	Lab = Labyrinth(lab, sp_size)
	Lab.build_lab()
	objects = Objects(lab, sp_size)
	macgyver = MacGyver(lab, sp_size, objects)
	guardian = Guardian(sp_size)
	yellow =(255, 255, 0)
	text = pygame.font.SysFont('impact', 20)
	pygame.display.flip()
	
	
	
	while current_game:

		#display all sprite of the game 
		
		objects.display_objets()
		screen.blit(guardian.image, (guardian.rect.x, guardian.rect.y))
		screen.blit(macgyver.image, (macgyver.rect.x, macgyver.rect.y))
		pick_up = macgyver.pick_up


		for event in pygame.event.get():
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
				macgyver.get_objets()

				Lab.build_lab()
				

			


				if macgyver.rect.x == guardian.rect.x and macgyver.rect.y == guardian.rect.y:
					if macgyver.pick_up == 3:
						screen.blit(pygame.image.load('ressource/you_win.png'), (2*sp_size, 5*sp_size))
						macgyver.not_arrived = False
					else:
						screen.blit(pygame.image.load('ressource/game_over.png'), (1*2*sp_size, 5*sp_size))
						macgyver.not_arrived = False

		counter_pickup_objets = text.render("backpack: " + str(pick_up) + "/3", 50, yellow, (0, 0, 0))
		screen.blit(counter_pickup_objets, (260, 10))
		pygame.display.flip() #update window endlessly as long as currentgame is True
		



if __name__ == '__main__':
	game()