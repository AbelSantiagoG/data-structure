class jugador:
    def __init__(self, x, y ,list):
        self.x= x
        self.y= y
        self.list= list
        self.puntaje= 0
    
    def score(self):
        puntaje=0
        for i in self.list:
            puntaje+= int(i)
        return puntaje
    
    def dibujarCartas(self):
        espacio=50
        #for carta in self.list:
            
