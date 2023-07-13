import pygame
from gui_form import *
from gui_botton import *
from gui_textbox import *
from progressbar import *
from player import *

class FormOptions(Form):
    def __init__(self, name, master_surface, x, y, ancho, alto, color_border, active, image_background=None, color_background=None):
        super().__init__(name, master_surface, x, y, ancho, alto, color_border, active, image_background, color_background)

        self.sonido_fondo  = 0.7#time total de la musica

        self.on = PATH_IMAGE + "Menu/96.png"
        self.off = PATH_IMAGE + "Menu/95.png"

        self.back = Button(master=self,x=10,y=700,ancho=100,alto=80,color_background=None,color_border=None,image_background=PATH_IMAGE + "Menu/Buttons/Back.png",on_click=self.on_click_boton1,on_click_param="Menu",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        #volumen
        self.subir = Button(master=self,x=890,y=250,ancho=50,alto=50,color_background=None,color_border=None,image_background=PATH_IMAGE + "Menu/Buttons/Next.png",on_click=self.on_click_subir_vol,on_click_param="Options",text=None,font="Verdana",font_size=30,font_color=C_WHITE)
        self.bajar = Button(master=self,x=600,y=250,ancho=50,alto=50,color_background=None,color_border=None,image_background=PATH_IMAGE + "Menu/Buttons/Previous.png",on_click=self.on_click_bajar_vol,on_click_param="Options",text=None,font="Verdana",font_size=30,font_color=C_WHITE)
    
        self.pb1 = ProgressBar(master=self,x=650,y=250,ancho=240,alto=50,color_background=None,color_border=None,image_background=PATH_IMAGE + "Other/Shadow.png",image_progress=PATH_IMAGE + "Other/Confetti (16x16).png",value = 8, value_max=8)

        self.mute_desmute = Button(master=self,x=700,y=330,ancho=150,alto=50,color_background=None,color_border=None,image_background=PATH_IMAGE + "Menu/96.png",on_click=self.on_click_boton_mute_desmute,on_click_param="options",text=None,font="Verdana",font_size=30,font_color=C_WHITE)

        self.text_sound = Widget(master_form=self,x=650,y=190,ancho=240,alto=50,color_background=None,color_border=None,image_background=None,text="SOUND",font="Arial",font_size=40,font_color=C_BLACK)

        self.lista_widget = [self.back,self.subir,self.bajar,self.pb1,self.text_sound,self.mute_desmute]

    def on_click_subir_vol(self,parametro):
        '''
        El metodo sube el volumen de la barra de sonido.
        '''
        if(self.pb1.value < self.pb1.value_max and self.mute_desmute.path_image != self.off):
            self.pb1.value += 1
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
            self.sonido_fondo += 0.1
            
    def on_click_bajar_vol(self,parametro):
        '''
        El metodo baja el volumen de la barra de musica.
        '''
        if(self.pb1.value >= 0 and self.mute_desmute.path_image != self.off):
            self.pb1.value -= 1
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)
            self.sonido_fondo -= 0.1
            if(self.pb1.value <= 0):
                pygame.mixer.music.set_volume(0.0)

    def on_click_boton_mute_desmute(self,parametro):
        '''
        El metodo mutea o desmutea la musica.
        '''
        if(self.mute_desmute.path_image == self.on):
            self.mute_desmute.path_image = self.off
            pygame.mixer.music.set_volume(0.0)
            self.mute_desmute.image_background = pygame.image.load(self.off).convert()

        elif(self.mute_desmute.path_image == self.off):
            self.mute_desmute.path_image = self.on
            pygame.mixer.music.set_volume(self.sonido_fondo)
            self.mute_desmute.image_background = pygame.image.load(self.on).convert()

        self.mute_desmute.image_background = pygame.transform.scale(self.mute_desmute.image_background,(self.mute_desmute.w,self.mute_desmute.h))         

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
        

    

