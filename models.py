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

    def build_lab(self):
        self.mappy_copy = []
        with open(self.mappy, "r") as f:
            for ln in f:
                line = list(ln)
                self.mappy_copy.append(line)

        for x, col in enumerate(self.mappy_copy):  #retrieve the coordinates of the cases to display the images
            for y, box in enumerate(col):
                pos_x = x*sp_size
                pos_y = y*sp_size

                
               # on va attribuer a chaque case l'image qu'il lui convient 

                if box == "s":
                    self.screen.blit(pygame.image.load("ressource/stones.png"), (pos_x, pos_y))
                elif box == "v":
                    self.screen.blit(pygame.image.load("ressource/black_bloc.png"), (pos_x, pos_y))
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
va afficher macgyver, gerer ses deplacements 
gerer le ramassage des objets

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
        self.not_arrived = True   #condition d'arret du jeu lors que macgyver se trouve en position de sorti
        self.mappy_copy = []
        with open(self.mappy, "r") as f:
            for ln in f:
                line = list(ln)
                self.mappy_copy.append(line)

    """
    Les 4 methodes ci dessous correspondent vont gerer les deplacemengt du sprite macgyver 
    Chaque méthode correspond a une direction de déplament
    elle seront appelés lors des evenement clavier correspondent
    Pour chaque deplament la condition if verifie si le deplacement est possible

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

            """
            cette methode recupe la position des objets depuis la classe objets le compare a la position macgyver
            supprimer les objets ramassé 
            incrementer le compter d'objets ramassé
            """
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


"""
class Guardian
definie les caracteres du gardien
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
generer les objets sur la fenetre
definir les position les position des objects aleatoirement 
"""
class Objects(pygame.sprite.Sprite):
    def __init__(self, mappy, sp_size):
        super().__init__()
        self.mappy = mappy
        self.img_ether = pygame.image.load('ressource/ether1.png')
        self.img_tube = pygame.image.load('ressource/tube_plastique1.png')
        self.img_seringue = pygame.image.load('ressource/seringue1.png')

        
        with open(self.mappy, "r") as f:
            self.mappy_copy = []
            for ln in f:
                line = list(ln)
                self.mappy_copy.append(line)

        self.empty_box_list = []
        for x, col in enumerate(self.mappy_copy):
            for y, box in enumerate(col):
                pos_x = x*sp_size
                pos_y = y*sp_size

                if box == "v":
                    pos_empty_box = (pos_x, pos_y)                # recuperer les coordonnées des cases vides de la structure
                    self.empty_box_list.append(pos_empty_box)

        self.dict_objects = {       #bibliotheque qui va héberger les cordonnées de des objets
        "ether": 0,
        "tube_plastique": 0,
        "seringue": 0
        }

        self.dict_objects["ether"] = choice(self.empty_box_list)       #random choice choisir un index aléatoire dans la liste 
        self.dict_objects["tube_platique"] = choice(self.empty_box_list)
        self.dict_objects["seringue"] = choice(self.empty_box_list)

    def display_objects(self):    #vérifier l'existence de la clé demandé dans la bibliotheque puis l'afficher 
        if "ether" in self.dict_objects:
            screen.blit(self.img_ether, self.dict_objects.get("ether"))
        if "tube_platique" in self.dict_objects:
            screen.blit(self.img_tube, self.dict_objects.get("tube_platique"))
        if "seringue" in self.dict_objects:
            screen.blit(self.img_seringue, self.dict_objects.get("seringue"))