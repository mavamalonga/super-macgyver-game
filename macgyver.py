import pygame
import sys
from random import *
from labyrinth import Labyrinth
from variables import *
pygame.init()


"""
Class MacGyver 
will display macgyver, manage its movements 
manage the collection of objects
"""

class MacGyver(pygame.sprite.Sprite):
    def __init__(self, mappy, sp_size, Objets, lab):
        super().__init__()
        self.objets = Objets
        self.lab = lab
        self.mappy = mappy
        self.image = pygame.image.load("ressource/MacGyver.png")
        self.rect = self.image.get_rect()
        self.x = 13                                 
        self.y = 7
        self.rect.x = self.x*sp_size
        self.rect.y = self.y*sp_size
        self.pos_macgyver = (self.x, self.y)
        self.pick_up = 0
        self.not_arrived = True
        self.mappy_copy = []
 
    def move_left(self):
        if (self.lab.mappy_copy[self.x - 1][self.y] == "v" or self.lab.mappy_copy[self.x][self.y - 1] == "g") and self.not_arrived:
            self.x = self.x - 1
            self.rect.x = self.rect.x - sp_size
            self.rect.y = self.rect.y 
        
    def move_right(self):
        if (self.lab.mappy_copy[self.x + 1][self.y] == "v" or self.lab.mappy_copy[self.x][self.y - 1] == "g") and self.not_arrived:
            self.x = self.x + 1
            self.rect.x = self.rect.x + sp_size
            self.rect.y = self.rect.y 

    def move_up(self):
        if (self.lab.mappy_copy[self.x][self.y - 1] == "v" or self.lab.mappy_copy[self.x][self.y - 1] == "g") and self.not_arrived:
            self.y = self.y - 1
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y - sp_size

    def move_down(self):
        if (self.lab.mappy_copy[self.x][self.y + 1] == "v" or self.lab.mappy_copy[self.x][self.y + 1] == "g") and self.not_arrived:
            self.y = self.y + 1
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y + sp_size

    def get_objects(self):
        if (self.rect.x, self.rect.y) == self.objets.dict_objects.get("ether"):
            self.objets.dict_objects.pop("ether")
            self.pick_up += 1
        if (self.rect.x, self.rect.y) == self.objets.dict_objects.get("tube"):
            self.objets.dict_objects.pop("tube")
            self.pick_up += 1
        if (self.rect.x, self.rect.y) == self.objets.dict_objects.get("seringue"):
            self.objets.dict_objects.pop("seringue")
            self.pick_up += 1

    def score_count(self):
        yellow =(255, 255, 0)
        text = pygame.font.SysFont('impact', 20)
        counter_pickup_objets = text.render("backpack: " + str(self.pick_up) + "/3", 50, yellow, (0, 0, 0))
        screen.blit(counter_pickup_objets, (260, 10))



