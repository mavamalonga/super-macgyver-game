import pygame
from labyrinth import Labyrinth
from variables import *
from random import *

"""
class Objects
generate objects on the window
define the positions of objects randomly
"""
class Objects(pygame.sprite.Sprite):
    def __init__(self, Lab):
        super().__init__()
        self.lab = Lab
        self.img_ether = pygame.image.load('ressource/ether1.png')
        self.img_tube = pygame.image.load('ressource/tube_plastique1.png')
        self.img_seringue = pygame.image.load('ressource/seringue1.png')

    def random(self):
        self.dict_objects = {
        "ether": self.lab.empty_box_list[randint(0, 121)],
        "tube": self.lab.empty_box_list[randint(0, 121)],
        "seringue": self.lab.empty_box_list[randint(0, 121)]
        }


    def display_objects(self):    
        if "ether" in self.dict_objects:
            screen.blit(self.img_ether, self.dict_objects.get("ether"))
        if "tube" in self.dict_objects:
            screen.blit(self.img_tube, self.dict_objects.get("tube"))
        if "seringue" in self.dict_objects:
            screen.blit(self.img_seringue, self.dict_objects.get("seringue"))