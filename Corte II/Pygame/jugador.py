import pygame
class jugador:
    def __init__(self, x, y ,list, x_lose, y_lose):
        self.x= x
        self.y= y
        self.list= list
        self.puntaje= 0
        self.lose= False
        self.xlose= x_lose
        self.ylose= y_lose

        self.carta_2= pygame.image.load("Imágenes 2/2V2.jpg")
        self.carta_3= pygame.image.load("Imágenes 2/3V2.jpg")
        self.carta_4= pygame.image.load("Imágenes 2/4V2.jpg")
        self.carta_5= pygame.image.load("Imágenes 2/5.jpg")
        self.carta_6= pygame.image.load("Imágenes 2/6.jpg")
        self.carta_7= pygame.image.load("Imágenes 2/7V2.jpg")
        self.carta_8= pygame.image.load("Imágenes 2/8.jpg")
        self.carta_9= pygame.image.load("Imágenes 2/9.jpg")
        self.carta_10= pygame.image.load("Imágenes 2/10.jpg")
        self.carta_J= pygame.image.load("Imágenes 2/J2.jpg")
        self.carta_K= pygame.image.load("Imágenes 2/K3.jpg")
        self.carta_Q= pygame.image.load("Imágenes 2/Q2.jpg")
        self.carta_A= pygame.image.load("Imágenes 2/as.png")

        self.carta_2= pygame.transform.scale(self.carta_2, (80, 115))
        self.carta_3= pygame.transform.scale(self.carta_3, (80, 115))
        self.carta_4= pygame.transform.scale(self.carta_4, (80, 115))
        self.carta_5= pygame.transform.scale(self.carta_5, (80, 115))
        self.carta_6= pygame.transform.scale(self.carta_6, (80, 115))
        self.carta_7= pygame.transform.scale(self.carta_7, (80, 115))
        self.carta_8= pygame.transform.scale(self.carta_8, (80, 115))
        self.carta_9= pygame.transform.scale(self.carta_9, (80, 115))
        self.carta_10= pygame.transform.scale(self.carta_10, (80, 115))
        self.carta_J= pygame.transform.scale(self.carta_J, (80, 115))
        self.carta_K= pygame.transform.scale(self.carta_K, (80, 115))
        self.carta_Q= pygame.transform.scale(self.carta_Q, (80, 115))
        self.carta_A= pygame.transform.scale(self.carta_A, (80, 115))
    
    def score(self):
        for i in self.list:
            self.puntaje+= int(i)
    
    def dibujarLista(self, screen):
        espacio= self.x
        for j in self.list:
            if j == "as":
                screen.blit(self.carta_A, (espacio, self.y))
            if j == "2":
                screen.blit(self.carta_2, (espacio, self.y))
            if j == "3":
                screen.blit(self.carta_3, (espacio, self.y))
            if j == "4":
                screen.blit(self.carta_4, (espacio, self.y))
            if j == "5":
                screen.blit(self.carta_5, (espacio, self.y))
            if j == "6":
                screen.blit(self.carta_6, (espacio, self.y))
            if j == "7":
                screen.blit(self.carta_7, (espacio, self.y))
            if j == "8":
                screen.blit(self.carta_8, (espacio, self.y))
            if j == "9":
                screen.blit(self.carta_9, (espacio, self.y))
            if j == "10":
                screen.blit(self.carta_10, (espacio, self.y))
            if j == "J":
                screen.blit(self.carta_J, (espacio, self.y))
            if j == "Q":
                screen.blit(self.carta_Q, (espacio, self.y))
            if j == "K":
                screen.blit(self.carta_K, (espacio, self.y))
            espacio+= 40

    def añadirCartas(self, card):
        if card=='J' or card == 'Q' or card == 'K':
            self.list.append(card)
            self.score+=10
        elif card == 'As':
            if self.score <=10:
                self.score+=11
                self.list.append(card)
            elif self.score >10:
                self.score+=1
                self.list.append(card)
        else:
            self.score+=int(card)
            self.list.append(card)