import pygame
from gui_form import *
from gui_textbox import *
from gui_botton import *
import sqlite3 as sql
from controller import *

class FormTextName(Form):
    def __init__(self, name, master_surface, x, y, ancho, alto, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_surface, x, y, ancho, alto, color_border, active, image_background, color_background)

        self.nombre_viajar = ""
        self.nivel_actual = ""
        self.puntos_totales = 0

        self.name_player = TextBox(master=self,x=ANCHO_VENTANA / 2 - 200 / 2,y=250,ancho=200,alto=100,color_background=None,color_border=None,image_background=PATH_IMAGE + "Menu/Buttons/table.png",text="Player",font="Arial",font_size=20,font_color=(0,0,0))

        self.ranking = Button(master=self,x=880,y=250,ancho=150,alto=70,color_background=None,color_border=None,image_background=PATH_IMAGE + "Menu/btn.png",on_click=self.on_click_boton1,on_click_param="ranking",text=None,font="Verdana",font_size=14,font_color=C_BLACK)

        self.lista_widget = [self.ranking,self.name_player]

    def on_click_boton1(self, parametro):
        self.nombre_viajar = self.name_player._text
        
        self.set_active(parametro)

    def update(self,lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

        self.agregar_info_sql()

    def draw(self): 
        super().draw()
        self.surface.blit(self.image_background,self.image_background_rect)
        for aux_boton in self.lista_widget:    
            aux_boton.draw()
    
    def agregar_info_sql(self):
        '''
        El metodo inserta el nombre y puntos del jugador a la base de datos.
        '''
        self.nombre = self.nombre_viajar
        if(self.nombre != ""):
            insertRow(self.nombre,self.puntos_totales)
            self.nombre = ""
            self.nombre_viajar = ""
            self.name_player._text = "Player"

        