
import sys
import pygame
from random import *
from models import Labyrinth, MacGyver
from models import Guardian, Objects
from variables import *

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((15*sp_size, 15*sp_size))

"""
def game():
run the program
call the classes
manage keyboard events
defines the conditions of victory and defeat
"""
def game():  

	current_game = True
	Lab = Labyrinth("mappy.txt", sp_size)  
	Lab.build_lab()     # On execute l'arriere plan du jeu, le labirynth
	objects = Objects("mappy.txt", sp_size)
	macgyver = MacGyver("mappy.txt", sp_size, objects)
	guardian = Guardian(sp_size)
	yellow =(255, 255, 0)
	text = pygame.font.SysFont('impact', 20)
	pygame.display.flip()
	
	
	while current_game:    #maintain the display of the window
		"""
		the game loop, as long as current_game is true
		le code contenu dans cette fenetre va s'executer en boucle
		"""

		#display all sprite of the game 
		
		objects.display_objects()
		screen.blit(guardian.image, (guardian.rect.x, guardian.rect.y))
		screen.blit(macgyver.image, (macgyver.rect.x, macgyver.rect.y))
		pick_up = macgyver.pick_up


		for event in pygame.event.get(): # la boucle for va s'activer a chaque evenement, clavier, souris	
			if event.type == pygame.QUIT: # event.type renvoie l'evenement, actionné 
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					macgyver.move_right()
				elif event.key == pygame.K_LEFT:
					macgyver.move_left()
				elif event.key == pygame.K_UP:
					macgyver.move_up()
				elif event.key == pygame.K_DOWN:
					macgyver.move_down()
				macgyver.get_objects()

				Lab.build_lab()
				


				#gestion de condition de victoire et de défaite
				if macgyver.rect.x == guardian.rect.x and macgyver.rect.y == guardian.rect.y:  
					if macgyver.pick_up == 3:
						screen.blit(pygame.image.load('ressource/you_win.png'), (2*sp_size, 5*sp_size))
						macgyver.not_arrived = False
					else:
						screen.blit(pygame.image.load('ressource/game_over.png'), (1*2*sp_size, 5*sp_size))
						macgyver.not_arrived = False

		#recuperer la variable pick_up le convertir en str et l'afficher
		counter_pickup_objets = text.render("backpack: " + str(pick_up) + "/3", 50, yellow, (0, 0, 0))
		screen.blit(counter_pickup_objets, (260, 10))
		pygame.display.flip()
		



if __name__ == '__main__':
	game()