import pygame
import sys
from random import *
from variables import * #all variables from this file
pygame.init()
		

class Labyrinthe:
	def __init__(self, base, sp_size):
		pygame.init()
		self.base_lab = base
		self.screen = pygame.display.set_mode((15*sp_size, 15*sp_size))

	def init_lab(self):
		self.structures = []
		for ln in self.base_lab:
			line = list(ln)
			self.structures.append(line)

		for x, col in enumerate(self.structures):
			for y, case in enumerate(col):
				pos_x = x*sp_size
				pos_y = y*sp_size

				if case == "s":
					self.screen.blit(pygame.image.load("ressource/stones.png"), (pos_x, pos_y))
				elif case == "v":
					self.screen.blit(pygame.image.load("ressource/black_bloc.png"), (pos_x, pos_y))
				elif case == "d":
					self.screen.blit(pygame.image.load("ressource/decorations3.png"),(pos_x, pos_y))
				elif case == "l":
					self.screen.blit(pygame.image.load("ressource/decorations4.png"),(pos_x, pos_y))
				elif case == "e":
					self.screen.blit(pygame.image.load("ressource/exit.png"),(pos_x, pos_y))
				elif case == "k":
					self.screen.blit(pygame.image.load("ressource/skull.png"),(pos_x, pos_y))



class MacGyver(pygame.sprite.Sprite):
	def __init__(self, base, sp_size):
		super().__init__()
		self.base_lab = base
		self.image = pygame.image.load("ressource/MacGyver.png")
		self.rect = self.image.get_rect()
		self.x = 13                                 #coordonnées index détachés de sp_size
		self.y = 7
		self.rect.x = self.x*sp_size
		self.rect.y = self.y*sp_size
		self.pick_up = 0

	
	def move_left(self):
		self.structures = []
		for ln in self.base_lab:
			line = list(ln)
			self.structures.append(line)

		if self.structures[self.x - 1][self.y] == "v":
			self.x = self.x - 1
			self.rect.x = self.rect.x - sp_size
			self.rect.y = self.rect.y 
		
	def move_right(self):
		self.structures = []
		for ln in self.base_lab:
			line = list(ln)
			self.structures.append(line)

		if self.structures[self.x + 1][self.y] == "v":
			self.x = self.x + 1
			self.rect.x = self.rect.x + sp_size
			self.rect.y = self.rect.y 


	def move_up(self):
		self.structures = []
		for ln in self.base_lab:
			line = list(ln)
			self.structures.append(line)

		if self.structures[self.x][self.y - 1] == "v":
			self.y = self.y - 1
			self.rect.x = self.rect.x
			self.rect.y = self.rect.y - sp_size

		
	def move_down(self):
		self.structures = []
		for ln in self.base_lab:
			line = list(ln)
			self.structures.append(line)

		if self.structures[self.x][self.y + 1] == "v":
			self.y = self.y + 1
			self.rect.x = self.rect.x
			self.rect.y = self.rect.y + sp_size

class Gardien(pygame.sprite.Sprite):
	def __init__(self, sp_size):
		super().__init__()
		self.x = 1
		self.y = 7
		self.image = pygame.image.load('ressource/Gardien.png')
		self.rect = self.image.get_rect()
		self.rect.x = self.x*sp_size
		self.rect.y = self.y*sp_size


class Objets(pygame.sprite.Sprite):
	def __init__(self, base, sp_size, img):
		super().__init__()
		self.base_lab = base
		self.structures = []
		self.image = pygame.image.load(img)
		self.rect = self.image.get_rect()

		for ln in self.base_lab:
			line = list(ln)
			self.structures.append(line)

		self.empty_box_list = []
		self.empty_box = []
		for x, col in enumerate(self.structures):
			for y, case in enumerate(col):
				pos_x = x*sp_size
				pos_y = y*sp_size

				if case == "v":
					pos_empty_box = (pos_x, pos_y)  
					self.empty_box_list.append(pos_empty_box)
		self.pos = choice(self.empty_box_list)



			




		
		
		



		

