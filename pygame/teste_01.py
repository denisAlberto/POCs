import pygame
from cannon import Cannon

pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_1 = Cannon( 1, 1 )
player_2 = Cannon( 2, 1 )

balls_p1 = []
balls_p2 = []

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_f]:
        balls_p1.append( player_1.fire() )
        balls_p2.append( player_2.fire() )

    screen.fill("black")

    player_1.render(screen)
    player_2.render(screen)

    for i, c in enumerate(balls_p1):
        c.render(screen)
        player_2.check_colision(c)
        
    balls_p1 = [c for c in balls_p1 if not c.can_destroy()]

    for i, c in enumerate(balls_p2):
        c.render(screen)
        player_1.check_colision(c)

    balls_p2 = [c for c in balls_p2 if not c.can_destroy()]

    if len(balls_p1)>0:
        print(f'p1 {len(balls_p1)}')
    
    if len(balls_p2)>0:
        print(f'p2 {len(balls_p2)}')


    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()