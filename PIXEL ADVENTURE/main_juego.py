#json se llama nivel, en ese nivel el player,enemigo,posicion,obstaculos.
import pygame
from pygame.locals import *
import sys
from constantes import *
from cargar_json import *
from gui_form_level1 import *
from gui_form_menu import *
from gui_menu_options import *
from gui_form_lvls import *
from gui_form_level2 import *
from gui_from_pause import *
from gui_ranking import *
from gui_form_level3 import *
from gui_form_name import *
from controller import *
from gui_form_rankings import *

pygame.init()
pygame.mixer.music.load("PIXEL ADVENTURE\Recursos\music\musica_fondo.wav")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
clock = pygame.time.Clock()
imagen_fondo = pygame.image.load(PATH_IMAGE + "fondo/game_background.png").convert()
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

level_uno = LevelUno("level_uno",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,C_BLACK,False,image_background=None,color_background=None)
    
menu = FormMenu("Menu",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,(0,0,0),True,image_background= "fondo\game_background.png",color_background=None)
options = FormOptions("Options",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,(0,0,0),False,image_background="fondo\game_background.png",color_background=None)
levels = FormLevels("levels",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,(0,0,0),False,image_background="fondo\game_background.png",color_background=None)
level_dos = LevelDos("level_dos",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,(0,0,0),False,"fondo\game_background.png",color_background=None)
juego_pause = FormPauseLvl("pause",screen,ANCHO_VENTANA / 2 - 400 / 2,100,400,450,None,False,image_background="Menu\Buttons\/bg.png",color_background=None)
ranking1 = FormRanking("nivel_uno",screen,550,100,400,600,None,False,"Menu\Buttons\/table.png",None)
level_tres = LevelTres("level_tres",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,(0,0,0),False,"fondo\game_background.png",None)
form_name_player = FormTextName("name_player",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,False,"fondo\game_background.png",None)
form_clasifiaciones = FormClasificaciones("ranking",screen,0,0,ANCHO_VENTANA,ALTO_VENTANA,None,False,"fondo\game_background.png",None)

while True:
    lista_events = pygame.event.get()   
    for event in lista_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    delta_ms = clock.tick(FPS)

    if menu.active:        
        menu.update(lista_events)
        menu.draw()

    elif options.active:
        options.update(lista_events)
        options.draw()

    elif juego_pause.active:
        juego_pause.update(lista_events)
        juego_pause.draw()

    elif levels.active:
        levels.update(lista_events)
        levels.draw()

    elif level_uno.active:
        level_uno.draw()
        level_uno.update(delta_ms,lista_events)
        
    elif level_dos.active:
        level_dos.draw()
        level_dos.update(delta_ms,lista_events)
    
    elif level_tres.active:
        level_tres.draw()
        level_tres.update(delta_ms,lista_events)

    elif form_name_player.active and not level_tres.win_lvl3 or level_tres.win_lvl3:
        form_name_player.update(lista_events)
        form_name_player.draw()

    elif form_clasifiaciones.active:
        form_clasifiaciones.update(lista_events)
        form_clasifiaciones.draw()

    elif ranking1.active:
        ranking1.update(lista_events)

    pygame.display.flip()  