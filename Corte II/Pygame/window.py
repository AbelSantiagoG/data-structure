from combbox import ComboBox
from SLL import SingleLinkedList
from menu import Menu
import pygame, sys

class ben10:
    def __init__(self):
        #Colores
        self.black= (0, 0, 0)
        self.white= (255, 255, 255)
        self.green= (0, 255, 0)
        self.red= (255, 0, 0)
        self.blue= (0, 0, 255)
        self.gray= (155, 155, 155)

        self.cambiarVentana= True

        #Rectángulos para cabezas
        self.rect1= pygame.Rect(240, 170, 130, 104)
        self.rect2= pygame.Rect(440, 170, 130, 104)
        self.rect3= pygame.Rect(640, 170, 130, 104)

        self.screen= pygame.display.set_mode((1000, 700))
        #Menu
        self.main_menu = Menu(self.screen, {"SLL": "imágenes/list-outline.png", "DLL": "imágenes/list-outline.png", "Pilas y colas": "imágenes/list-outline.png", "Árboles": "imágenes/tree-solid.png", "Grafos": "imágenes/circle-nodes-solid.png"}, self.green, 40, "Sans Serif", 22, self.black)
        
        #Instancia de sll
        self.inst_sll= SingleLinkedList()

        pygame.init()
        pygame.display.set_caption("TAD")
        self.color= (220, 220, 220) 

        #Combobox métodos
        self.combo_rect1 = pygame.Rect(330, 125, 255, 28)
        self.combo1 = ComboBox(self.screen, ["Agregar elemento al inicio", "Agregar elemento al final", "Agregar elemento en una posicion", "Eliminar primer elemento", "Eliminar ultimo elemento", "Eliminar elemento en una posicion", "Eliminar todos los elementos", "Invertir lista", "Cambiar imagen en una posicion", "Lista vacia"], self.combo_rect1, self.black, "Sans serif", 22, 5, self.white, self.white, 40, "")
        self.button = pygame.Rect(504, 500, 191, 39)
        self.click_button = False

        #Posiciones de la lista
        self.posiciones= []
        for i in range (self.inst_sll.length):
            self.posiciones.append(i)

        #Combobox posiciones
        self.combo_rect2= pygame.Rect(750, 125, 100, 28)
        self.combo2= ComboBox(self.screen, self.posiciones, self.combo_rect2, self.black, "Sans Serif", 22, 5, self.white, self.white, 40, "")

        #Imágenes}
        self.bestia= pygame.image.load("imágenes/Bestia.png").convert()
        self.cuatro_brazos= pygame.image.load("imágenes/Cuatrobrazos.png").convert()
        self.diamante= pygame.image.load("imágenes/Diamante.png").convert()
        self.fantasmatico= pygame.image.load("imágenes/Fantasmático.png").convert()
        self.cannonbolt= pygame.image.load("imágenes/Cannonbolt.png").convert()
        self.xlr8= pygame.image.load("imágenes/XLR8.png").convert()
        
        self.xlr8= pygame.transform.scale(self.xlr8, (130, 104))
        self.bestia= pygame.transform.scale(self.bestia, (130, 104))
        self.cuatro_brazos= pygame.transform.scale(self.cuatro_brazos, (130, 104))
        self.diamante= pygame.transform.scale(self.diamante, (130, 104))
        self.fantasmatico= pygame.transform.scale(self.fantasmatico, (130, 104))
        self.cannonbolt= pygame.transform.scale(self.cannonbolt, (130, 104))
    
    def mantenerVentana(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.color)

            #Zona de dibujo
            #SLL
            if(self.main_menu.getSelectedOption() == 0):
                if self.cambiarVentana:
                    self.dibujarVentana1()
                else:
                    self.dibujarVentana2()
            elif(self.main_menu.getSelectedOption() == 1):
                pygame.draw.rect(self.screen, (0, 0 ,0), (0, 40, self.screen.get_width(), self.screen.get_height() - 40))
            self.main_menu.draw()
            pygame.display.flip()

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
    
    #def añadirAlInicio(self):
        #for i in range (self.inst_sll.length):
            #if 

    def dibujarVentana1(self):
        #Texto
        self.mostrarTexto("Single Linked List", self.black, 30, 20, 70)
        self.mostrarTexto("PARA INICIAR DEBES SELECCIONAR AL MENOS UNA IMAGEN QUE SERÁ LA CABEZA DE LA LISTA", self.black, 24, 100, 140)
        #Imágenes
        self.dibujarImagenes(self.cannonbolt, 240, 200)
        self.dibujarImagenes(self.diamante, 440, 200)
        self.dibujarImagenes(self.bestia, 640, 200)
        self.tocoCabeza()
    
    def dibujarVentana2(self):
        #Texto
        self.mostrarTexto("Single Linked List", self.black, 30, 20, 70)
        self.mostrarTexto("Selecciona un método", self.black, 28, 110, 128)
        self.mostrarTexto("Posición", self.black, 28, 657, 128)
        #Imágenes
        self.dibujarImagenes(self.cannonbolt, 55, 180)
        self.dibujarImagenes(self.bestia, 205, 180)
        self.dibujarImagenes(self.cuatro_brazos, 355, 180)
        self.dibujarImagenes(self.diamante, 505, 180)
        self.dibujarImagenes(self.xlr8, 655, 180)
        self.dibujarImagenes(self.fantasmatico, 805, 180)


        #Botón
        self.drawButton("Aceptar", self.gray, self.button, 0, 16, 22, True, self.black)
        #Combobox
        pygame.draw.rect(self.screen, self.black, self.combo_rect1, 0, 5)
        self.combo1.draw()
        pygame.draw.rect(self.screen, self.black, self.combo_rect2, 0, 5)
        self.combo2.draw()
        
        self.clickOnButton()

    def mostrarTexto(self, texto, color, dimensiones, x , y):
        superficie= pygame.font.SysFont("Sans Serif", dimensiones)
        text_surface= superficie.render(texto, True, color)
        self.screen.blit(text_surface, (x,y))

    def dibujarImagenes(self, img, x, y):
        rect= pygame.draw.rect(self.screen, self.white, (x,y,130, 104),0,10)
        self.screen.blit(img, (x,y))
        rect= pygame.draw.rect(self.screen, self.black, (x,y,130, 104),2,10)
        if rect.collidepoint(pygame.mouse.get_pos()):
            rect= pygame.draw.rect(self.screen, self.black, (x, y, 130, 104),2,10)
    
    def drawButton(self, text, button_color, background_rect, border, border_radius, text_size, text_bold, text_color):
        pygame.draw.rect(self.screen, button_color, background_rect, border, border_radius)
        font = pygame.font.SysFont("Sans Serif", text_size, text_bold)
        render_text = font.render(text, True, text_color, None)
        self.screen.blit(render_text, (background_rect.x + (background_rect.width - render_text.get_width())/2, background_rect.y + (background_rect.height - render_text.get_height())/2))

    def clickOnButton(self):
        if self.button.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == True and not self.click_button:
                print(self.combo1.getValue())
                self.click_button = True
        if not pygame.mouse.get_pressed()[0]:
            self.click_button = False