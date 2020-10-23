import pygame

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