import numpy as np
from PIL import Image, ImageDraw, ImageOps
import pygame
import io

def get_circular_img(image):
    imgsize = (image.size[0], image.size[1])
    mask = Image.new('L', imgsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + imgsize, fill=255)
    mask = mask.resize(imgsize, Image.ANTIALIAS)
    image.putalpha(mask)
    return image

class CannonBall:
    def __init__(self, img, diameter, direction, pos) -> None:
        self.destroy = False
        self.pos = [pos[0], pos[1]]
        self.diameter = diameter
        self.direction = direction
        
        self.explode = False
        self.explosion_frame = 0
        self.explosion_img = pygame.image.load( 'explo.png').convert_alpha()
        
        min_len = min(img.size)
        x_crop = img.size[0]//2 - min_len//2
        y_crop = img.size[1]//2 - min_len//2
        img = img.crop((x_crop, y_crop, x_crop + min_len, y_crop + min_len))
        
        # resize
        img = img.resize( (diameter, diameter) )
        img = get_circular_img(img)

        mode = img.mode
        size = img.size
        self.img = pygame.image.fromstring(img.tobytes(), size, mode)   


    def render(self, surface):
        
        if not self.explode:
            self.pos[0] += self.direction[0]
            self.pos[1] += self.direction[1]
            surface.blit( self.img, self.pos )

            if self.pos[0] < -self.diameter or\
                self.pos[1] < -self.diameter:
                self.destroy = True

            if surface.get_width() < self.pos[0] + self.diameter or\
                surface.get_height() < self.pos[1] + self.diameter:
                self.destroy = True
        else:
            if self.explosion_frame < 4:
                w, h = 103, 103
                explosion = pygame.Surface( (w, h) ).convert_alpha()
                explosion.blit(self.explosion_img, (0,0), ((self.explosion_frame * w), 0, w, h))
                explosion.set_colorkey((0,0,0))
                surface.blit(explosion, ( self.pos[0] - 30, self.pos[1] - 50 ) )

                self.explosion_frame += 1
            else:
                self.destroy = True
                               

    def explosion(self):
        self.explode = True


    def can_destroy(self):
        return self.destroy