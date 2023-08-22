from typing import Any
import pygame
import random

class Cannon:
    def __init__(self, 
                 position, 
                 player_number, 
                 scale) -> None:
        
        self.max_angle = 30
        self.life = 100
        self.angle_inc = 0.35
        self.angle = random.uniform(-self.max_angle, self.max_angle)
        self.clockwise = random.choice([True, False])
        self.position = position
        self.cannon_image = pygame.image.load(f'player_{player_number}//cannon.png').convert_alpha()
        self.cannon_image = pygame.transform.scale( self.cannon_image, 
                                                    (self.cannon_image.get_width() * scale,
                                                        self.cannon_image.get_height() * scale ))
        
        self.base = pygame.image.load(f'player_{player_number}//cannon_base.png').convert_alpha()
        self.base = pygame.transform.scale( self.base, 
                                            (self.base.get_width() * scale,
                                                self.base.get_height() * scale ))

    def render(self, screen):
        rotated = pygame.transform.rotate(self.cannon_image, self.angle)
        screen.blit(rotated, (self.position[0] - rotated.get_width() // 2, self.position[1] - rotated.get_height() // 2))

        rotated = pygame.transform.rotate(self.base, self.angle)
        screen.blit(rotated, (self.position[0] - rotated.get_width() // 2, self.position[1] - rotated.get_height() // 2))

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
        pass

    def special(self):
        pass

    def get_damage(self):
        pass
        