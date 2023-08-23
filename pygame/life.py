import pygame


class Life:
    def __init__(self, divisions, size):
        self.value = 100
        self.size = size
        self.divisions = divisions
        

    def set_value(self, value):
        self.value = value


    def render(self, surface, position):
        pygame.draw.rect(surface=surface, 
                         color = (0, 0, 255), 
                         rect=(position[0],position[1], self.size[0], self.size[1]),
                          border_radius = 1 )