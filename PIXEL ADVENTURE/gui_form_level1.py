import pygame
from gui_form import *
from pygame.locals import *
import sys
import sqlite3 as sql
from constantes import *
from player import *
from plataforma import *
from score import *
from gui_barravida import *
from info_levels import *
from gui_textbox import *
from gui_widget import *

class LevelUno(Form):
    def __init__(self, name, master, x, y, ancho, alto, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master, x, y, ancho, alto, color_border, active, image_background, color_background)

        self.master = master
        self.name = name
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color_border = color_border
        self.active = active
        self.image_background = image_background
        self.color_background = color_background

        #Lista con la información total del level 2.
        self.lista_info = Datalevels(master,"level_uno")

        #Imagen de fondo que va a tener el nivel 2.
        self.imagen_fondo = pygame.image.load(PATH_IMAGE + self.lista_info.lista_data["background"]).convert()
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

        #El player del nivel y su barra de vida.
        self.barra_vida = BarraVida(self,x=10,y=10,ancho=500,alto=50,color_background=C_BLACK,color_border=C_BLUE,image_background=None,image_progress=None,value = self.lista_info.player.hp, value_max=self.lista_info.player.hp,color_vida=C_WHITE)
        self.image_vida = Widget(self,512,10,45,45,None,None,PATH_IMAGE + "Menu\heart.png",None,"Arial",None,None)

        #Lista plataformas.
        self.lista_plataformas = self.lista_info.lista_plataforma

        #Lista enemigos.
        self.lista_enemigos = self.lista_info.lista_enemigos

        #Lista frutas.
        self.fruits = self.lista_info.lista_frutas

        #Puntos.
        self.score = Widget(self,1300,0,200,50,None,None,PATH_IMAGE + "Menu/Buttons/fondo_botones.png",self.lista_info.player.puntos_player,"Arial",30,C_BLACK)
        self.puntos_totales = self.lista_info.player.puntos_player

        #Tiempo.
        self.time_juego = 60
        self.acumulador_time = 0
        self.time = Widget(self,650,0,200,50,None,None,PATH_IMAGE + "Menu/Buttons/fondo_botones.png",self.time_juego,"Arial",30,C_BLACK)
        self.image_time = Widget(self,850,5,50,50,None,None,PATH_IMAGE + "Menu/clock.png",None,"Arial",None,None)
        self.tick_1s = pygame.USEREVENT+0
        pygame.time.set_timer(self.tick_1s,1000)

        #ganó O perdió.
        self.win_lvl = self.lista_info.win
        self.win = Widget(self,ANCHO_VENTANA / 2 - 450/2,170,500,300,None,None,PATH_IMAGE + "Menu/Buttons/you win.png",None,"Arial",30,C_BLACK)

        self.lose = Widget(self,ANCHO_VENTANA / 2 - 450/2,170,500,300,None,None,PATH_IMAGE + "Menu/Buttons/you lose.png",None,"Arial",30,C_BLACK)
        
        #Lista de widgets.
        self.lista_widget = [self.time,self.score,self.image_time,self.image_vida]
        
    def draw(self):
        super().draw()
        '''
        Dibuja en el formulario el fondo.
        '''
        self.surface.blit(self.imagen_fondo,(0,0))

    def resetear(self):
        '''
        El metodo resetea el nivel, para volver a jugar.
        '''
        self.__init__(self.name,self.master,self.x,self.y,self.ancho,self.alto,self.color_border,self.active,self.image_background,self.color_background)
        
        
    def update(self,delta_ms,lista_events):
        '''
        El metodo updatea todo lo necesario para podrucir el nivel 1.
        Recibe por parametro el tiempo actual del juego y la lista de eventos.
        '''

        if not self.lista_info.win and not self.lista_info.player.muerte and self.time_juego > 0:
            
            #Información total del lvl 1.
            self.lista_info.update(delta_ms,self.master)
            
            #Widgets.
            for aux_widget in self.lista_widget:    
                aux_widget.update(lista_events)
                aux_widget.draw()
            
            #Tiempo.
            self.time._text = self.time_juego
            
            #Player y su barra de vida.
            self.lista_info.player.update(delta_ms,self.lista_plataformas,self.lista_enemigos,lista_events,self.lista_info.list_trampas)
            self.lista_info.player.draw()
            self.barra_vida.update(lista_events,self.lista_info.player.hp)
            self.barra_vida.draw()

            #Score.
            self.score._text = self.lista_info.player.puntos_player
            self.puntos_totales = self.lista_info.player.puntos_player

            #Eventos
            for event in lista_events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.set_active("pause")
                if  event.type == self.tick_1s:
                    self.time_juego -= 1

        elif self.lista_info.win:  
            self.win_lvl = True
            self.win.update(lista_events)
            self.win.draw()
            self.display_finish_lvl(delta_ms)
            self.forms_dict["levels"].condicion_lvl2 = True
                
        elif self.lista_info.player.muerte or self.time_juego <= 0:
            self.lose.update(lista_events)
            self.lose.draw()
            self.display_finish_lvl(delta_ms)

    def display_finish_lvl(self,delta_ms):
        '''
        El metodo activa segun la condicion un formulario cuando finaliza el nivel, ya sea consiguiendo el objetivo o perdiendo por muerte o tiempo y resetea el nivel.
        '''
        self.acumulador_time += delta_ms
        if self.acumulador_time >= 2000:
            
            self.set_active("levels")

            self.forms_dict["level_dos"].lista_info.player.puntos_player = self.puntos_totales

            self.resetear()
            self.acumulador_time = 0
            
            
            

       