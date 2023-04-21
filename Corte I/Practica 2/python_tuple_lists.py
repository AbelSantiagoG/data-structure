class TupleList:
    def __init__(self):
        self.countries_list= []
        self.country_name= " "
        self.population= 0
        self.continent= " "

    #Funcion que solicita al usuario cuantos paises quiere ingresar
    def total_countries(self):
        print("     Ingresa la siguiente información: \n")
        print("============================================")
        while True:
            try:
                number_countries= int(input("Cantidad a añadir: "))
                for country in range(number_countries):
                    self.country_name= input("      País>> ")
                    while True:
                        try:
                            self.population= int(input("        Población>> "))
                            self.continent= input("     Continente>> ")
                            print("--------------------------------------------------")
                            #Añadimons una tupla a la lista append((Valores de la tupla))
                            self.countries_list.append((self.country_name, self.population, self.continent))
                            break
                        except ValueError:
                            print(">> Se esperaba un valor numérico <<")
                print(self.total_countries)
            except ValueError:
                print("Error en el tipo de dato")