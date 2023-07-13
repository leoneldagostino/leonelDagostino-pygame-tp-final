import pygame
from pygame.locals import *
from gui_widget import Widget
from constantes import *

class Form:
    forms_dict = {}
    def __init__(self,name,master_surface,x,y,ancho,alto,color_border,active,image_background=None,color_background=None):
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color_background = color_background
        self.color_border = color_border
        self.image = image_background

        self.surface = pygame.Surface((ancho,alto))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        self.x = x
        self.y = y

        if(self.color_background != None):
            self.surface.fill(self.color_background)
        
        if(self.image != None):
            self.image_background = pygame.image.load(PATH_IMAGE + self.image).convert()
            self.image_background = pygame.transform.scale(self.image_background,(self.ancho,self.alto))
            self.image_background_rect = self.image_background.get_rect()

    def set_active(self,name):
        '''
        El metodo activa el formulario dependiendo el nombre que ingrese por parametro.
        Recibe por parametro el nombre del formulario.
        '''
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True

    def render(self):
        pass

    def update(self,lista_eventos):
        pass

    def draw(self):
        '''
        Blitea el formulario en el scren cuando está activo.
        '''
        self.master_surface.blit(self.surface,self.slave_rect)
        
