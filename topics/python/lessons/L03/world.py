import pygame

class World:
    def __init__(self):
        self.platforms = [
            pygame.Rect(0, 550, 800, 50),
            pygame.Rect(250, 430, 200, 30),
            pygame.Rect(520, 330, 180, 30),
        ]

    def draw(self, screen):
        for p in self.platforms:
            pygame.draw.rect(screen, (80, 200, 120), p)