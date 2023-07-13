import pygame
from gui_widget import Widget
from constantes import *

class BarraVida(Widget):
    def __init__(self,master,x=0,y=0,ancho=200,alto=50,color_background=C_GREEN,color_border=C_RED,image_background=None,color_vida=C_WHITE,image_progress=None,value=1,value_max=5):
        super().__init__(master,x,y,ancho,alto,color_background,color_border,image_background,None,None,None,None)

        self.color_vida = color_vida
        self.barra = pygame.Rect(0,0,ancho,alto)
        
        self.value_min = 0
        self.value = value_max
        self.value_max=value_max
        
    def render_vida(self,player_hp):
        super().render()
        '''
        El metodo genera la barra de vida del player y la actualiza dependiendo la vida.
        Recibe por parametro la vida actual del player.
        '''
        self.barra.w = player_hp * self.w / self.value_max
        self.slave_surface.fill(self.color_vida,self.barra)
        
    def update(self,lista_eventos,player_hp):
        self.render_vida(player_hp)  

    

