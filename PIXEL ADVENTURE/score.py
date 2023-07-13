import pygame
from auxiliar import *
from constantes import *

class Text:
    def __init__(self,x,y,text,color_text,screen) -> None:
        self.x = x
        self.y = y
        self.text = text
        self.screen = screen
        self.font = pygame.font.SysFont("Pacifico, cursive",30)
        self.color_text = color_text
        self.text_image = self.font.render(self.text, True,self.color_text)
        self.text_image_rect = self.text_image.get_rect(centerx = self.x,centery = self.y, h = 100 ,w = 100)

    def draw(self):
        self.screen.blit(self.text_image,self.text_image_rect)
    
        
    



