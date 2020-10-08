
import sys
import pygame
from random import *
from models import Labyrinth, MacGyver
from models import Guardian, Objects
from variables import *

pygame.init()
pygame.font.init()


#function checks the win or defeat condition
def arbitror(macgyver, guardian):
	if macgyver.rect.x == guardian.rect.x and macgyver.rect.y == guardian.rect.y:  
		if macgyver.pick_up == 3:
			screen.blit(pygame.image.load('ressource/you_win.png'), (2*sp_size, 5*sp_size))
			macgyver.not_arrived = False
		else:
			screen.blit(pygame.image.load('ressource/game_over.png'), (1*2*sp_size, 5*sp_size))
			macgyver.not_arrived = False


"""
def main():
call the classes
manage keyboard events
call game function
"""
def main():  


	screen = pygame.display.set_mode((15*sp_size, 15*sp_size))
	Lab = Labyrinth("mappy.txt", sp_size)
	Lab.build_lab()  
	objects = Objects("mappy.txt", sp_size)
	macgyver = MacGyver("mappy.txt", sp_size, objects)
	guardian = Guardian(sp_size)
	pygame.display.flip()

	current_game = True

	while current_game:
		


		for event in pygame.event.get(): # the for loop will activate at each event, keyboard, mouse	
			if event.type == pygame.QUIT: # event.type returns the event, activated
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
				arbitror(macgyver, guardian)


		objects.display_objects()
		screen.blit(guardian.image, (guardian.rect.x, guardian.rect.y))
		screen.blit(macgyver.image, (macgyver.rect.x, macgyver.rect.y))
		macgyver.score_count()
		pygame.display.flip()



if __name__ == '__main__':
	main()