import pygame
from constantes import *
from cargar_json import *
from enemigo import *
from plataforma import *
from varios import *
from proyectil import *
from score import *
from trampas import *

class Datalevels:
    def __init__(self,screen,lvl) -> None:   
        self.lvl = lvl     
        self.lista_data = cargar_json_data("PIXEL ADVENTURE/levels.json")[0][self.lvl]
        self.screen = screen
        self.player = Player(100,540,10,10,50,10,15,10,screen)
        self.lista_enemigos = []
        self.lista_plataforma = []
        self.lista_frutas = []
        self.list_trampas = []
        self.crear_enemigos()
        self.create_trampas()
        self.crear_plataformas()
        self.crear_frutas()
        self.win = False

    def crear_enemigos(self):
        '''
        El metodo crea la lista de enemigos para cada nivel desde la información exportada del json.
        '''
        for enemigo in self.lista_data["enemigos"]:
            if self.lvl == "level_uno":
                if enemigo["name"] == "chancho":
                    for i in range(enemigo["amount"]):
                        self.lista_enemigos.append(EnemigoVerde(enemigo["position_x"][i],enemigo["position_y"][i],enemigo["speed"][i],50,50,self.screen))
                if enemigo["name"] == "planta":
                    for i in range(enemigo["amount"]):
                        self.lista_enemigos.append(EnemigoPlanta(enemigo["position_x"][i],enemigo["position_y"][i],enemigo["speed"][i],50,50,self.screen))

            elif self.lvl == "level_dos":           
                if enemigo["name"] == "ghost":
                    for i in range(enemigo["amount"]):
                        self.lista_enemigos.append(EnemigoFantasma(enemigo["position_x"][i],enemigo["position_y"][i],enemigo["speed"][i],50,50,self.screen))
                if enemigo["name"] == "rino":
                    for i in range(enemigo["amount"]):
                        self.lista_enemigos.append(EnemigoRino(enemigo["position_x"][i],enemigo["position_y"][i],enemigo["speed"][i],50,50,self.screen))

            elif self.lvl == "level_tres":
                if enemigo["name"] == "ghost":  
                    for i in range(enemigo["amount"]):
                        self.lista_enemigos.append(EnemigoFantasma(enemigo["position_x"][i],enemigo["position_y"][i],enemigo["speed"][i],50,50,self.screen))
                if enemigo["name"] == "planta":
                    for i in range(enemigo["amount"]):
                        self.lista_enemigos.append(EnemigoPlanta(enemigo["position_x"][i],enemigo["position_y"][i],enemigo["speed"][i],50,50,self.screen))

    def crear_plataformas(self):
        '''
        El metodo crea la lista de plataformas para cada nivel desde la información exportada del json.
        '''
        for plataforma in self.lista_data["plataformas"]:
            if plataforma["name"] == "left_wall":
                for i in range(plataforma["amount"]):
                    self.lista_plataforma.append(Platform(plataforma["position_x"],plataforma["position_y"][i],plataforma["width"],plataforma["speed"],plataforma["height"],50,0,0,0,4,0))
            
            if plataforma["name"] == "right_wall":
                for i in range(plataforma["amount"]):
                    self.lista_plataforma.append(Platform(plataforma["position_x"],plataforma["position_y"][i],plataforma["width"],plataforma["speed"],plataforma["height"],50,0,0,0,4,0))

            elif plataforma["name"] == "flat":
                for i in range(plataforma["amount"]):
                    self.lista_plataforma.append(Platform(plataforma["position_x"][i],plataforma["position_y"],plataforma["width"],plataforma["speed"],plataforma["height"],50,0,0,0,1,0))
            
            elif plataforma["name"] == "some":
                for i in range(plataforma["amount"]):
                    self.lista_plataforma.append(Platform(plataforma["position_x"][i],plataforma["position_y"][i],plataforma["width"],plataforma["speed"],plataforma["height"],50,0,0,0,plataforma["type"][i],0))
            
            elif plataforma["name"] == "movable":
                for i in range(plataforma["amount"]):
                    self.lista_plataforma.append(Platform(plataforma["position_x"][i],plataforma["position_y"][i],plataforma["width"],plataforma["speed"][i],plataforma["height"],50,plataforma["point_move_l"][i],plataforma["point_move_r"][i],plataforma["speed_up_down"],plataforma["type"][i],plataforma["punto_volver_plat_up"][i]))

    def crear_frutas(self):
        '''
        El metodo crea la lista de frutas para cada nivel desde la información exportada del json.
        '''
        self.win = False
        for fruit in self.lista_data["frutas"]:
            if fruit["name"] == "apple":
                for i in range(fruit["amount"]):
                    self.lista_frutas.append(Fruta(fruit["position_x"][i],fruit["position_y"][i],50,fruit["speed"]))
            if fruit["name"] == "apple_movable":
                for i in range(fruit["amount"]):
                    self.lista_frutas.append(Fruta(fruit["position_x"][i],fruit["position_y"][i],50,fruit["speed"][i]))

    def create_trampas(self):
        '''
        El metodo crea la lista de trampas para cada nivel desde la información exportada del json.
        '''
        for trampa in self.lista_data["trampas"]:
            if trampa["name"] == "cierra":
                for i in range(trampa["amount"]):
                    self.list_trampas.append(Trampa(trampa["position_x"][i],trampa["position_y"][i],50,self.screen))

    def update(self,delta_ms,screen):
        '''
        Updatea y dibuja las trampas, plataformas,enemigos y frutas.
        Recibe por parametro el tiempo actual del juego y la pantalla.
        '''
        for trampa in self.list_trampas:
            trampa.update(delta_ms)
            trampa.draw()

        for plataforma in self.lista_plataforma:
            plataforma.update(delta_ms)
            plataforma.draw(self.screen)
        
        for enemy in self.lista_enemigos:
            enemy.update(delta_ms,self.player)
            enemy.draw(self.screen)
            if(not enemy.live):
                self.lista_enemigos.remove(enemy)
                self.player.puntos_player = self.player.puntos_player + 50

        for fruit in self.lista_frutas:
            fruit.update(delta_ms,self.lista_plataforma,self.player.collition_rect)
            fruit.draw(screen)    
            if(fruit.collision):
                self.player.puntos_player = self.player.puntos_player + 50
                self.lista_frutas.remove(fruit)

            if(len(self.lista_frutas) <= 0):
                self.win = True 
        

        