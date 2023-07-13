import pygame
from constantes import * 
from auxiliar import *
from plataforma import *

class Fruta:
    def __init__(self,x,y,frame_rate_ms,is_move) -> None:
        self.stay = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Items/Fruits/Apple.png",17,1,False,1)
        self.frame = 0
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_move = is_move
        self.move_x = 0
        self.move_y = 0
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido = 0
        self.collision = False
        self.collition_fruits = pygame.mixer.Sound("PIXEL ADVENTURE/Recursos/music/recolect_sound.wav")

        self.rect_collition = pygame.Rect(self.rect)

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,(240,255,0),rect=self.rect_collition)

        if(not self.collision):
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)

    def update(self,delta_ms,platform_list,posicion_x_y):
        self.tiempo_transcurrido += delta_ms
        if(self.tiempo_transcurrido >= self.frame_rate_ms):
            self.tiempo_transcurrido = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                self.frame = 0
            self.change_x(self.move_x)
            self.change_y(self.move_y)
            
            self.move(platform_list)
            self.collition(posicion_x_y)

    def change_x(self,delta_x):
        if(self.is_move == 1):
            self.rect.x += delta_x
            self.rect_collition.x += delta_x

    def change_y(self,delta_y):
        if(self.is_move == 1):
            self.rect.y += delta_y
            self.rect_collition.y += delta_y

    def move(self,platform_list):
        self.is_on_platform = False
        for platform in platform_list:
            if(platform.move_l or platform.move_r):
                self.move_x = platform.move_x
                self.move_y = 0
            else:
                self.move_y = platform.move_y
                self.move_x = 0
    
    def collition(self,posicion_x_y):
        if(self.rect_collition.colliderect(posicion_x_y)):
            self.collision = True
            self.collition_fruits.set_volume(0.4)
            self.collition_fruits.play()
            
                            
