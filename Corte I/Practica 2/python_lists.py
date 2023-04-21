'''
List methods
Date: 27/01/23
'''
class ListMethods:
    #1. Método inicializador de la clase
    def __init__(self):
        #Definimos una lista vacía
        self.pets= []
        self.vehicles= list()

    #2. Método para añadir elementos en la lista
    def add_list_elements(self):
        #["dog", "cat"]
        self.pets.append("dog")
        self.pets.append("cat")
        print(self.pets)

    #3. Método que solicita valores al usuario
    def input_data_vehicles_list(self):
        #Variables locales: vehicles_number, vehicles_type
        vehicles_number= int(input("¿Cuántos vehículos tienes? "))
        #Recorrer una lista
        for vehicle_item in range(vehicles_number):
            vehicle_type= input("Tipo de vehículo: ")
            #Añadimos vehículos a la lista
            self.vehicles.append(vehicle_type)
        #Imprimir toda la lista
        print(self.vehicles)
        #Imprimir último elemento de la lista
        print(self.vehicles[-1], self.vehicles[-2], self.vehicles[-3])

    #4. Extraer valores de una lista (imprimir)
    def show_collection_data_list(self): 
        #Imprimir desde la posición 2 hasta 4-1
        print(self.vehicles [2:4])
        #Imprimir todos los elementos de la lista
        print(self.vehicles[:])
        #Imprimir elementos desde un índice específico (desde x hasta el final)
        print(self.vehicles[2:])
        #Imprimir elementos hasta un índice específico (desde el inicio hasta x)
        print(self.vehicles[:2])
        #Acceder a los elementos de x en x (::x), de toda la lista UwU
        print(self.vehicles[::2])
        #Acceder a un subconjunto de elementos de 2 en 2
        print(self.vehicles[1:5:2])

    #5. Iterar los elementos de una lista con for
    def iterarion_list(self):
        for item in self.vehicles:
            print(item)
        #Validar si la lista contiene un valor específico
        if "caRro".capitalize in self.vehicles:
            print("No se encontró un valor")

    #6. Añadir varios elementos al final de la lista
    def add_elements(self):
        self.vehicles.extend(["Avion", "Tractomula", "Otro medio"])
        print(self.vehicles)

    #7. Añadir un elemento en posición esepcífica de la lista
    def add_specific_element(self):
        self.vehicles.insert(0, "Moto")
        print(self.vehicles)

    #8. Eliminar último elemento de la lista
    def remove_last_element(self):
        self.vehicles.pop()
        print(self.vehicles)

    #9. Eliminar elemento de posición específica
    def remove_specific_element(self):
        #Primer elemento
        self.vehicles.pop(0)
        print(self.vehicles)

    #10. Eliminar todos los valores de la lista
    """ def remove_all_elements(self):
        self.vehicles.clear() """

    #11. ELiminar de la lista un valor específico: ["Tractomula"]
    def remove_element_by_name(self):
            self.vehicles.remove("Tractomula".capitalize())
            print(self.vehicles)

    #12. Eliminar todas las coincidencias de valor encontradas en una lista
    """ def remove_all_match_elements(self):
        for item in self.vehicles:
            if(item=="Tractomula".capitalize()):
                self.vehicles.remove(item) """
    def remove_all_match_elements(self):
        new_list= list(filter("Tractomula").__ne__, self.vehicles)
        print(new_list)
    
    