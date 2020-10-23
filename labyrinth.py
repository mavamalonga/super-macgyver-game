import pygame
from variables import *

"""
class Labyrinth :
construction of the labyrinth structure
"""

class Labyrinth:
    def __init__(self, mappy, sp_size):
        pygame.init()
        self.mappy = mappy
        self.screen = pygame.display.set_mode((15*sp_size, 15*sp_size))
        self.empty_box_list = []

    def convert_file_txt(self):
        self.mappy_copy = []
        with open(self.mappy, "r") as f:
            for ln in f:
                line = list(ln)
                self.mappy_copy.append(line)

    def get_pos(self):
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
               