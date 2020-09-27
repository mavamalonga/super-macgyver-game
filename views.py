import sys
import pygame
from random import *
from models import Labyrinthe, MacGyver
from models import Gardien, Objets
from variables import *
from controler import *


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((15*sp_size, 15*sp_size))


def game():

	currentgame = True

	# call every class of model file 
	Lab = Labyrinthe(lab, sp_size)
	Lab.init_lab()
	objets = Objets(lab, sp_size)
	macgyver = MacGyver(lab, sp_size, objets)
	gardien = Gardien(sp_size)
	yellow =(255, 255, 0)
	count_score = pygame.font.SysFont('monospace', 15)
	pygame.display.flip()
	
	
	
	while currentgame:

		#display all sprite of the game 
		
		objets.display_objets()
		screen.blit(gardien.image, (gardien.rect.x, gardien.rect.y))
		screen.blit(macgyver.image, (macgyver.rect.x, macgyver.rect.y))
		score = macgyver.pick_up


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

				Lab.init_lab()
				

			


				if gardien.rect.x == macgyver.rect.x and gardien.rect.y == macgyver.rect.y :
					if macgyver.pick_up == 3:
						screen.blit(pygame.image.load('ressource/screen_win.png'), (0*sp_size, 0*sp_size))
					else:
						screen.blit(pygame.image.load('ressource/screen_gameover.png'), (0*sp_size, 0*sp_size))

		text = count_score.render("objets:" + str(score) + "/3", 50, yellow, (0, 0, 0))
		screen.blit(text, ((645-70)/2, 20))
		pygame.display.flip() #update window endlessly as long as currentgame is True
		



if __name__ == '__main__':
	game()



