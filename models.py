import pygame
import sys
pygame.init()



class Position:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Labyrinthe(pygame.sprite.Sprite):
	ZONES = []
	MIN_CASE = 0
	MAX_CASE = 15
	WIDTH_CASE = 1
	MIN_CASEY = 0
	MAX_CASEY = 15
	HEIGHT_CASE = 1

	def __init__(self):
		super().__init__()
		self.vide = []


	@classmethod
	def initialize_zones(cls):
		for caseX in range(cls.MIN_CASE, cls.MAX_CASE, cls.WIDTH_CASE):
			for caseY in range(cls.MIN_CASEY, cls.MAX_CASEY, cls.HEIGHT_CASE):
				bottom_left_corner = Position(caseX, caseY)
				top_right_corner = Position(caseX + cls.WIDTH_CASE, caseY + cls.HEIGHT_CASE)
				zone = Labyrinthe(bottom_left_corner, top_right_corner)
				cls.ZONES.append(zone)
				print(len(cls.ZONES))




class MacGyver(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('ressource/MacGyver.png')
		self.rect = self.image.get_rect()
		self.rect.x = 100
		self.rect.y = 100
		self.position = Position(self.rect.x, self.rect.y)



