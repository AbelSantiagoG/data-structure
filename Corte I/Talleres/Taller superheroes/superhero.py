from colorama import Back, Fore, init
class SuperHero:
    def __init__(self):
        self.superheros_marvel_list=[]
        self.superheros_dc_list= []
        self.menu_option= 0
        self.superheros=[]
        self.menu_option2= 0
    
    def menu_total(self):
        while True:
            try:
                self.menu_option2= int(input("\n       1. Crear un superhéroe\n       2. Buscar un superhéroe\n       3. Eliminar un superhéroe\n       4. Mas superpoderes\n       5. Menos superpoderes\n       6. Marvel y DC\n       7. Salir\n>>>"))
                if self.menu_option2 < 1 or self.menu_option2 > 7:
                    print("\nOpcion inválida")
                
                elif self.menu_option2 == 1:
                    print("\n CREAR SUPERHÉROE: ")
                    self.initial_menu()
                
                elif self.menu_option2 == 2:
                    print("\n BUSCAR SUPERHÉROE: ")
                    self.find_superhero()
                
                elif self.menu_option2 == 3:
                    print("\n ELIMINAR SUPERHÉROE: ")
                    self.delete_superhero()
                
                elif self.menu_option2 == 4:
                    print("\n MAS SUPERPODERES: ")
                    self.powerful_superhero()
                
                elif self.menu_option2 == 5:
                    print("\n MENOS PODERES: ")
                    self.weaker_superhero()
                
                elif self.menu_option2 == 6:
                    print("\n LISTA CONJUNTA: ")
                    self.marvel_and_dc()
                
                else:
                    print("Saliendo...\n")
                    break
            except ValueError:
                print("\nOpción inválida")
    
    def initial_menu(self):
        #Cantidad de superhéroes de DC
        number_of_superheros= 0
        #Nombre del superhéroe
        super_hero_name= " "
        #Cantidad de poderes superhéroe
        number_of_powers= 0
        #Poder (si tiene uno solo)
        super_hero_power= ""
        #poder para añadir a la lista
        power= ""
        #Cantidad de creadores
        number_of_creators= 0
        #Nombre del creador(si es uno solo)
        created_by= ""
        #creador para añadir a la lista
        creator= ""

        print("\n>>>>>>>>>>>>>>Seleccione una opción del menú<<<<<<<<<<<<<<<<")
        while True:
            try:
                self.menu_option= int(input("\n       1. Marvel\n       2. DC\n       3. Salir\n\n >>>"))
                if self.menu_option < 1 or self.menu_option > 3:
                    print("\nOpcion inválida")

                elif self.menu_option == 1:
                    print("\nMarvel:")
                    number_of_superheros= int(input("\n¿Cuántos superhéroes desea añadir?\n>"))
                    for i in range(0, number_of_superheros):
                        #Lista de superpoderes
                        super_hero_powers_list=[]
                        #Lista de creadores
                        creators_list= []

                        super_hero_name= input(f"Ingrese el nombre del superhérore {i+1}\n").upper()
                        number_of_powers= int(input("Ingrese la cantidad de poderes que tiene \n"))
                        for i in range(0,number_of_powers):
                            power=input("Ingrese el poder\n")
                            super_hero_powers_list.append(power)
                        number_of_creators=int(input("Ingrese la cantidad de creadores \n"))
                        if number_of_creators==1:
                            created_by= input("Ingrese el creador\n")
                        else:
                            for i in range(0, number_of_creators):
                                creator=input("Ingrese el creador\n")
                                creators_list.append(creator)
                        
                        if number_of_creators==1:
                            self.superheros_marvel_list.append((super_hero_name,super_hero_powers_list,created_by))
                            self.superheros.append((super_hero_name,super_hero_powers_list,created_by))
                        else:
                            self.superheros_marvel_list.append((super_hero_name, super_hero_powers_list, creators_list))
                            self.superheros.append((super_hero_name, super_hero_powers_list, creators_list))
                    print(self.superheros_marvel_list)

                elif self.menu_option == 2:
                    print("\nDC")
                    number_of_superheros= int(input("\n¿Cuántos superhéroes desea añadir?\n>"))
                    for i in range(0, number_of_superheros):
                        #Lista de superpoderes
                        super_hero_powers_list=[]
                        #Lista de creadores
                        creators_list= []

                        super_hero_name= input(f"Ingrese el nombre del superhérore {i+1}\n").upper()
                        number_of_powers= int(input("Ingrese la cantidad de poderes que tiene \n"))
                        for i in range(0,number_of_powers):
                            power=input("Ingrese el poder\n")
                            super_hero_powers_list.append(power)
                        number_of_creators=int(input("Ingrese la cantidad de creadores \n"))
                        if number_of_creators==1:
                            created_by= input("Ingrese el creador\n")
                        else:
                            for i in range(0, number_of_creators):
                                creator=input("Ingrese el creador\n")
                                creators_list.append(creator)
                        
                        if number_of_creators==1:
                            self.superheros_dc_list.append((super_hero_name,super_hero_powers_list,created_by))
                            self.superheros.append((super_hero_name,super_hero_powers_list,created_by))
                        else:
                            self.superheros_dc_list.append((super_hero_name, super_hero_powers_list, creators_list))
                            self.superheros.append((super_hero_name, super_hero_powers_list, creators_list))
                    print(self.superheros_dc_list)

                else:
                    print("\nSaliendo...")
                    break

            except ValueError:
                print("\nError en la opción indicada")

    def find_superhero(self):
        name=input("Ingrese el nombre del superhéroe que desea buscar\n")
        search= False
        for i in self.superheros:
            if name.upper() in i[0]:
                print(i[1])
                search= True
        if not search:
            print("No se encuentra el superhéroe")
            add_superhero=int(input("¿Desea añadir al superheroe?\n \n1. Si\n2. No\n\n"))
            if(add_superhero==1):
                self.initial_menu()
            else:
                print("\nNo añadir\n")
    
    def delete_superhero(self):
        name=input("\nIngrese el nombre del superhéroe que desea eliminar\n")
        search= False
        for hero in self.superheros_marvel_list:
            if name.upper() in hero[0]:
                self.superheros_marvel_list.remove(hero)
                print(self.superheros_marvel_list)
        for hero in self.superheros_dc_list:
            if name.upper() in hero[0]:
                self.superheros_dc_list.remove(hero)
                print(self.superheros_dc_list)
        for hero in self.superheros:
            if name.upper() in hero[0]:
                self.superheros.remove(hero)
                print(self.superheros)
                search=True
        if not search:
            print("No se encuentra el superhéroe")
    
    def powerful_superhero(self):
        mayor= -99999
        for hero in self.superheros:
            if len(hero[1])>mayor:
                mayor=len(hero[1])
                he=hero
        print(f"El superhéroe con más poderes es: {he[0]}")
    
    def weaker_superhero(self):
        menor= 999999
        for hero in self.superheros:
            if len(hero[1])<menor:
                menor=len(hero[1])
                he=hero
        print(f"El superhéroe con menos poderes es: {he[0]}")
    
    def marvel_and_dc(self):
        print(self.superheros)