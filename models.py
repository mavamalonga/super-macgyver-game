import pygame
import sys
from variables import * #all variables from this file
pygame.init()
		

class Labyrinthe():
	def __init__(self, base, sp_size):
		pygame.init()
		self.base_lab = base
		self.screen = pygame.display.set_mode((15*sp_size, 15*sp_size))

	def init_lab(self):
		self.structures = []
		for ln in self.base_lab:
			line_level = list(ln)
			self.structures.append(line_level)

		for x, col in enumerate(self.structures):
			for y, case in enumerate(col):
				pos_x = x*sp_size
				pos_y = y*sp_size
				if case == "m":
					self.screen.blit(pygame.image.load("ressource/MacGyver.png"), (pos_x, pos_y))
				elif case == "g":
					self.screen.blit(pygame.image.load("ressource/Gardien.png"), (pos_x, pos_y))
				elif case == "s":
					self.screen.blit(pygame.image.load("ressource/structures.png"), (pos_x, pos_y))


		pygame.display.flip()



