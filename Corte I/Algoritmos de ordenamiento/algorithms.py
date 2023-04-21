from random import sample
from colorama import Fore, Back, init

class SortAlgorithms:
    def __init__(self):
        self.number_list= range(100)
        self.list_bubble_sort= sample(self.number_list,8)
        self.list_select_sort= sample(self.number_list,8)
        self.list_insert_sort= sample(self.number_list,8)
        self.list_merge_sort= sample(self.number_list,8)
        self.list_quick_sort= sample(self.number_list,8)
        self.list_radix_sort= sample(self.number_list,8)
        
    
    #Ordenamiento burbuja
    def bubble_sort_function(self):
        #Comparando por pares, inciamos comparando los 2 primeros elementos
        print(Fore.CYAN + "-------------------------------------------"+Fore.RESET)
        print(Fore.GREEN + "           Ordenamiento burbuja" + Fore.RESET)
        #Crear un contador para conocer la cantidad de elementos de la lista
        count_item_list= 0
        #Recorremos la lista self.list_bubble_sort
        for i in self.list_bubble_sort:
            #Al contador de elementos, cada vez que visitemos una posicion le sumamos 1:
            count_item_list+= 1
        print(self.list_bubble_sort)

        #Recorremos la lista e iniciamos la comparacion de valor
        print("Primer for contador-1:  ", count_item_list-1)
        for j in range (count_item_list-1):
            print(Fore.RED + str(j) + Fore.RESET)
            for k in range (count_item_list-j-1):
                print(Fore.BLUE + str(k) + '-' + str(k+1) + Fore.RESET)
                #Comparamos el valor de la poscion actual con el valor de la siguiente posición
                if(self.list_bubble_sort[k]>self.list_bubble_sort[k+1]):
                    self.list_bubble_sort[k], self.list_bubble_sort[k+1]= self.list_bubble_sort[k+1], self.list_bubble_sort[k]
        print(self.list_bubble_sort)

    def bubble_sort_function_refactor(self):
        change_position= True
        while change_position:
            change_position=False
            for i in range(len(self.list_bubble_sort)-1):
                if(self.list_bubble_sort[i]>self.list_bubble_sort[i+1]):
                    self.list_bubble_sort[i], self.list_bubble_sort[i+1]= self.list_bubble_sort[i+1], self.list_bubble_sort[i]
                    change_position= True
        print(self.list_bubble_sort)

    def select_sort_function(self):
        print(Fore.CYAN + "-------------------------------------------"+Fore.RESET)
        print(Fore.GREEN + "           Ordenamiento selection sort" + Fore.RESET)
        count_item_list = 0
        for i in self.list_select_sort:
            count_item_list+= 1
        #Recorremos la lista y generamos la comparación de valores entre posiciones
        for i in range (count_item_list):
            min= i
            print(Fore.RED + str(i) + Fore.RESET)
            for j in range(i+1, count_item_list):
                print(Fore.BLUE + str(j) + Fore.RESET)
                #Comparación de valores
                print("Comparacion: " + Fore.BLUE + str(self.list_select_sort[min]) + ' - ' + str(self.list_select_sort[j]) + Fore.RESET)
                if self.list_select_sort[min] > self.list_select_sort[j]:
                    min=j
            #Generamos el intercambio
            self.list_select_sort[i], self.list_select_sort[min] = self.list_select_sort[min], self.list_select_sort[i]
        print(self.list_select_sort)

    def insert_sort_function(self):
        print(Fore.CYAN + "-------------------------------------------"+Fore.RESET)
        print(Fore.GREEN + "         Ordenamiento de insertion" + Fore.RESET)
        #Separamos la lista en 2 partes (puede o no estar) ordenada
        print(self.list_insert_sort)
        for i in range(1, len(self.list_insert_sort)):
            item_visited= self.list_insert_sort[i]
            #Visitamos la posición anterior a la actual
            j= i-1
            #Todos los elementos de valor mayor pasan adelante
            while j >= 0 and self.list_insert_sort[j]> item_visited:
                print(Fore.CYAN + str(self.list_insert_sort[j]) + Fore.RESET + ">" + str(item_visited))
                self.list_insert_sort[j+1] = self.list_insert_sort[j]
                j -= 1
            self.list_insert_sort[j+1]= item_visited
        print(self.list_insert_sort)
    
    def merge_sort_function(self):
        print(Fore.CYAN + "-------------------------------------------"+Fore.RESET)
        print(Fore.GREEN + "          Ordenamiento merge sort" + Fore.RESET)