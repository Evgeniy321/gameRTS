import pygame
from player import *
from block import *
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
run = True
hero = Player()
map = Map()
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    window.fill((0,0,0))
    hero.update(map)
    map.update()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
