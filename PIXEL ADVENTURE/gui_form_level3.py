import pygame
from gui_form import *
from constantes import *
from player import *
from plataforma import *
from score import *
from gui_barravida import *
from info_levels import *
from gui_textbox import *

class LevelTres(Form):
    def __init__(self, name, master_form, x, y, ancho, alto, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_form, x, y, ancho, alto, color_border, active, image_background, color_background)

        self.master_form = master_form
        self.name = name
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color_border = color_border
        self.active = active
        self.image_background = image_background
        self.color_background = color_background


        #Información del nivel 3.
        self.lista_info = Datalevels(master_form,"level_tres")
        
        #Imagen de fondo del nivel.
        self.imagen_fondo = pygame.image.load(PATH_IMAGE + self.lista_info.lista_data ["background"]).convert()
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

        #Barra de vida del player.
        self.barra_vida = BarraVida(self,x=10,y=10,ancho=500,alto=50,color_background=C_BLACK,color_border=C_BLUE,image_background=None,image_progress=None,value = self.lista_info.player.hp, value_max=self.lista_info.player.hp,color_vida=C_WHITE)
        self.image_vida = Widget(self,512,10,45,45,None,None,PATH_IMAGE + "Menu/heart.png",None,"Arial",None,None)
        
        #Tiempo juego.
        self.acumulador_time = 0
        self.time_juego = 60
        self.time = Widget(self,650,0,200,50,None,None,PATH_IMAGE + "Menu/Buttons/fondo_botones.png",self.time_juego,"Arial",30,C_BLACK)
        self.tick_1s = pygame.USEREVENT+0
        pygame.time.set_timer(self.tick_1s,1000)
        self.image_time = Widget(self,850,5,50,50,None,None,PATH_IMAGE + "Menu/clock.png",None,"Arial",None,None)

        #Puntos.
        self.score = Widget(self,1300,0,200,50,None,None,PATH_IMAGE + "Menu/Buttons/fondo_botones.png",self.lista_info.player.puntos_player,"Arial",30,C_BLACK)
        self.puntos_totales = self.lista_info.player.puntos_player

        #Display WIN O LOSE.
        self.win_lvl3 = self.lista_info.win
        self.win = Widget(self,ANCHO_VENTANA / 2 - 450/2,150,500,300,None,None,PATH_IMAGE + "Menu/Buttons/you win.png",None,"Arial",30,C_BLACK)
        self.lose = Widget(self,ANCHO_VENTANA / 2 - 450/2,170,500,300,None,None,PATH_IMAGE + "Menu/Buttons/you lose.png",None,"Arial",30,C_BLACK)

        #Listas.
        self.lista_widget = [self.time,self.score,self.image_time,self.image_vida]

        self.lista_fruits = self.lista_info.lista_frutas

        self.lista_plataformas = self.lista_info.lista_plataforma

        self.lista_enemigos = self.lista_info.lista_enemigos

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
        self.__init__(self.name,self.master_form,self.x,self.y,self.ancho,self.alto,self.color_border,self.active,self.image_background,self.color_background)    

    def update(self,delta_ms,lista_events):
        '''
        El metodo updatea todo lo necesario para podrucir el nivel 2.
        Recibe por parametro el tiempo actual del juego y la lista de eventos.
        '''

        if not self.lista_info.win and not self.lista_info.player.muerte and self.time_juego > 0:
            
            #Información total del lvl 3.
            self.lista_info.update(delta_ms,self.master_form)

            #Widgets.
            for aux_boton in self.lista_widget: 
                aux_boton.update(lista_events)   
                aux_boton.draw()

            #Puntos.
            self.score.update(lista_events)
            self.score._text = self.lista_info.player.puntos_player  #Cada vez que ingrese al update va a ir modificando el texto del widget score por medio de su metodo render.
            self.puntos_totales = self.lista_info.player.puntos_player

            #Tiempo.
            self.time.update(lista_events)
            self.time._text = self.time_juego
            
            #Player_dos y su barra de vida
            self.lista_info.player.update(delta_ms,self.lista_plataformas,self.lista_enemigos,lista_events,self.lista_info.list_trampas)
            self.lista_info.player.draw()
            self.barra_vida.update(lista_events,self.lista_info.player.hp)
            self.barra_vida.draw()

        if self.lista_info.win:
            self.win_lvl3 = True
            self.win.update(lista_events)
            self.win.draw()
            self.display_finish_lvl(delta_ms)

        elif self.lista_info.player.muerte or self.time_juego <= 0:
            self.lose.update(lista_events)
            self.lose.draw()
            self.display_finish_lvl(delta_ms)

        for event in lista_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.set_active("pause")
            if event.type == self.tick_1s:
                self.time_juego -= 1

    def display_finish_lvl(self,delta_ms):
        '''
        El metodo activa segun la condicion un formulario cuando finaliza el nivel, ya sea consiguiendo el objetivo o perdiendo por muerte o tiempo y resetea el nivel.
        '''
        self.acumulador_time += delta_ms
        if self.acumulador_time >= 2000:
            self.set_active("name_player")
            self.forms_dict["name_player"].puntos_totales = self.puntos_totales
            self.resetear()
            self.acumulador_time = 0
        