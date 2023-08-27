from typing import Any
import pygame
import random
import numpy as np
from horizontalStatusBar import HorizontalStatusBar
from cannon_ball import CannonBall
import os
from PIL import Image
from shield import Shield
import math

class Cannon:
    def __init__(self,
                 player_number, 
                 scale,
                 ang_inc = 0.4) -> None:
        
        self.ball_velocity = 1.5
        self.destroy = False
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
        
        self.life_bar = HorizontalStatusBar(color=( 0,255, 0 ), border_len=2, chunk_len=8, space_len=2 )
        self.shield_bar = HorizontalStatusBar( color=( 0, 0, 255 ), border_len=2, chunk_len=8, space_len=2 )
        
        if player_number == 1:
            self.shield = Shield((200, 200), scale, 180)
        else:
            self.shield = Shield((200, 200), scale)

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
            self.shield.render(screen, self.position )

            self.life_bar.render( surface=screen, position=(self.position[0]-self.cannon_image.get_width()//2, 
                                                            self.position[1]-self.cannon_image.get_height()//2 ))
            
            self.shield_bar.render( surface=screen, position=(  self.position[0]-self.cannon_image.get_width()//2, 
                                                                self.position[1]-self.cannon_image.get_height()//2 - 15 ))
            
            

        else:
            self.shield.render(screen, self.position )

            self.life_bar.render( surface=screen, position=(self.position[0]-self.cannon_image.get_width()//2, 
                                                            self.position[1]+self.cannon_image.get_height()//2 ))
            
            self.shield_bar.render( surface=screen, position=(  self.position[0]-self.cannon_image.get_width()//2, 
                                                                self.position[1]+self.cannon_image.get_height()//2 + 15 ))
            
        
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

        arquivos_png = [f for f in os.listdir('imgs') if f.endswith('.png')]
        img = Image.open(f'imgs\\{random.choice(arquivos_png)}')
        
        if self.player_number == 1:
            direction = [np.sin(np.deg2rad(self.angle)) * self.ball_velocity, 
                        np.cos(np.deg2rad(self.angle)) * self.ball_velocity]
            pos = [self.position[0] - 15 + np.sin(np.deg2rad(self.angle)) * 60,
               self.position[1] - 15 + np.cos(np.deg2rad(self.angle)) * 60 ]
        else:
            direction = [np.sin(np.deg2rad(self.angle)) * -self.ball_velocity, 
                        np.cos(np.deg2rad(self.angle)) * -self.ball_velocity]
            pos = [self.position[0] - 15 - np.sin(np.deg2rad(self.angle)) * 60,
               self.position[1] - 15 - np.cos(np.deg2rad(self.angle)) * 60 ]
        
        return CannonBall(img, 30, direction, pos)


    def special(self):
        pass



    def check_colision(self, cannon_ball):
        dist = math.hypot(cannon_ball.pos[0] + cannon_ball.diameter//2 - self.position[0], 
                          cannon_ball.pos[1] + cannon_ball.diameter//2 - self.position[1])

        if self.shield_bar.value > 0:
            if dist < cannon_ball.diameter + 50:
                cannon_ball.explosion()
        else:
            if dist < cannon_ball.diameter + 30:
                cannon_ball.explosion()