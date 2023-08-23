import pygame
from cannon import Cannon

pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_1 = Cannon( 1, 1 )
player_2 = Cannon( 2, 1 )

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    player_1.render(screen)
    player_2.render(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_f]:
        player_1.fire()
        player_2.fire()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()