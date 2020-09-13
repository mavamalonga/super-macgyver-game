import pygame 
import sys
from models import MacGyver, Labyrinthe

pygame.init()

class Game:

	#SIZE(500, 500) #screen size

	def __init__(self):
		self.screen = pygame.display.set_mode((500,500)) #window creation
		pygame.display.set_caption('MACGYVER GAME EDITION ALPHA') #title of window
		self.currentgame = True

	def main_function(self):

		macgyver = MacGyver()
		labyrinthe = Labyrinthe(0, 10)

		# event management and display game elements
		while self.currentgame:

			self.screen.blit(macgyver.image, macgyver.rect)


			for event in pygame.event.get(): #pygame.event.get() : event list keyboard and mouse
				if event.type == pygame.QUIT:
					sys.exit() # method  allows close window, exit game

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

			labyrinthe.initialize_zones.draw(self.screen.blit)


def main():
	game = Game()
	game.main_function()

	

main()
