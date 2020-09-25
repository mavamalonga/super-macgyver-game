import pygame
import sys
from random import *
from variables import *
pygame.init()
        

class Labyrinthe:
    def __init__(self, mappy, sp_size):
        pygame.init()
        self.base_lab = mappy
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
    def __init__(self, lab, sp_size, Objets):
        super().__init__()
        self.objets = Objets
        self.base_lab = lab
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

        if self.structures[self.x - 1][self.y] == "v" or self.structures[self.x][self.y - 1] == "g":
            self.x = self.x - 1
            self.rect.x = self.rect.x - sp_size
            self.rect.y = self.rect.y 
        
    def move_right(self):
        
        self.structures = []
        for ln in self.base_lab:
            line = list(ln)
            self.structures.append(line)

        if self.structures[self.x + 1][self.y] == "v" or self.structures[self.x][self.y - 1] == "g":
            self.x = self.x + 1
            self.rect.x = self.rect.x + sp_size
            self.rect.y = self.rect.y 


    def move_up(self):
        self.structures = []
        for ln in self.base_lab:
            line = list(ln)
            self.structures.append(line)

        if self.structures[self.x][self.y - 1] == "v" or self.structures[self.x][self.y - 1] == "g":
            self.y = self.y - 1
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y - sp_size

        
    def move_down(self):
        self.structures = []
        for ln in self.base_lab:
            line = list(ln)
            self.structures.append(line)

        if self.structures[self.x][self.y + 1] == "v" or self.structures[self.x][self.y + 1] == "g":
            self.y = self.y + 1
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y + sp_size

    def get_objets(self):
        if (self.rect.x, self.rect.y) == self.objets.empty_box[0]:
            print("yes")

class Gardien(pygame.sprite.Sprite):
    def __init__(self, sp_size):
        super().__init__()
        self.x = 1
        self.y = 7
        self.image = pygame.image.load('ressource/Gardien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.x*sp_size
        self.rect.y = self.y*sp_size
        self.pos_mac =(self.x*sp_size, self.y*sp_size)


class Objets(pygame.sprite.Sprite):
    def __init__(self, lab, sp_size):
        super().__init__()
        self.base_lab = lab
        self.structures = []
        self.img_ether = pygame.image.load('ressource/ether1.png')
        self.img_tube = pygame.image.load('ressource/tube_plastique1.png')
        self.img_seringue = pygame.image.load('ressource/seringue1.png')

        
        self.structures = []
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

        # select Three empty position random for objets
        for i in range(3):
            self.pos = choice(self.empty_box_list)
            self.empty_box.append(self.pos)

    def display_objets(self):
        screen.blit(self.img_ether, self.empty_box[0])
                
                




        
        
        



        

