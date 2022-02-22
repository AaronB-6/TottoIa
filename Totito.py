import random
import pygame
from copy import deepcopy

#Reward
#Play -> Posicion
#Game Iteration
#If lose

class Jugador:
    
    def __init__(self):
        self.puntos = 0
        self.figura = ""
        self.str = 2
        self.turno = False
    
    def get_Puntos(self):
        return self.puntos

    def set_Puntos(self,puntos):
        self.puntos = puntos
    
    def get_Figura(self):
        return self.figura
        
    def set_Figura(self,figura):
        self.figura = figura

    def get_Turno(self):
        return self.turno
        
    def set_Turno(self,turno):
        self.turno = turno

    def get_Str(self):
        return self.str
    
    def set_Str(self,str):
        self.str = str

Screen = True
Contador = 1
Matrix = [[10,11,12],[13,14,15],[16,17,18]]
pygame.init()

Player1 = Jugador()
Player1.set_Figura("equis.png")
Player1.set_Str(1)
Player1.set_Turno(True)
Player2 = Jugador()
Player2.set_Figura("Circulo.png")
Player2.set_Str(0)
Player2.set_Turno(False)

# Tamaño en pantalla
HEIGHT_SCREEN = 600
WIDTH_SCREEN = 800
# Color
WHITE = (255,255,255,)
BLACK = (0,0,0)

display_surface = pygame.display.set_mode((WIDTH_SCREEN,HEIGHT_SCREEN))

def main():
    global Screen,Matrix,Contador

    display_surface.fill(WHITE)
    #Dibujar lineas
    #primera linea horizontal
    pygame.draw.line(display_surface,BLACK,(140,200),(WIDTH_SCREEN-140,200),10)
    #primera linea vertical
    pygame.draw.line(display_surface,BLACK,(300,50),(300,HEIGHT_SCREEN-50),10)
    #segunda linea horizontal
    pygame.draw.line(display_surface,BLACK,(140,400),(WIDTH_SCREEN-140,400),10)
    #segunda linea vertical
    pygame.draw.line(display_surface,BLACK,(500,50),(500,HEIGHT_SCREEN-50),10)

    #Icono
    Icon = pygame.image.load("Logo.png")
    Icon = pygame.transform.scale(Icon,(70,50))
    pygame.display.set_icon(Icon)
    pygame.display.set_caption("Totito")

    #Texto
    letras = pygame.font.SysFont("calibri",32)
    letras_custom = pygame.font.Font("broadway.ttf",32)


    #definir texto 
    texto1 = letras.render("Player1 score:"+str(Player1.get_Puntos())+"",True,BLACK)
    texto1_object = texto1.get_rect()
    texto1_object.x = 0
    texto1_object.y = 0
    texto2 = letras.render("Player2 score:"+str(Player2.get_Puntos())+"",True,BLACK)
    texto2_object = texto2.get_rect()
    texto2_object.x = 600
    texto2_object.y = 0

    display_surface.blit(texto1,texto1_object)
    display_surface.blit(texto2,texto2_object)
    
    while Screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Screen = False
            
            if Player1.get_Turno():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] > 140 and event.pos[0] < 660 and event.pos[1] > 50 and event.pos[1] < 550:
                        if WhosPlaying(event):
                            Player1.set_Turno(True)
                            Player2.set_Turno(False)
                            Contador = 1
                            Matrix = [[10,11,12],[13,14,15],[16,17,18]]
                            main()
            else:
                if IaTurno():
                            Player1.set_Turno(True)
                            Player2.set_Turno(False)
                            Contador = 1
                            Matrix = [[10,11,12],[13,14,15],[16,17,18]]
                            main()

        pygame.display.update()

def WhosPlaying(event):
    global Player1,Player2,Contador
    if Contador == 9:
        return True
    if SeleccionarCuadro(CrearFigura(Player1),event) == False: return False
    if CheckWin() == False:
        Player1.set_Puntos(Player1.get_Puntos()+1)
        return True
    Player1.set_Turno(False)
    Player2.set_Turno(True)
    Contador = Contador +1    
        
def IaTurno():
    global Player1,Player2,Contador
    if Contador == 9:
        return True
    if SeleccionarIA(CrearFigura(Player2)) == False: return False
    if CheckWin() == False:
        Player2.set_Puntos(Player2.get_Puntos()+1)
        return True
    Player2.set_Turno(False)
    Player1.set_Turno(True)
    Contador = Contador +1 

def CrearFigura(Player):
    Figura = pygame.image.load(Player.get_Figura())
    Figura = pygame.transform.scale(Figura,(50,50))
    Figura_Object = Figura.get_rect()
    return Figura,Figura_Object,Player.get_Str()

def SeleccionarCuadro(Seleccion,event):
    #Primer cuadro
    if (event.pos[0] > 140 and event.pos[0] < 300 ) and (event.pos[1] > 50 and event.pos[1] < 200 ) :
        if Matrix[0][0] == 1 or Matrix[0][0] == 0 :
            return False
        else:
            Seleccion[1].x = 160+30
            Seleccion[1].y = 100 
            display_surface.blit(Seleccion[0], Seleccion[1])
            Matrix[0][0] = Seleccion[2]
        
    #Segundo Cuadro
    if (event.pos[0] > 300 and event.pos[0] < 500 ) and (event.pos[1] > 50 and event.pos[1] < 200 ) :
        if Matrix[0][1] == 1 or Matrix[0][1] == 0 :
            return False
        else:
            Seleccion[1].x = 300+75
            Seleccion[1].y = 100 
            display_surface.blit(Seleccion[0], Seleccion[1])
            Matrix[0][1] = Seleccion[2]
    #Tercer Cuadro
    if (event.pos[0] > 500 and event.pos[0] < WIDTH_SCREEN-140 ) and (event.pos[1] > 50 and event.pos[1] < 200 ) :
        if Matrix[0][2] == 1  or Matrix[0][2] == 0 :
            return False
        else:
            Seleccion[1].x = 500+60
            Seleccion[1].y = 100 
            display_surface.blit(Seleccion[0], Seleccion[1])
            Matrix[0][2] = Seleccion[2]

    #Cuarto
    if (event.pos[0] > 140 and event.pos[0] < 300 ) and (event.pos[1] > 200 and event.pos[1] < 400 ) :
        if Matrix[1][0] == 1 or Matrix[1][0] == 0 :
            return False
        else:
            Seleccion[1].x = 160+30
            Seleccion[1].y = 275 
            display_surface.blit(Seleccion[0], Seleccion[1])
            Matrix[1][0] = Seleccion[2]
    #Quinto
    if (event.pos[0] > 300 and event.pos[0] < (WIDTH_SCREEN-140-160)) and (event.pos[1] > 200 and event.pos[1] < (HEIGHT_SCREEN-200)):
        if Matrix[1][1] == 1 or Matrix[1][1] == 0 :
            return False
        else:
            Seleccion[1].centerx = WIDTH_SCREEN/2
            Seleccion[1].centery = HEIGHT_SCREEN/2
            display_surface.blit(Seleccion[0], Seleccion[1])
            Matrix[1][1] = Seleccion[2]
    #Sexto
    if (event.pos[0] > 500 and event.pos[0] < 660 ) and (event.pos[1] > 200 and event.pos[1] < 400 ) :
        if Matrix[1][2] == 1 or Matrix[1][2] == 0 :
            return False
        else:
            Seleccion[1].x = 500+60
            Seleccion[1].y = 275
            display_surface.blit(Seleccion[0], Seleccion[1])
            Matrix[1][2] = Seleccion[2]

    #Septimo cuadro
    if (event.pos[0] > 140 and event.pos[0] < 300 ) and (event.pos[1] > 400 and event.pos[1] < 550 ) :
        if Matrix[2][0] == 1 or Matrix[2][0] == 0 :
            return False
        else:
            Seleccion[1].x = 160+30
            Seleccion[1].y = 455 
            display_surface.blit(Seleccion[0], Seleccion[1])
            Matrix[2][0] = Seleccion[2]
    #Octavo Cuadro
    if (event.pos[0] > 300 and event.pos[0] < 500 ) and (event.pos[1] > 400 and event.pos[1] < 550 ) :
        if Matrix[2][1] == 1 or Matrix[2][1] == 0 :
            return False
        else:
            Seleccion[1].x = 300+75
            Seleccion[1].y = 455  
            display_surface.blit(Seleccion[0], Seleccion[1])
            Matrix[2][1] = Seleccion[2]
    #Noveno Cuadro
    if (event.pos[0] > 500 and event.pos[0] < WIDTH_SCREEN-140 ) and (event.pos[1] > 400 and event.pos[1] < 550 ) :
        if Matrix[2][2] == 1 or Matrix[2][2] == 0 :
            return False
        else:
            Seleccion[1].x = 500+60
            Seleccion[1].y = 455  
            display_surface.blit(Seleccion[0], Seleccion[1])
            Matrix[2][2] = Seleccion[2]
            
def SeleccionarIA(Seleccion):
     
    Libres = []
    for i in range(len(Matrix)):
        for x in range(len(Matrix)):
            if Matrix[i][x] != 0 and Matrix[i][x] != 1:
                    Libres.append( (i,x) )

    rand = random.choice(Libres)
    

    if posiblemovement(Seleccion):
        return True
    else:

        if  Matrix[1][1] == 0 or Matrix[1][1] == 1:
            

            if Matrix[rand[0]][rand[1]] == 0 or Matrix[rand[0]][rand[1]] == 1:
                return False
            else:
                randomMove(Seleccion,rand)
        else:
             Seleccion[1].centerx = WIDTH_SCREEN/2
             Seleccion[1].centery = HEIGHT_SCREEN/2
             display_surface.blit(Seleccion[0], Seleccion[1])
             Matrix[1][1] = Seleccion[2]
           
def posiblemovement(Seleccion) :
    Libres = []
    Temp = [0,1]
    for y in Temp:
        for i in range(len(Matrix)):
            for x in range(len(Matrix[i])):
                if Matrix[i][x] != 0 and Matrix[i][x] != 1:
                    Libres.append( (i,x) )
                    for p1 in (Libres):
                        Estado = deepcopy(Matrix)
                        Estado[p1[0]][p1[1]] = y
                        if ThinkAccion(Estado):
                          
                            if (0,0) == (p1[0],p1[1]) :
                            
                                Seleccion[1].x = 160+30
                                Seleccion[1].y = 100 
                                display_surface.blit(Seleccion[0], Seleccion[1])
                                Matrix[0][0] = Seleccion[2]
                                return True
                            #Segundo Cuadro
                            if (0,1) == (int(p1[0]),int(p1[1])) :
                                Seleccion[1].x = 300+75
                                Seleccion[1].y = 100 
                                display_surface.blit(Seleccion[0], Seleccion[1])
                                Matrix[0][1] = Seleccion[2]
                                return True
                            #Tercer Cuadro
                            if (0,2) == (p1[0],p1[1]):
                                Seleccion[1].x = 500+60
                                Seleccion[1].y = 100 
                                display_surface.blit(Seleccion[0], Seleccion[1])
                                Matrix[0][2] = Seleccion[2]
                                return True
                            #Cuarto
                            if (1,0) == (p1[0],p1[1]) :
                              
                                Seleccion[1].x = 160+30
                                Seleccion[1].y = 275 
                                display_surface.blit(Seleccion[0], Seleccion[1])
                                Matrix[1][0] = Seleccion[2]
                                return True
                            #Quinto
                            if (1,1) == (p1[0],p1[1]) :
                               
                                Seleccion[1].centerx = WIDTH_SCREEN/2
                                Seleccion[1].centery = HEIGHT_SCREEN/2
                                display_surface.blit(Seleccion[0], Seleccion[1])
                                Matrix[1][1] = Seleccion[2]
                                return True
                            #Sexto
                            if (1,2) == (p1[0],p1[1]) :
                               
                                Seleccion[1].x = 500+60
                                Seleccion[1].y = 275
                                display_surface.blit(Seleccion[0], Seleccion[1])
                                Matrix[1][2] = Seleccion[2]
                                return True
                            #Septimo cuadro
                            if (2,0) == (p1[0],p1[1]) :
                               
                                Seleccion[1].x = 160+30
                                Seleccion[1].y = 455 
                                display_surface.blit(Seleccion[0], Seleccion[1])
                                Matrix[2][0] = Seleccion[2]
                                return True
                            #Octavo Cuadro
                            if (2,1) == (p1[0],p1[1]) :
                            
                                Seleccion[1].x = 300+75
                                Seleccion[1].y = 455  
                                display_surface.blit(Seleccion[0], Seleccion[1])
                                Matrix[2][1] = Seleccion[2]
                                return True
                            #Noveno Cuadro
                            if (2,2) == (p1[0],p1[1]) :

                                Seleccion[1].x = 500+60
                                Seleccion[1].y = 455  
                                display_surface.blit(Seleccion[0], Seleccion[1])
                                Matrix[2][2] = Seleccion[2]
                                return True

def ThinkAccion(Estado):
    for i in range(len(Estado)):
        if Estado[i][0] == Estado[i][1] and Estado[i][0] == Estado[i][2]:
            return True     
    for i in range(len(Estado)):
        if Estado[0][i] == Estado[1][i] and Estado[1][i] == Estado[2][i]:
            return True      
    i = 0
    if Estado[i][i] == Estado[i+1][i+1] and Estado[i][i] == Estado[i+2][i+2] or Estado[i][2] == Estado[i+1][i+1] and Estado[i][2] == Matrix[i+2][i]:
        return True                   

def randomMove(Seleccion,p1):
    #Primer Cuadro
    if (0,0) == (p1[0],p1[1]) :
        Seleccion[1].x = 160+30
        Seleccion[1].y = 100 
        display_surface.blit(Seleccion[0], Seleccion[1])
        Matrix[0][0] = Seleccion[2]
        return True
    #Segundo Cuadro
    if (0,1) == (int(p1[0]),int(p1[1])) :
        Seleccion[1].x = 300+75
        Seleccion[1].y = 100 
        display_surface.blit(Seleccion[0], Seleccion[1])
        Matrix[0][1] = Seleccion[2]
        return True
    #Tercer Cuadro
    if (0,2) == (p1[0],p1[1]):
        Seleccion[1].x = 500+60
        Seleccion[1].y = 100 
        display_surface.blit(Seleccion[0], Seleccion[1])
        Matrix[0][2] = Seleccion[2]
        return True
    #Cuarto
    if (1,0) == (p1[0],p1[1]) :
        
        Seleccion[1].x = 160+30
        Seleccion[1].y = 275 
        display_surface.blit(Seleccion[0], Seleccion[1])
        Matrix[1][0] = Seleccion[2]
        return True
    #Quinto
    if (1,1) == (p1[0],p1[1]) :
        
        Seleccion[1].centerx = WIDTH_SCREEN/2
        Seleccion[1].centery = HEIGHT_SCREEN/2
        display_surface.blit(Seleccion[0], Seleccion[1])
        Matrix[1][1] = Seleccion[2]
        return True
    #Sexto
    if (1,2) == (p1[0],p1[1]) :
        
        Seleccion[1].x = 500+60
        Seleccion[1].y = 275
        display_surface.blit(Seleccion[0], Seleccion[1])
        Matrix[1][2] = Seleccion[2]
        return True
    #Septimo cuadro
    if (2,0) == (p1[0],p1[1]) :
        
        Seleccion[1].x = 160+30
        Seleccion[1].y = 455 
        display_surface.blit(Seleccion[0], Seleccion[1])
        Matrix[2][0] = Seleccion[2]
        return True
    #Octavo Cuadro
    if (2,1) == (p1[0],p1[1]) :

        Seleccion[1].x = 300+75
        Seleccion[1].y = 455  
        display_surface.blit(Seleccion[0], Seleccion[1])
        Matrix[2][1] = Seleccion[2]
        return True
    #Noveno Cuadro
    if (2,2) == (p1[0],p1[1]) :

        Seleccion[1].x = 500+60
        Seleccion[1].y = 455  
        display_surface.blit(Seleccion[0], Seleccion[1])
        Matrix[2][2] = Seleccion[2]
        return True

def CheckWin():

    for i in range(len(Matrix)):
        if Matrix[i][0] == Matrix[i][1] and Matrix[i][0] == Matrix[i][2]:
            return False     
    for i in range(len(Matrix)):
        if Matrix[0][i] == Matrix[1][i] and Matrix[1][i] == Matrix[2][i]:
            return False      
    i = 0
    if Matrix[i][i] == Matrix[i+1][i+1] and Matrix[i][i] == Matrix[i+2][i+2] or Matrix[i][2] == Matrix[i+1][i+1] and Matrix[i][2] == Matrix[i+2][i]:
        return False    

main()

pygame.quit()
