from combbox import ComboBox
from SLL import SingleLinkedList
from menu import Menu
import webbrowser
import pygame, sys
import random
from jugador import jugador
from crupier import crupier

class challenge:
    def __init__(self):
        #Colores
        self.black= (0, 0, 0)
        self.white= (255, 255, 255)
        self.green= (0, 255, 0)
        self.red= (255, 0, 0)
        self.blue= (0, 0, 255)
        self.gray= (155, 155, 155)
        self.brown= (113, 63, 16)

        #Cambiar ventana cuando se selecciona una cabeza
        self.cambiarVentana= True

        #valor seleccionado
        self.value= ""

        #Rectángulos para cabezas
        self.rect1= pygame.Rect(240, 170, 130, 124)
        self.rect2= pygame.Rect(440, 170, 130, 124)
        self.rect3= pygame.Rect(640, 170, 130, 124)

        self.screen= pygame.display.set_mode((1000, 700))
        #Menu
        self.main_menu = Menu(self.screen, {"SLL": "imágenes/list-outline.png", "DLL": "imágenes/list-outline.png", "Pilas y colas": "imágenes/list-outline.png", "Árboles": "imágenes/tree-solid.png", "Grafos": "imágenes/circle-nodes-solid.png"}, self.white, 40, "Sans Serif", 22, self.black)
        
        #Instancia de sll
        self.inst_sll= SingleLinkedList()

        pygame.init()
        pygame.display.set_caption("TAD")
        self.color= (220, 220, 220) 

        #Combobox métodos
        self.combo_rect1 = pygame.Rect(330, 125, 255, 28)
        self.combo1 = ComboBox(self.screen, ["Agregar elemento al inicio", "Agregar elemento al final", "Agregar elemento en una posicion", "Eliminar primer elemento", "Eliminar ultimo elemento", "Eliminar elemento en una posicion", "Eliminar todos los elementos", "Invertir lista", "Cambiar imagen en una posicion", "Lista vacia", "Eliminar duplicados"], self.combo_rect1, self.black, "Sans serif", 22, 5, self.white, self.white, 40, "Seleccione el metodo")
        self.button = pygame.Rect(145, 345, 191, 39)
        self.click_button = False

        #Combobox posiciones
        self.combo_rect2= pygame.Rect(750, 125, 100, 28)
        self.combo2= ComboBox(self.screen, ["1"], self.combo_rect2, self.black, "Sans Serif", 22, 5, self.white, self.white, 40, "¨Posiciones")

        #Imágenes SLL
        self.bestia= pygame.image.load("imágenes/Bestia.png")
        self.cuatro_brazos= pygame.image.load("imágenes/Cuatrobrazos.png")
        self.diamante= pygame.image.load("imágenes/Diamante.png")
        self.fantasmatico= pygame.image.load("imágenes/Fantasmático.png")
        self.cannonbolt= pygame.image.load("imágenes/Cannonbolt.png")
        self.xlr8= pygame.image.load("imágenes/XLR8.png")
        
        self.xlr8= pygame.transform.scale(self.xlr8, (130, 124))
        self.bestia= pygame.transform.scale(self.bestia, (130, 124))
        self.cuatro_brazos= pygame.transform.scale(self.cuatro_brazos, (130, 124))
        self.diamante= pygame.transform.scale(self.diamante, (130, 124))
        self.fantasmatico= pygame.transform.scale(self.fantasmatico, (130, 124))
        self.cannonbolt= pygame.transform.scale(self.cannonbolt, (130, 124))

#Pilas y colas
        #Imágenes pilas y colas
            #Fondo
        self.fondo= pygame.image.load("Imágenes 2/blackjack-classic-background.jpg")
        self.crupier_img= pygame.image.load("Imágenes 2/CRUPIER-removebg-preview(1).png")

        self.fondo= pygame.transform.scale(self.fondo, (1000, 630))
        self.crupier_img= pygame.transform.scale(self.crupier_img, (300, 200))

        #Botones
        self.button_start= pygame.Rect(404, 85, 110, 27)
        self.button_plantarme_jugador_1= pygame.Rect(170, 305, 110, 33)
        self.button_plantarme_jugador_2= pygame.Rect(495, 445, 110, 33)
        self.button_plantarme_jugador_3= pygame.Rect(810, 305, 110, 33)
        self.button_pedir_cartas= pygame.Rect(460, 270, 135, 33)

        self.click_button_start = False
        self.click_button_plantarme_jugador_1= False
        self.click_button_plantarme_jugador_2= False
        self.click_button_plantarme_jugador_3= False
        self.click_button_pedir_cartas= False

        #Barajas
        self.baraja_total= list()

        #Jugadores
        self.jugador_1= jugador(70, 180, 120, 290)
        self.jugador_2= jugador(400, 330, 445, 430)
        self.jugador_3= jugador(770, 180, 760, 290)
        self.crupier= crupier(570, 90)

        #Lista de jugadores
        self.lista_jugadores= list()
        self.lista_jugadores.append(self.jugador_1)
        self.lista_jugadores.append(self.jugador_2)
        self.lista_jugadores.append(self.jugador_3)

        self.puntaje_crupier= 0
        self.turno= 1

#Funcion principal

    def Run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.color)
            #SLL
            if(self.main_menu.getSelectedOption() == 0):
                self.mostrarTexto("Single Linked List", self.black, 30, 20, 70, "Sans Serif")
                self.dibujarFooter((220, 220, 220))
                self.clickEnLogoGit()
                if self.cambiarVentana:
                    self.dibujarVentana1()
                else:
                    self.dibujarVentana2()
            elif(self.main_menu.getSelectedOption() == 1):
                pygame.draw.rect(self.screen, (0, 0 ,0), (0, 40, self.screen.get_width(), self.screen.get_height() - 40))
            elif(self.main_menu.getSelectedOption() == 2):
                self.dibujarFooter(self.white)
                self.dibujarVentanaBlackJack()
                self.llenarBarajaTotal()
                self.iniciar()
                self.juego()
                self.dibujarCartas()
                if self.turno <= 3:
                    self.crupier.dibujarLista(self.screen)
                    self.crupier.dibujarPrimerasCartas(self.screen,615,76)
                else:
                    self.crupier.dibujarLista(self.screen)
                self.jugadorPierde()
                self.crupierSePlanta()
                self.clickEnLogoGit()
            self.main_menu.draw()
            pygame.display.flip()

#SLL (reto 1)
#-------------------------------------------------------------------------------------------------------------------------------------------

    def tocoCabeza(self):
        mousecoord= pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.rect1.collidepoint(mousecoord):
                self.inst_sll.create_node_sll_unshift("Cannonbolt")
                self.cambiarVentana= False
            if self.rect2.collidepoint(mousecoord):
                self.inst_sll.create_node_sll_unshift("Diamante")
                self.cambiarVentana= False
            if self.rect3.collidepoint(mousecoord):
                self.inst_sll.create_node_sll_unshift("Bestia")
                self.cambiarVentana= False

    def valueNode(self):
        cannonbolt= pygame.Rect(60, 180, 130, 124)
        bestia= pygame.Rect(210, 180, 130, 124)
        cuatro_brazos= pygame.Rect(360, 180, 130, 124)
        diamante= pygame.Rect(510, 180, 130, 124)
        xlr8= pygame.Rect(660, 180, 130, 124)
        fantasmatico= pygame.Rect(810, 180, 130, 124)

        mousecoord= pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if cannonbolt.collidepoint(mousecoord):
                self.value= "Cannonbolt"
            if bestia.collidepoint(mousecoord):
                self.value= "Bestia"
            if cuatro_brazos.collidepoint(mousecoord):
                self.value= "Cuatrobrazos"
            if diamante.collidepoint(mousecoord):
                self.value= "Diamante"
            if xlr8.collidepoint(mousecoord):
                self.value= "Xlr8"
            if fantasmatico.collidepoint(mousecoord):
                self.value= "Fantasmatico"

    def metodos(self):
            if(self.combo1.getIndex() == 0 and self.inst_sll.length < 7):
                self.inst_sll.create_node_sll_unshift(self.value)
            elif(self.combo1.getIndex() == 1 and self.inst_sll.length < 7):
                self.inst_sll.create_node_sll_ends(self.value)
            elif(self.combo1.getIndex() == 2 and self.inst_sll.length < 7):
                self.inst_sll.create_node_sll_at_determinate_position(self.value, int(self.combo2.getValue()))
            elif(self.combo1.getIndex() == 3):
                self.inst_sll.shift_node_sll()
            elif(self.combo1.getIndex() == 4):
                self.inst_sll.delete_node_sll_pop()
            elif(self.combo1.getIndex() == 5):
                self.inst_sll.remove_node(int(self.combo2.getValue()))
            elif(self.combo1.getIndex() == 6):
                self.inst_sll.delete_all_items()
            elif(self.combo1.getIndex() == 7):
                self.inst_sll.reverse_sll()
            elif(self.combo1.getIndex() == 8):
                self.inst_sll.update_node_value(int(self.combo2.getValue()), self.value)
            elif(self.combo1.getIndex() == 9):
                self.inst_sll.is_empty()
            elif(self.combo1.getIndex() == 10):
                self.inst_sll.remove_node_duplicated(self.value)
            data_list = [str(x) for x in range(1, self.inst_sll.length+1)]
            self.combo2.updateOptions(data_list)

    def dibujarLista(self):
        j=10
        for i in range (1,self.inst_sll.length+1):
                if self.inst_sll.get_node_value(i) == "Cannonbolt":
                    self.dibujarImagenes(self.cannonbolt, j, 415)
                elif self.inst_sll.get_node_value(i) == "Bestia":
                    self.dibujarImagenes(self.bestia, j, 415)
                elif self.inst_sll.get_node_value(i) == "Diamante":
                    self.dibujarImagenes(self.diamante, j, 415)
                elif self.inst_sll.get_node_value(i) == "Cuatrobrazos":
                    self.dibujarImagenes(self.cuatro_brazos, j, 415)
                elif self.inst_sll.get_node_value(i) == "Fantasmatico":
                    self.dibujarImagenes(self.fantasmatico, j, 415)
                elif self.inst_sll.get_node_value(i) == "Xlr8":
                    self.dibujarImagenes(self.xlr8, j, 415)
                j+=135
            

    def dibujarVentana1(self):
        #Texto
        self.mostrarTexto("PARA INICIAR DEBES SELECCIONAR AL MENOS UNA IMAGEN QUE SERÁ LA CABEZA DE LA LISTA", self.black, 24, 100, 140, "Sans Serif")
        #Imágenes
        self.dibujarImagenes(self.cannonbolt, 240, 200)
        self.dibujarImagenes(self.diamante, 440, 200)
        self.dibujarImagenes(self.bestia, 640, 200)
        self.tocoCabeza()
    
    def dibujarVentana2(self):
        #Texto
        self.mostrarTexto("Selecciona un método", self.black, 28, 110, 128, "Sans Serif")
        self.mostrarTexto("Posición", self.black, 28, 657, 128, "Sans Serif")
        #Imágenes
        self.dibujarImagenes(self.cannonbolt, 60, 180)
        self.dibujarImagenes(self.bestia, 210, 180)
        self.dibujarImagenes(self.cuatro_brazos, 360, 180)
        self.dibujarImagenes(self.diamante, 510, 180)
        self.dibujarImagenes(self.xlr8, 660, 180)
        self.dibujarImagenes(self.fantasmatico, 810, 180)
        #Botón
        self.drawButton("Aceptar", self.gray, self.button, 0, 16, 22, True, self.black)
        #Zona de mostrar lista
        pygame.draw.rect(self.screen, (208, 208, 208), (0, 400, self.screen.get_width(), 150))
        #Combobox
        pygame.draw.rect(self.screen, self.black, self.combo_rect1, 0,5)
        pygame.draw.rect(self.screen, self.black, self.combo_rect2, 0, 5)
        
        self.clickOnButtonAccept()
        self.valueNode()
        #self.metodos()
        self.dibujarLista()
        self.combo1.draw()
        self.combo2.draw()
        
    def dibujarFooter(self, color):
        pygame.draw.rect(self.screen, color, (0, 630, self.screen.get_width(), 80))
        logo1= pygame.image.load("imágenes/logo_uam.jpg")
        logo1= pygame.transform.scale(logo1, (55, 50))
        logo2= pygame.image.load("imágenes/logo_github.png")
        logo2= pygame.transform.scale(logo2, (45, 40))
        self.mostrarTexto("Desarrollado por:", self.black, 23, 360, 650, "Sans Serif")
        self.mostrarTexto("Abel Gomez", self.black, 21, 490, 650, "Sans Serif")
        self.mostrarTexto("@ | SEM -2023", self.black, 21, 415, 675, "Sans Serif")
        self.dibujarImagenes(logo2, 580, 650)
        self.dibujarImagenes(logo1, 935, 650)

    def clickEnLogoGit(self):
        mousecoord= pygame.mouse.get_pos()
        rect= pygame.Rect(580, 630, 45, 40)
        if pygame.mouse.get_pressed()[0]:
            if rect.collidepoint(mousecoord):
                webbrowser.open(r"https://github.com/AbelSantiagoG/data-structure.git")

    def mostrarTexto(self, texto, color, dimensiones, x , y, fuente):
        superficie= pygame.font.SysFont(fuente, dimensiones)
        text_surface= superficie.render(texto, True, color)
        self.screen.blit(text_surface, (x,y))

    def dibujarImagenes(self, img, x, y):
        self.screen.blit(img, (x,y))
    
    def drawButton(self, text, button_color, background_rect, border, border_radius, text_size, text_bold, text_color):
        pygame.draw.rect(self.screen, button_color, background_rect, border, border_radius)
        font = pygame.font.SysFont("Sans Serif", text_size, text_bold)
        render_text = font.render(text, True, text_color, None)
        self.screen.blit(render_text, (background_rect.x + (background_rect.width - render_text.get_width())/2, background_rect.y + (background_rect.height - render_text.get_height())/2))

    def clickOnButtonAccept(self):
        if self.button.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.click_button:
                self.click_button = True
                self.metodos()
        if not pygame.mouse.get_pressed()[0]:
            self.click_button = False

#-------------------------------------------------------------------------------------------------------------------------------------------

#Empieza pilas (reto 2)
#-------------------------------------------------------------------------------------------------------------------------------------------
    
    def dibujarVentanaBlackJack(self):
        self.dibujarImagenes(self.fondo, 0, 0)
        self.drawButton("START", self.brown, self.button_start, 0, 10, 18, True, self.black)
        self.drawButton("PLANTARME", self.brown, self.button_plantarme_jugador_1, 0, 10, 18, True, self.black)
        self.drawButton("PLANTARME", self.brown, self.button_plantarme_jugador_2, 0, 10, 18, True, self.black)
        self.drawButton("PLANTARME", self.brown, self.button_plantarme_jugador_3, 0, 10, 18, True, self.black)
        self.drawButton("PEDIR CARTAS", self.brown, self.button_pedir_cartas, 0, 10, 18, True, self.black)
        self.dibujarImagenes(self.crupier_img, 350, 115)
        self.mostrarTexto("Para iniciar el juego debes dar click en el botón START", self.white, 18, 45, 85, "Arial")
        self.mostrarTexto("JUGADOR 1", self.white, 18, 84, 310, "Arial")
        self.mostrarTexto("JUGADOR 2", self.white, 18, 407, 449, "Arial")
        self.mostrarTexto("JUGADOR 2", self.white, 18, 720, 310, "Arial")


    def iniciar(self):
        if self.button_start.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.click_button_start:
                self.click_button_start = True
                self.repartirCartas()
                print(self.jugador_1.list)
                print(self.jugador_2.list)
                print(self.jugador_3.list)
        if not pygame.mouse.get_pressed()[0]:
            self.click_button_start = False
    
    def llenarBarajaTotal(self):
        while len(self.baraja_total) < 52:
            numeros = list(range(1, 14))
            random.shuffle(numeros)
            for i in numeros:
                if self.baraja_total.count(i) < 4:
                    if i== 1:
                        self.baraja_total.append("as")
                    elif i == 11:
                        self.baraja_total.append("J")
                    elif i == 12:
                        self.baraja_total.append("Q")
                    elif i == 13:
                        self.baraja_total.append("K")
                    else:
                        self.baraja_total.append(str(i))
            
    

    def jugadorPierde(self):
        for i in self.lista_jugadores:
            if i.puntaje > 21:
                i.lose = True
                self.mostrarTexto('Está fuera', self.black, 20,i.xlose+5, i.ylose + 45, "Arial")
    
    def crupierPide(self):
        while self.crupier.puntaje <=16:
            self.crupier.añadirCartas(self.baraja_total.pop())

    def crupierSePlanta(self):
        if self.crupier.puntaje<=16 and self.turno > 3:
            self.crupier.plantarse = True
            self.crupier.añadirCartas(self.baraja_total.pop())
        if self.crupier.puntaje > 21 and self.turno >3: 
            self.crupier.lose = True
            self.mostrarTexto('Está fuera', self.white, 20, 751, 52, "Arial")
        
    def repartirCartas(self):
        self.jugador_1.añadirCartas(self.baraja_total.pop())
        self.jugador_2.añadirCartas(self.baraja_total.pop())
        self.jugador_3.añadirCartas(self.baraja_total.pop())
        self.jugador_1.añadirCartas(self.baraja_total.pop())
        self.jugador_2.añadirCartas(self.baraja_total.pop())
        self.jugador_3.añadirCartas(self.baraja_total.pop())

        self.crupier.añadirCartas(self.baraja_total.pop())
        self.crupier.añadirCartas(self.baraja_total.pop())
    
    def dibujarCartas(self):
        for i in self.lista_jugadores:
            i.dibujarLista(self.screen)
    
    def juego(self):
        if self.turno == 1:
            if pygame.mouse.get_pressed()[0]:
                if self.button_pedir_cartas.collidepoint(pygame.mouse.get_pos()) and len(self.baraja_total)!=0 and not self.jugador_1.lose:
                    self.jugador_1.añadirCartas(self.baraja_total.pop())
                    if self.jugador_1.puntaje > 21:
                        self.turno+=1
                        return
                elif self.button_plantarme_jugador_1.collidepoint(pygame.mouse.get_pos()) or self.jugador_1.lose:
                    print('jugador 1:', self.jugador_1.puntaje)
                    self.turno+=1

        if self.turno == 2:
            if pygame.mouse.get_pressed()[0]:
                if self.button_pedir_cartas.collidepoint(pygame.mouse.get_pos()) and len(self.baraja_total)!=0 and not self.jugador_2.lose:
                    self.jugador_2.añadirCartas(self.baraja_total.pop())
                    if self.jugador_2.puntaje > 21:
                        self.turno+=1
                        return
                elif self.button_plantarme_jugador_2.collidepoint(pygame.mouse.get_pos()) or self.jugador_2.lose:
                    print('jugador 2:', self.jugador_2.puntaje)
                    self.turno+=1

        if self.turno == 3:
            if pygame.mouse.get_pressed()[0]:
                if self.button_pedir_cartas.collidepoint(pygame.mouse.get_pos()) and len(self.baraja_total)!=0 and not self.jugador_3.lose:
                    self.jugador_3.añadirCartas(self.baraja_total.pop())
                    if self.jugador_3.puntaje > 21:
                        self.turno+=1
                        return
                elif self.button_plantarme_jugador_3.collidepoint(pygame.mouse.get_pos()) or self.jugador_3.lose:
                    print('Jugador 3: ',self.jugador_3.puntaje)
                    self.turno+=1
        if self.turno == 4:
            self.crupierSePlanta()
            self.ganadores()

    def ganadores(self):
        for i in self.lista_jugadores:
            if i.puntaje > self.crupier.puntaje and not i.lose:
                self.mostrarTexto('Gano el juego', self.white, 20,i.xlose, i.ylose, "Arial")
            elif i.puntaje < self.crupier.puntaje and not self.crupier.lose:
                self.mostrarTexto('Perdio el juego', self.white, 20,i.xlose, i.ylose, "Arial")
            elif i.puntaje == self.crupier.puntaje and not self.crupier.lose:
                self.mostrarTexto('Empate', self.white, 20,i.xlose, i.ylose, "Arial")
            elif not i.lose and self.crupier.lose:
                self.mostrarTexto('Gano el juego', self.white, 20,i.xlose, i.ylose, "Arial")
    
