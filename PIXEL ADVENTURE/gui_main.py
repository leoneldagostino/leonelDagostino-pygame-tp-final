import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form import *

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

while True:
    lista_events = pygame.event.get()

    for event in lista_events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

    delta_ms = clock.tick(FPS)

    pygame.display.flip()   