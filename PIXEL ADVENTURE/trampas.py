import pygame
from constantes import *
from auxiliar import *

class Trampa:
    def __init__(self,x,y,move_rate_ms,screen) -> None:
        self.stay= Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Traps/Saw/On (38x38).png",8,1,False,1)
        
        self.screen = screen
        self.frame = 0
        self.move_rate_ms = move_rate_ms   
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tiempo_transcurrido_move = 0
        self.collition_rect = pygame.Rect(x,y,self.rect.width,self.rect.height)
    
    def update(self,delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            if(self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                self.frame = 0
    
    def draw(self):
        if(DEBUG):
            pygame.draw.rect(self.screen,color=(255,255,0),rect=self.collition_rect)

        self.image = self.animation[self.frame]
        self.screen.blit(self.image,self.rect)