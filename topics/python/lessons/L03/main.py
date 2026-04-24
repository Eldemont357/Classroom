import pygame
from settings import *
from player import Player
from world import World

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player(100, 400)
world = World()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(world.platforms)

    screen.fill((92, 148, 252))

    world.draw(screen)
    player.draw(screen)

    pygame.display.update()

pygame.quit()