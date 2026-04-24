import pygame
from settings import GRAVITY

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load(
            "assets/Pixel Adventure 1/Main Characters/Mask Dude/Idle (32x32).png"
        ).convert_alpha()

        self.image = self.image.subsurface((0, 0, 32, 32))
        self.image = pygame.transform.scale(self.image, (64, 64))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 5
        self.velocity_y = 0
        self.jump_power = -15
        self.on_ground = False

    def update(self, platforms):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_power
            self.on_ground = False

        # гравитация
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # коллизии
        self.on_ground = False
        for p in platforms:
            if self.rect.colliderect(p) and self.velocity_y >= 0:
                self.rect.bottom = p.top
                self.velocity_y = 0
                self.on_ground = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)