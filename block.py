import pygame 
from random import randint as r
import coin
blocksize = 64
class Platform:
    def __init__(self,pos, size) -> None:
        self.image = pygame.Surface((blocksize*size, blocksize))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect(center = pos)
    def collideplat(self, other):
        res = 0
        for oPlat in other:
            if self.rect.colliderect(oPlat.rect):
                res+= 1
        return res
    def update(self):
        pygame.display.get_surface().blit(self.image, self.rect)
        pygame.draw.rect(pygame.display.get_surface(), (255,0,0), self.rect, 4)

class Map:
    def __init__(self, platformcount = 5) -> None:
        self.allplatforms = [Platform((r(32, 600), i*100), r(2, 8)) for i in range(platformcount)]
        self.coin = coin.Coin()
            
    def colidePlatform(self, other):
        self.coin.get(other)
        for i in self.allplatforms:
            if i.rect.colliderect(other.rect):
                return i
        return False


    def movePlatform(self):
        for i in self.allplatforms:
            i.rect.y += 2
            if i.rect.top >= 600:
                i.rect.bottom = 0
                i.rect.centerx = r(0, 800)
      
    def update(self):
        self.movePlatform()
        self.coin.update()
        for i in self.allplatforms:
            i.update()
