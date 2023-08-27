import pygame
import numpy as np

class HorizontalStatusBar:
    def __init__(self, 
                 divisions=10, 
                 chunk_len=5, 
                 border_len=1, 
                 height=10, 
                 space_len=1,
                 color=(0,255,0)):
        self.value = 100
        self.size = ( 2 * border_len + divisions * chunk_len + space_len * (divisions-1), height )
        self.chunk_len = chunk_len
        self.divisions = divisions
        self.space_len = space_len
        self.border_len = border_len
        self.color = color
        

    def set_value(self, value):
        self.value = value


    def render(self, surface, position ):

        pygame.draw.rect(surface=surface, 
                         color = (0, 0, 0), 
                         rect=(position[0], position[1], self.size[0], self.size[1]),
                         border_radius = 2 )

        for i in range(self.divisions):
            chunk_x = position[0] + i * self.chunk_len + i * self.space_len + self.border_len
            
            pygame.draw.rect(surface=surface, 
                             color = self.color, 
                             rect=(chunk_x, position[1] + self.border_len, self.chunk_len, self.size[1] - (2*self.border_len)),
                             border_radius = 1 )
                
        # pygame.draw.rect(surface=surface, 
        #                  color = self.color, 
        #                  rect=(position[0], position[1], self.size[0], self.size[1]),
        #                  border_radius = 1 )