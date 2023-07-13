import pygame
from constantes import *
from auxiliar import *
from player import *

class Enemigo:
    def __init__(self,x,y,speed,move_rate_ms,frame_rate_ms,screen) -> None:
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\AngryPig\Idle (36x30).png",9,1,False,1)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\AngryPig\Idle (36x30).png",9,1,True,1)
        self.hit = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\AngryPig\Hit 1 (36x30).png",5,1,False,1)
        self.frame = 0
        self.animation = self.stay_l
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_x = 0
        self.move_y = 0
        self.speed = speed
        self.direction = "R"
        self.live = True
        self.vida = 50
        self.impacto = False

        self.tiempo_colision = 0
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        self.tiempo_transcurrido_move = 0
        self.tiempo_spawn = 0
        self.tiempo_transcurrido_animation = 0
        self.tiempo_attack = 0
        self.damage_generate = 0
        self.colicion = False

        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_COLLIDE_H)
        self.rect_vision = pygame.Rect(self.rect.x - 100,self.rect.y,self.rect.w + 150,self.rect.h)
        self.rect_collition_bala_l = pygame.Rect(self.rect.x - 2,self.rect.y,self.rect.w - 70,self.rect.h)
        self.rect_collition_bala_r = pygame.Rect(self.rect.x + 20,self.rect.y,self.rect.w - 70,self.rect.h)

        self.tiempo_transcurrido = 0


    def spawn(self,direction):
        """
        El metodo posiciona de manera quieta al enemigo dependiendo la direccion.
        Recibe la direccion del enemigo.
        """
        self.tiempo_spawn = pygame.time.get_ticks() 
        self.direction = direction
        if(direction == DIRECTION_R):
            self.animation = self.stay_r
        else:
            self.animation = self.stay_l
        self.frame = 0

    def draw(self,screen):
        """
        El metodo dibuja en la pantalla los rectangulos generados en caso de ser necesario.
        Y dibuja al enemigo en la pantalla.
        """
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,255,255),rect=self.rect_vision)
            pygame.draw.rect(screen,color=(255,0,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(0,255,0),rect=self.rect_ground_collition)
            pygame.draw.rect(screen,color=(255,255,255),rect=self.rect_collition_bala_l)
            pygame.draw.rect(screen,color=(255,255,255),rect=self.rect_collition_bala_r)

        if(self.live):
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)
    
    def realizar_movimiento(self,delta_ms):
        """
        El metodo mueve el player llamando a los metodos de movimientos despues de producir el evento necesario y dependiendo el tiempo establecido.
        Recibe por parametro el tiempo actual del juego para así generar un delay en el movimiento.
        """
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

    def realizar_animacion(self,delta_ms):
        """
        El metodo va restableciendo los frames del spritesheet cada vez que llega al final del mismo.
        Recibe el tiempo actual del juego para así generar un delay en la animación del enemigo.
        """
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def update(self,delta_ms,player):
        """
        El metodo llama a los anteriores metodos para ejecutarlos de manera continua en el main de juego.
        Recibe por parametro lo necesario para cada metodo que necesite algún objeto enemigo.
        """
        self.realizar_movimiento(delta_ms)
        self.realizar_animacion(delta_ms) 

    def change_x(self,delta_x):
        """
        El metodo produce el movimiento de los rectangulos siguiendo el rectangulo del enemigo de manera horizontal.
        Recibe por parametro el delta_x que es el "speed" ingresado.
        """
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.rect_ground_collition.x += delta_x
        self.ground_collition_rect.x += delta_x
        self.rect_collition_bala_r.x += delta_x
        self.rect_collition_bala_l.x += delta_x 
 
    def change_y(self,delta_y):
        """
        El metodo produce el movimiento de los rectangulos siguiendo el rectangulo del enemigo de manera vertical.
        Recibe por parametro el delta_y.
        """
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.rect_ground_collition.y += delta_y
        self.ground_collition_rect.y += delta_y
        self.rect_collition_bala_r.y += delta_y
        self.rect_collition_bala_l.y += delta_y

    def animation_frame(self,animation):
        """
        El metodo vuelve los frame a 0 si la animación es distinta a la ingresada, o sea, en caso de cambiar la animacion con una cantidad mayor o menor de frame la vuelve a 0.
        """
        if(self.animation != animation):
            self.frame = 0
                

class EnemigoVerde(Enemigo):
    def __init__(self, x, y, speed, move_rate_ms, frame_rate_ms,screen) -> None:
        super().__init__(x, y, speed, move_rate_ms, frame_rate_ms,screen)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\AngryPig\Idle (36x30).png",9,1,False,1)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\AngryPig\Idle (36x30).png",9,1,True,1)
        self.move_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\AngryPig\Run (36x30).png",12,1,False,1)
        self.move_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\AngryPig\Run (36x30).png",12,1,True,1)
        self.hit = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\AngryPig\Hit 1 (36x30).png",5,1,False,1)
        self.spawn(DIRECTION_L)
        
        self.rect_vision = pygame.Rect(self.rect.x - 270,self.rect.y,self.rect.w + 200,self.rect.h)

    def x_move(self,delta_ms):
        """
        El metodo mueve al enemigo dependiendo la condición de manera horizontal.
        Recibe por parametro el tiempo actual del juego.
        """
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move > self.move_rate_ms ):
            self.animation_frame(self.move_l)
            self.animation = self.move_l
            self.move_x = -self.speed
            self.change_x(self.move_x)
            self.tiempo_transcurrido_move = 0
            self.tiempo_colision = 0

    def colision_vision(self,posicion_x_y,delta_ms):
        """
        El metodo detecta si el player colisiona con el rectangulo de vision del enemigo, de ser así, se porducen los eventos.
        Recibe por parametro la posicion del player y el tiempo actual del juego.
        """
        if(self.rect_vision.colliderect(posicion_x_y)):
            self.x_move(delta_ms)

    def colision_bala(self):
        """
        El metodo detecta si las balas del player colisionaron con el enemigo, produciendo el cambio de animacion y descuento de vida.
        """
        if(self.impacto):
            self.vida -= self.damage_generate
            self.animation_frame(self.hit)
            self.animation = self.hit
            self.impacto = False
            if(self.vida <= 0):
                self.live = False
    
    def update(self,delta_ms,player):
        super().update(delta_ms,player)
        """
        super().update(delta_ms,player) ver linea 99 o update del enemigo padre.
        El metodo llama al update padre y además llama al metodo de collition vision para poder producir el evento.
        """
        self.colision_vision(player.collition_rect,delta_ms)
                
class EnemigoPlanta(Enemigo):
    def __init__(self, x, y, speed, move_rate_ms, frame_rate_ms,screen) -> None:
        super().__init__(x, y, speed, move_rate_ms, frame_rate_ms,screen)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\Plant\Idle (44x42).png",11,1,False,1)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\Plant\Idle (44x42).png",11,1,True,1)
        self.attack_planta_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\Plant\Attack (44x42).png",8,1,False,1)
        self.spawn(DIRECTION_L)
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y + 20, self.rect.w / 3, GROUD_RECT_H_PLANTA)
        self.rect_vision = pygame.Rect(self.rect.x - 300,self.rect.y,self.rect.w + 400,self.rect.h + 20)
        self.tiempo_transcurrido_attack = 0
        self.direction = "L"
        self.spawn(DIRECTION_L)
        self.lista_proyectiles = ListProyectil(screen,self.rect,"Enemies\Plant\Bullet.png",self)
        self.tiempo_attack = 0 
    
    def colision_bala(self):
        if(self.impacto):
            self.vida -= self.damage_generate
            self.impacto = False
            if(self.vida <= 0):
                self.live = False

    def disparar(self,delta_ms):
        """
        El metodo genera las balas y dispara en caso de ser necesario.
        Recibe por parametro el tiempo actual del juego.
        """
        self.tiempo_attack += delta_ms
        if(self.animation == self.attack_planta_l and self.tiempo_attack >= self.frame_rate_ms + 1450):
            self.tiempo_attack = 0
            self.lista_proyectiles.generar_balas(4,self.direction,-30,10)

    def ataque(self,posicion_x_y):  
        """
        El metodo hace que el enemigo ataque en caso que el player haya colisionado con el rectangulo de vision del enemigo.
        Recibe por parametro la posicion del player para detectar dicha condicion de ataque.
        """
        if self.rect_vision.colliderect(posicion_x_y):
            self.animation_frame(self.attack_planta_l)
            self.animation = self.attack_planta_l 
        else:
            self.animation_frame(self.stay_l)
            self.animation = self.stay_l
            
    def update(self,delta_ms,player):
        super().update(delta_ms,player)
        """
        super().update(delta_ms,player) ver linea 99 o el metodo update de class Enemigo.
        El metodo llama al update padre y además llama al metodo de collition vision para poder producir el evento.
        Llama al metodo disparar y hace el updatea a la lista de proyectiles.
        """
        self.ataque(player.collition_rect) 
        self.lista_proyectiles.update([player])
        self.disparar(delta_ms)
    
        
class EnemigoFantasma(Enemigo):
    def __init__(self, x, y, speed, move_rate_ms, frame_rate_ms, screen) -> None:
        super().__init__(x, y, speed, move_rate_ms, frame_rate_ms, screen)

        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\Ghost\Desappear (44x30).png",4,1,False,1)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\Ghost\Desappear (44x30).png",4,1,True,1)
        self.hit = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\Ghost\Hit (44x30).png",5,1,True,1)
        self.attack_ghost = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\Ghost\Idle (44x30).png",10,1,True,1)
        self.spawn(DIRECTION_R)
        self.rect_collition_bala_l = pygame.Rect(self.rect.x - 2,self.rect.y,self.rect.w - 65,self.rect.h)

        self.rect_vision = pygame.Rect(self.rect.x + 50,self.rect.y,self.rect.w + 300,self.rect.h + 20)
        self.lista_proyectiles = ListProyectil(screen,self.rect,"Enemies\Plant\Bullet.png",self)

    def colision_bala(self):
        if(self.impacto):
            self.vida -= self.damage_generate
            self.animation_frame(self.hit)
            self.animation = self.hit
            self.impacto = False
            if(self.vida <= 0):
                self.live = False

    def disparar(self,delta_ms):
        self.tiempo_attack += delta_ms
        if(self.animation == self.attack_ghost and self.tiempo_attack >= self.frame_rate_ms + 1450):
            self.tiempo_attack = 0
            self.lista_proyectiles.generar_balas(4,self.direction,10,10)

    def ataque(self,posicion_x_y):  
        if self.rect_vision.colliderect(posicion_x_y):
            self.animation_frame(self.attack_ghost)
            self.animation = self.attack_ghost 
        else:
            self.animation_frame(self.stay_r)
            self.animation = self.stay_r
        
    def update(self, delta_ms,player):
        super().update(delta_ms,player)
        self.lista_proyectiles.update([player])
        self.ataque(player.collition_rect)
        self.disparar(delta_ms)

class EnemigoRino(Enemigo):
    def __init__(self, x, y, speed, move_rate_ms, frame_rate_ms, screen) -> None:
        super().__init__(x, y, speed, move_rate_ms, frame_rate_ms, screen)

        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\Rino\Idle (52x34).png",11,1,False,1)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\Rino\Idle (52x34).png",11,1,True,1)  
        self.move_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\Rino\Run (52x34).png",6,1,False,1)
        self.move_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\Rino\Run (52x34).png",6,1,True,1)
        self.hit = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Enemies\Rino\Hit (52x34).png",5,1,False,1)
        self.spawn(DIRECTION_L)
        
        self.rect_vision = pygame.Rect(self.rect.x - 150,self.rect.y,self.rect.w - 400,self.rect.h)

    def colision_bala(self):
        if(self.impacto):
            self.vida -= self.damage_generate
            self.animation_frame(self.hit)
            self.animation = self.hit
            self.impacto = False
            if(self.vida <= 0):
                self.live = False

    def x_move(self,delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move > self.move_rate_ms):
            self.animation_frame(self.move_l)
            self.animation = self.move_l
            self.move_x = -self.speed
            self.change_x(self.move_x)
            self.tiempo_transcurrido_move = 0
            self.tiempo_colision = 0
    
    def colision_vision(self,posicion_x_y,delta_ms):
        if(self.rect_vision.colliderect(posicion_x_y)):
            self.x_move(delta_ms)

    def update(self, delta_ms,player):
        super().update(delta_ms,player)
        self.colision_vision(player,delta_ms)
        