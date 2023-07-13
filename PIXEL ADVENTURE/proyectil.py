import pygame
from auxiliar import Auxiliar
from constantes import *

class Proyectil:
    def __init__(self,x,y,velocidad_disparo,direccion,path_image,creador) -> None:
        self.image_proyectil = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + path_image,1,False,1,2,10,10)
        self.frame = 0
        self.animation = self.image_proyectil
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.velocidad_Disparo = velocidad_disparo
        self.rect.x = x
        self.rect.y = y
        self.move_x = 0
        self.move_y = 0
        self.damage = 10
        self.creador = creador
        self.impacto_objetivo = False
        self.tiempo_colicion = 0
        self.tiempo_trayectoria = 0
        self.collition_rect = pygame.Rect(self.rect)
        self.rect_collition_varios_r = pygame.Rect(self.rect.x + 25,self.rect.y,self.rect.w - 27,self.rect.h)
        self.rect_collition_varios_l = pygame.Rect(self.rect.x,self.rect.y,self.rect.w - 20,self.rect.h)
        self.direccion = direccion
        self.explosion_sound = pygame.mixer.Sound("PIXEL ADVENTURE/Recursos/music/explosion.wav")
        self.explosion_sound.set_volume(0.4)
        self.is_collision_bala = False

    def trayectoria(self):
        if self.direccion == DIRECTION_R:
            self.move_x = self.velocidad_Disparo
            self.change_x(self.move_x)
        elif self.direccion == DIRECTION_L:
            self.move_x = -self.velocidad_Disparo
            self.change_x(self.move_x)

    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,color=(255,0,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,255),rect=self.rect_collition_varios_l)
            pygame.draw.rect(screen,color=(255,255,255),rect=self.rect_collition_varios_r)

        if self.impacto_objetivo == False:
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.rect_collition_varios_l.x += delta_x
        self.rect_collition_varios_r.x += delta_x
 
    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.rect_collition_varios_r.y += delta_y
        self.rect_collition_varios_r.y += delta_y

    def update(self,lista_objetivos):   
        self.collision(lista_objetivos)
        self.trayectoria()
        self.collision_fuera_image()

    def collision(self,lista_objetivos):
        for objetivo in lista_objetivos:
            if self.rect_collition_varios_l.colliderect(objetivo.rect_collition_bala_r):
                self.explosion_sound.play()
                objetivo.impacto = True
                objetivo.damage_generate = self.damage
                objetivo.colision_bala()
                self.velocidad_Disparo = 0
                self.impacto_objetivo = True
                
    def collision_fuera_image(self):
        if(self.rect.x <= -20 or self.rect.x >= 1600):
            self.impacto_objetivo = True
    
            


    







