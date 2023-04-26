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

        self.screen= pygame.display.set_mode((1000, 700))
        #Menu
        self.main_menu = Menu(self.screen, {"SLL": "imágenes/list-outline.png", "DLL": "imágenes/list-outline.png", "Pilas y colas": "imágenes/list-outline.png", "Árboles": "imágenes/tree-solid.png", "Grafos": "imágenes/circle-nodes-solid.png"}, self.green, 40, "Sans Serif", 22, self.black)
        #Instancia de sll
        inst_sll= SingleLinkedList()
        pygame.init()
        pygame.display.set_caption("SLL")
        self.color= (220, 220, 220) 

        self.combo_rect1 = pygame.Rect(200, 270, 200, 28)
        self.combo1 = ComboBox(self.screen, ["Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5"], self.combo_rect1, self.black, "Sans serif", 22, 5, self.white, self.white, 40, "Selecciona un método")
        self.button = pygame.Rect(504, 356, 191, 39)
        self.click_button = False

        #Imágenes
        self.acuatico= pygame.image.load("imágenes/Acuático.png").convert()
        self.bestia= pygame.image.load("imágenes/Bestia.png").convert()
        self.cuatro_brazos= pygame.image.load("imágenes/Cuatrobrazos.png").convert()
        self.diamante= pygame.image.load("imágenes/Diamante.png").convert()
        self.fantasmatico= pygame.image.load("imágenes/Fantasmático.png").convert()
        self.fuego= pygame.image.load("imágenes/Fuego.png").convert()
        self.cannonbolt= pygame.image.load("imágenes/Cannonbolt.png").convert()
        self.materia_gris= pygame.image.load("imágenes/Materia_gris.png").convert()
        self.ultra_t= pygame.image.load("imágenes/Ultra_t.png").convert()
        self.xlr8= pygame.image.load("imágenes/XLR8.png").convert()
        
        self.xlr8= pygame.transform.scale(self.xlr8, (130, 134))
        self.acuatico= pygame.transform.scale(self.acuatico, (130, 134))
        self.bestia= pygame.transform.scale(self.bestia, (130, 134))
        self.cuatro_brazos= pygame.transform.scale(self.cuatro_brazos, (130, 134))
        self.diamante= pygame.transform.scale(self.diamante, (130, 134))
        self.fantasmatico= pygame.transform.scale(self.fantasmatico, (130, 134))
        self.fuego= pygame.transform.scale(self.fuego, (130, 134))
        self.cannonbolt= pygame.transform.scale(self.cannonbolt, (130, 134))
        self.materia_gris= pygame.transform.scale(self.materia_gris, (130, 134))
        self.ultra_t= pygame.transform.scale(self.ultra_t, (130, 134))
    
    def mantenerVentana(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.color)

            #Zona de dibujo
            #-------------------------------------------
            if(self.main_menu.getSelectedOption() == 0):
                pygame.draw.rect(self.screen, self.black, self.combo_rect1, 0, 5)
                self.combo1.draw()
                self.drawButton("Aceptar", self.gray, self.button, 0, 16, 22, True, self.black, "Consolas")
                self.clickOnButton()
                self.mostrarTexto("PARA INICIAR DEBES SELECCIONAR AL MENOS UNA IMAGEN QUE SERÁ LA CABEZA DE LA LISTA", self.black, 24, 100, 52)
                self.dibujarImagenes(self.acuatico, 235, 95)
                self.dibujarImagenes(self.diamante, 435, 95)
                self.dibujarImagenes(self.bestia, 635, 95)
            elif(self.main_menu.getSelectedOption() == 1):
                pygame.draw.rect(self.screen, (250, 10, 20), (0, 40, self.screen.get_width(), self.screen.get_height() - 40))
            self.main_menu.draw()
            pygame.display.flip()

    def mostrarTexto(self, texto, color, dimensiones, x , y):
        superficie= pygame.font.SysFont("Sans Serif", dimensiones)
        text_surface= superficie.render(texto, True, color)
        self.screen.blit(text_surface, (x,y))

    def dibujarImagenes(self, img, x, y):
        rect= pygame.draw.rect(self.screen, self.white, (x,y,130, 134),0,10)
        self.screen.blit(img, (x,y))
        rect= pygame.draw.rect(self.screen, self.black, (x,y,130, 134),2,10)
        if rect.collidepoint(pygame.mouse.get_pos()):
            rect= pygame.draw.rect(self.screen, self.black, (x, y, 130, 134),2,10)
    
    def drawButton(self, text, button_color, background_rect, border, border_radius, text_size, text_bold, text_color, text_font):
        pygame.draw.rect(self.screen, button_color, background_rect, border, border_radius)
        font = pygame.font.SysFont("Sans Serif", text_size, text_bold)
        render_text = font.render(text, True, text_color, None)
        self.screen.blit(render_text, (background_rect.x + (background_rect.width - render_text.get_width())/2, background_rect.y + (background_rect.height - render_text.get_height())/2))

    def clickOnButton(self):
        if self.button.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == True and not self.click_button:
                print(self.combo.getValue())
                self.click_button = True
        if not pygame.mouse.get_pressed()[0]:
            self.click_button = False