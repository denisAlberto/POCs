import pygame
import numpy as np
import random

class Shield:
    def __init__(self, size, scale=1, direction=0) -> None:
        self.size = size
        self.scale = scale
        self.direction = direction
        self.shield_n1 = pygame.image.load( 'player_1\\shield_n1.png' ).convert_alpha()
        self.shield_n1 = pygame.transform.rotate(self.shield_n1, self.direction)
        self.shield_n1 = pygame.transform.scale( self.shield_n1, 
                                                (self.shield_n1.get_width() * scale,
                                                    self.shield_n1.get_height() * scale ))
        
        self.shield_n2 = pygame.image.load( 'player_1\\shield_n2.png' ).convert_alpha()
        self.shield_n2 = pygame.transform.rotate(self.shield_n2, self.direction)
        self.shield_n2 = pygame.transform.scale( self.shield_n2, 
                                                (self.shield_n2.get_width() * scale,
                                                    self.shield_n2.get_height() * scale ))

    def render(self, surface, pos):
        shield_n1 = self.shield_n1.copy()

        surface.blit( shield_n1, (pos[0] - shield_n1.get_width()//2, 
                                  pos[1] - shield_n1.get_height()//2 ))
        
        surface.blit( self.shield_n2, (pos[0] - self.shield_n2.get_width()//2, 
                                       pos[1] - self.shield_n2.get_height()//2 ))

        # nivel_1 = pygame.Surface(self.size)
        # nivel_1.set_colorkey((0,0,0))
        # nivel_1.set_alpha(100 + 10 * random.random( ))
        # pygame.draw.arc(nivel_1, (120, 0, 255), (0, 0, self.size[0], self.size[1]), np.deg2rad(170), np.deg2rad(370), 5)
        # surface.blit( nivel_1, (pos[0] - self.size[0]//2, pos[1] - self.size[1]//2) )

        # s_2 = (self.size[0] * 0.8, self.size[1] * 0.8)
        # nivel_2 = pygame.Surface(s_2)
        # nivel_2.set_colorkey((0,0,0))
        # nivel_2.set_alpha(40)
        # pygame.draw.arc(nivel_2, (150, 255, 0), (0, 0, s_2[0], s_2[1]), np.deg2rad(170), np.deg2rad(370), int(20 * 0.7))
        # surface.blit( nivel_2, (pos[0] - s_2[0]//2, pos[1] - s_2[1]//2) )



    def check_colision():
        pass