import pygame
import sys
from input import Input


class Base(object):
    def __init__(self):
        pygame.init()
        screen_size = (512, 512)
        display_flags = pygame.DOUBLEBUF | pygame.OPENGL
        self.screen = pygame.display.set_mode(screen_size, display_flags)
        pygame.display.set_caption("OPENGL TEST")
        self.running = True
        self.clock = pygame.time.Clock()
        self.input = Input()

    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):
        self.initialize()
        
        while( self.running ):

            self.input.update()

            if self.input.quit:
                self.running = False

            self.update()

            pygame.display.flip()

            self.clock.tick(60)


        pygame.quit()
        sys.exit()



