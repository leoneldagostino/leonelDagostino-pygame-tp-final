import pygame
from constantes import *
from auxiliar import Auxiliar

class Platform:
    def __init__(self, x, y,ancho,speed,alto,move_rate_ms,punto_volver_plat_l,punto_volver_plat_r,speed_up_down,type,puntos_volver_plat_up):

        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "space/Tiles/Tile ({0}).png",15,False,1,1,w=ancho,h=alto)
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_x = 0
        self.move_y = 0
        self.punto_volver_plat_l = punto_volver_plat_l
        self.punto_volver_plat_r = punto_volver_plat_r
        self.punto_volver_plat_up = puntos_volver_plat_up

        self.speed_up_down = speed_up_down

        self.move_up = False
        self.move_down = False

        self.move_l = False
        self.move_r = True

        self.speed = speed
        self.collition_rect = pygame.Rect(self.rect)
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_COLLIDE_H)
        self.rect_collition_bala_r = pygame.Rect(self.rect)
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms

        self.impacto = False
     
        self.speed_up_down = speed_up_down

    def draw(self,screen):
        '''
        Dibuja la plataforma y los rectagunlos en caso de ser necesario.
        Recibe por parametro la pantalla. 
        '''
        screen.blit(self.image,self.rect)
        if DEBUG:
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_ground_collition)

    def update(self,time_delta):   
        self.tiempo_transcurrido_move += time_delta
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            self.punto_volver()
            self.move_platform_x()
            self.move_platform_y()
            self.tiempo_transcurrido_move = 0

    def change_x(self,delta_x):
        '''
        El metodo produce el movimiento del rectangulo del mismo de manera horizontal y seguida de sus rectangulos correspondiente.
        Recibe por parametro el delta_x.
        '''
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.rect_ground_collition.x += delta_x
        self.rect_collition_bala_r.x += delta_x

    def change_y(self,delta_y):
        '''
        El metodo produce el movimiento del rectangulo del mismo de manera vertical y seguida de sus rectangulos correspondiente.
        Recibe por parametro el delta_y.
        '''
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.rect_ground_collition.y += delta_y
        self.rect_collition_bala_r.y += delta_y

    def move_platform_x(self):
        '''
        El metodo mueve la plataforma de manera horizontal dependiendo el speed ingresado.
        '''
        if self.move_r:
            self.move_x = self.speed
            self.change_x(self.move_x)
        elif self.move_l:
            self.move_x = -self.speed
            self.change_x(self.move_x)

    def move_platform_y(self):
        '''
        El metodo mueve la plataforma de manera vertical dependiendo el speed ingresado.
        '''
        if self.move_up:
            self.move_y = -self.speed_up_down
            self.change_y(self.move_y)
        elif self.move_down:
            self.move_y = self.speed_up_down
            self.change_y(self.move_y)

    def punto_volver(self):
        '''
        El metodo verifica la posicion de la plataforma y dependiendo la ubicación del rect se produce los eventos.
        '''
        if self.rect.x >= self.punto_volver_plat_r and self.rect.y >= 550:
            self.move_r = False
            self.move_l = True
            self.move_down = False
        elif self.rect.x <= self.punto_volver_plat_l and self.rect.y >= 550:
            self.move_x = 0
            self.move_r = False
            self.move_l = False
            self.move_up = True
            self.move_down = False
        
        if self.rect.y <= self.punto_volver_plat_up:
            self.move_up = False
            self.move_down = True

    def colision_bala(self):
        '''
        El metodo verifica si la bala colision con la plataforma para luego poder removerla de la lista.
        '''
        if self.impacto:
            self.impacto = False
    