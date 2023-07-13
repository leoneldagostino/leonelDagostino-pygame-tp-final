import pygame
from gui_form import *
from gui_botton import *
from gui_textbox import *
from constantes import *

class FormClasificaciones(Form):
    def __init__(self, name, master_surface, x, y, ancho, alto, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_surface, x, y, ancho, alto, color_border, active, image_background, color_background)

        self.text_ranking = Widget(self,ANCHO_VENTANA/2 - 400/ 2,100,400,150,None,None,PATH_IMAGE + "Menu/Banner04.png","RANKING","Arial",40,C_BLACK,)

        # self.rank_level_one = Button(master=self,x=ANCHO_VENTANA/2 - 150/ 2,y=250,w=150,h=60,color_background=None,color_border=None,image_background=PATH_IMAGE + "Menu/Buttons/fondo_botones.png",on_click=self.on_click_boton1,on_click_param="nivel_uno",text="",font="Verdana",font_size=24,font_color=C_BLACK)

        self.ranking_final = Button(master=self,x=ANCHO_VENTANA/2 - 150/ 2,y=350,ancho=150,alto=60,color_background=None,color_border=None,
        image_background=PATH_IMAGE + "Menu/Buttons/fondo_botones.png",on_click=self.on_click_boton1,on_click_param="nivel_uno",text="RANKING",font="Verdana",font_size=24,font_color=C_BLACK)

        # self.rank_level_tres = Button(master=self,x=ANCHO_VENTANA/2 - 150/ 2,y=450,w=150,h=60,color_background=None,color_border=None,
        # image_background=PATH_IMAGE + "Menu/Buttons/fondo_botones.png",on_click=self.on_click_boton1,on_click_param="nivel_tres",text="NIVEL TRES",font="Verdana",font_size=24,font_color=C_BLACK)

        self.back = Button(master=self,x=10,y=700,ancho=100,alto=80,color_background=None,color_border=None,image_background=PATH_IMAGE + "Menu/Buttons/Back.png",on_click=self.on_click_boton1,on_click_param="Menu",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        self.lista_widget = [self.ranking_final,self.back,self.text_ranking]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        self.surface.blit(self.image_background,self.image_background_rect)
        for aux_boton in self.lista_widget:    
            aux_boton.draw()