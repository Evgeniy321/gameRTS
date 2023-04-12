import pygame
import block
maxspeed = 5
jumpheight = 20
class Player():
    def __init__(self) -> None:
        self.speed = pygame.math.Vector2(0,0)
        self.image = pygame.Surface((64,64))
        self.image.fill((255,255,255))
        self.onground = False
        self.rect = self.image.get_rect(center = (400,300))

    def checkGround(self, map: block.Map):
        platform = map.colidePlatform(self)
        if platform:
            self.speed.xy = (0,0)
            self.onground = True
        else:
            self.onground = False
        

    def move(self):
        keys = pygame.key.get_pressed()
        
        if self.onground:
            self.speed.y = 0
        else:
            self.speed.y += 1
        if keys[pygame.K_d]:
            self.speed.x = maxspeed
        elif keys[pygame.K_a]:
            self.speed.x = -maxspeed
        else:
            self.speed.x = 0
        if keys[pygame.K_SPACE] and self.onground:
            self.speed.y = -jumpheight

        self.rect.center += self.speed

    def update(self, map : block.Map):
        self.checkGround(map)
        self.move()
        pygame.display.get_surface().blit(self.image, self.rect)

