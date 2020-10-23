import pygame
import sys
from random import *
from variables import *
pygame.init()


"""
class Labyrinth :
construction of the labyrinth structure
- the walls
- the arrival
- the decoration
"""

class Labyrinth:
    def __init__(self, mappy, sp_size):
        pygame.init()
        self.mappy = mappy
        self.screen = pygame.display.set_mode((15*sp_size, 15*sp_size))
        self.empty_box_list = []

    def build_lab(self):
        self.mappy_copy = []
        with open(self.mappy, "r") as f:
            for ln in f:
                line = list(ln)
                self.mappy_copy.append(line)

        for x, col in enumerate(self.mappy_copy):  
            for y, box in enumerate(col):
                pos_x = x*sp_size
                pos_y = y*sp_size

                if box == "s":
                    self.screen.blit(pygame.image.load("ressource/stones.png"), (pos_x, pos_y))
                elif box == "v":
                    self.screen.blit(pygame.image.load("ressource/black_bloc.png"), (pos_x, pos_y))
                    self.empty_box_list.append((pos_x, pos_y))
                elif box == "d":
                    self.screen.blit(pygame.image.load("ressource/decorations3.png"),(pos_x, pos_y))
                elif box == "l":
                    self.screen.blit(pygame.image.load("ressource/decorations4.png"),(pos_x, pos_y))
                elif box == "e":
                    self.screen.blit(pygame.image.load("ressource/exit.png"),(pos_x, pos_y))
                elif box == "k":
                    self.screen.blit(pygame.image.load("ressource/skull.png"),(pos_x, pos_y))
               

"""
Class MacGyver 
will display macgyver, manage its movements 
manage the collection of objects
"""

class MacGyver(pygame.sprite.Sprite):
    def __init__(self, mappy, sp_size, Objets):
        super().__init__()
        self.objets = Objets
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
        with open(self.mappy, "r") as f:
            for ln in f:
                line = list(ln)
                self.mappy_copy.append(line)

    """
    The 4 methods below will manage the movement of the macgyver sprite
    Each method corresponds to a direction of displacement
    """
    def move_left(self):
        if (self.mappy_copy[self.x - 1][self.y] == "v" or self.mappy_copy[self.x][self.y - 1] == "g") and self.not_arrived:
            self.x = self.x - 1
            self.rect.x = self.rect.x - sp_size
            self.rect.y = self.rect.y 
        
    def move_right(self):
        if (self.mappy_copy[self.x + 1][self.y] == "v" or self.mappy_copy[self.x][self.y - 1] == "g") and self.not_arrived:
            self.x = self.x + 1
            self.rect.x = self.rect.x + sp_size
            self.rect.y = self.rect.y 


    def move_up(self):
        if (self.mappy_copy[self.x][self.y - 1] == "v" or self.mappy_copy[self.x][self.y - 1] == "g") and self.not_arrived:
            self.y = self.y - 1
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y - sp_size

        
    def move_down(self):
        if (self.mappy_copy[self.x][self.y + 1] == "v" or self.mappy_copy[self.x][self.y + 1] == "g") and self.not_arrived:
            self.y = self.y + 1
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y + sp_size

            
    def get_objects(self):
      
        if (self.rect.x, self.rect.y) == self.objets.dict_objects.get("ether"):
            self.objets.dict_objects.pop("ether")
            self.pick_up += 1
        if (self.rect.x, self.rect.y) == self.objets.dict_objects.get("tube_platique"):
            self.objets.dict_objects.pop("tube_platique")
            self.pick_up += 1
        if (self.rect.x, self.rect.y) == self.objets.dict_objects.get("seringue"):
            self.objets.dict_objects.pop("seringue")
            self.pick_up += 1

    def score_count(self):
        yellow =(255, 255, 0)
        text = pygame.font.SysFont('impact', 20)
        counter_pickup_objets = text.render("backpack: " + str(self.pick_up) + "/3", 50, yellow, (0, 0, 0))
        screen.blit(counter_pickup_objets, (260, 10))



"""
class Guardian
define the guardian's characters
display the guardien
"""
class Guardian(pygame.sprite.Sprite):
    def __init__(self, sp_size):
        super().__init__()
        self.x = 1
        self.y = 7
        self.image = pygame.image.load('ressource/Gardien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.x*sp_size
        self.rect.y = self.y*sp_size
        self.pos_guardian = (self.x, self.y)

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


        self.dict_objects = {
        "ether": 0,
        "tube_plastique": 0,
        "seringue": 0
        }

        
        self.dict_objects["ether"] =  self.lab.empty_box_list[randint(0, 122)]
        self.dict_objects["tube_platique"] = self.lab.empty_box_list[randint(0, 122)]
        self.dict_objects["seringue"] = self.lab.empty_box_list[randint(0, 122)]

    def display_objects(self):    
        if "ether" in self.dict_objects:
            screen.blit(self.img_ether, self.dict_objects.get("ether"))
        if "tube_platique" in self.dict_objects:
            screen.blit(self.img_tube, self.dict_objects.get("tube_platique"))
        if "seringue" in self.dict_objects:
            screen.blit(self.img_seringue, self.dict_objects.get("seringue"))