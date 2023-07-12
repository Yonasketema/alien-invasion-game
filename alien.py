import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        # self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)