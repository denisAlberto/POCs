from typing import Any
import pygame
import random
import numpy as np
from life import Life

class Cannon:
    def __init__(self,
                 player_number, 
                 scale,
                 ang_inc = 0.4) -> None:
        
        self.scale = scale
        self.firing = False
        self.max_angle = 30
        self.angle_inc = ang_inc
        self.cannon_retraction = 0
        self.player_number = player_number
        self.clockwise = random.choice([True, False])
        self.angle = random.uniform(-self.max_angle, self.max_angle)
        
        self.cannon_image = pygame.image.load(f'player_{player_number}//cannon.png').convert_alpha()
        self.cannon_image = pygame.transform.scale( self.cannon_image, 
                                                    (self.cannon_image.get_width() * scale,
                                                     self.cannon_image.get_height() * scale ))
        
        self.life = Life(divisions=15, 
                         size=( self.cannon_image.get_width(),
                                self.cannon_image.get_height() * 0.05 ) )

        self.base = pygame.image.load(f'player_{player_number}//cannon_base.png').convert_alpha()
        self.base = pygame.transform.scale( self.base, 
                                            (self.base.get_width() * scale,
                                                self.base.get_height() * scale ))
        
        if player_number == 1:
            self.direction = 180
        elif player_number == 2:
            self.direction = 0

    def render(self, screen):
        if self.player_number == 1:
            self.position = (screen.get_width()//2, 100)
        else:
            self.position = (screen.get_width()//2, screen.get_height() - 100)
        
        if self.firing:
            rotated = pygame.transform.rotate(self.cannon_image, self.angle + self.direction)
            screen.blit(rotated, (self.position[0] + (np.sin(np.deg2rad(self.angle + self.direction)) * self.cannon_retraction) -
                                  rotated.get_width() // 2, 
                                  self.position[1] + (np.cos(np.deg2rad(self.angle + self.direction)) * self.cannon_retraction) - 
                                  rotated.get_height() // 2))
           
            self.cannon_retraction -= 1
            if self.cannon_retraction < 0:
                self.cannon_retraction = 0
                self.firing = False
        else:
            rotated = pygame.transform.rotate(self.cannon_image, self.angle + self.direction)
            screen.blit(rotated, (self.position[0] - rotated.get_width() // 2, self.position[1] - rotated.get_height() // 2))

        rotated = pygame.transform.rotate(self.base, self.angle + self.direction)
        screen.blit(rotated, (self.position[0] - rotated.get_width() // 2, self.position[1] - rotated.get_height() // 2))

        if self.player_number == 1:
            self.life.render( surface=screen, position=(self.position[0]-self.cannon_image.get_width()//2, 
                                                        self.position[1]-self.cannon_image.get_height()//2 ))
        else:
            self.life.render( surface=screen, position=(self.position[0]-self.cannon_image.get_width()//2, 
                                                        self.position[1]+self.cannon_image.get_height()//2 ))

        if self.clockwise:
            if self.angle > -self.max_angle:
                self.angle -= self.angle_inc
            else:
                self.clockwise = False                
        else:
            if self.angle < self.max_angle:
                self.angle += self.angle_inc
            else:
                self.clockwise = True


        
    def fire(self):
        self.firing = True
        self.cannon_retraction = 10

    def special(self):
        pass

    def get_damage(self):
        pass
        