import pygame
from gui_form import *
from gui_botton import *
from gui_textbox import *
import sqlite3 as sql
from controller import *

class FormRanking(Form):
    def __init__(self, name, master_surface, x, y, ancho, alto, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_surface, x, y, ancho, alto, color_border, active, image_background, color_background)

        self.data_player = readRows()
        self.name = name
        self.lista_widgets_puntos = []   
        self.lista_widgets_name = []
        self.eje_y = 120              

        for i in range(len(self.data_player)):
            self.lista_widgets_name.append(Widget(master_form=self,x=60,y=self.eje_y,ancho=160,alto=65,color_background=None,color_border=None,image_background=PATH_IMAGE + "Menu/table_2.png",text= self.data_player[i][1],font="Arial",font_size=40,font_color=C_BLACK))

            self.lista_widgets_puntos.append(Widget(master_form=self,x=240,y=self.eje_y,ancho=100,alto=65,color_background=None,color_border=None,image_background=PATH_IMAGE + "Menu/table_2.png",text= self.data_player[i][2],font="Arial",font_size=40,font_color=C_BLACK))
            self.eje_y += 70

        self.boton_name_ranking = Widget(master_form=self,x=150,y=20,ancho=100,alto=150,color_background=None,color_border=None,image_background=None,text= "Score",font="Arial",font_size=40,font_color=C_BLACK)
        
        self.boton_atras = Button(master=self,x=0,y=500,ancho=100,alto=80,color_background=None,color_border=None,image_background=PATH_IMAGE + "Menu/Buttons/Back.png",on_click=self.on_click_boton1,on_click_param="ranking",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        self.lista_widget = [self.boton_name_ranking,self.boton_atras]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    
    def update(self,lista_eventos):
        self.updatear_ranking(lista_eventos)
        self.draw()

    def draw(self): 
        super().draw()
        self.surface.blit(self.image_background,self.image_background_rect)
        for widget_name in self.lista_widgets_name:    
            widget_name.draw()
        for aux in self.lista_widget:
            aux.draw()
        for widget_puntos in self.lista_widgets_puntos:
            widget_puntos.draw()
        
    def updatear_ranking(self,lista_eventos):
        '''
        El metodo va manteniendo constantemente la información de la base de datos, sin necesidad de salir para mostrar los puntos finales.
        Recibe por parametro la lista de eventos.
        '''
        self.data_player = readRows()

        for i in range(len(self.lista_widgets_name)):
            self.lista_widgets_name[i]._text = self.data_player[i][1]

            self.lista_widgets_puntos[i]._text = self.data_player[i][2]

        for widget_name in self.lista_widgets_name:
            widget_name.update(lista_eventos)
        for widget_puntos in self.lista_widgets_puntos:
            widget_puntos.update(lista_eventos)
        for aux in self.lista_widget:
            aux.update(lista_eventos)
    

