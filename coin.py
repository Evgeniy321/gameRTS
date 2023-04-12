import pygame
from random import randint as r
blocksize = 64
pygame.init()
class Coin():
    def __init__(self) -> None:
        self.image = pygame.Surface((blocksize, blocksize))
        self.image.fill((255, 234, 3))
        self.rect =  pygame.Rect(r(0, 736), r(0, 536), blocksize, blocksize)
        self.count = 0
        self.font = pygame.font.SysFont("arial", 25)
        self.lable = self.font.render(str(self.count), True, (237, 225, 92))
    def get(self, player):
        if self.rect.colliderect(player.rect):
            self.count += 1
            self.rect.center = (r(64, 736), r(64, 536))
            self.lable = self.font.render(str(self.count), True, (237, 225, 92))

    def update(self):
        pygame.display.get_surface().blit(self.image, self.rect)
        pygame.display.get_surface().blit(self.lable,(10, 10))
