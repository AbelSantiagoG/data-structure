'''
data type: list practice
Date: 25/01/23
'''

# 1. Declarar la clase
class ListPractice:
    # 2. Crear una función incializadora de la clase
    def __init__(self):
        # 3. Definir las variables goblales de la clase
        self.student_name = " "
        self.courses_list = ["POO", "TAD"]

    #4. Funcion customizada
    def show_info_list(self):
        #Imprimir el contenido de la lista courses_list
        print(self.courses_list)
        #Cantidad de elementos que tiene la lista
        print(len(self.courses_list))

    #5. Funcion que solicita informacion al usuario 
    def input_data_course(self):
        #1. Declaramos una variable a nivel de método
        print("Ingrese la siguiente información: ")
        #solicitud de texto
        self.student_name= input("Nombre: ")
        #solicitud de números enteros
        courses_number= int(input("Cantidad de asignaturas: "))
        #Validamos que el courses_number sea menor que el tamaño de la lista
        if courses_number <= len(self.courses_list):
            print(">> Error: Cursos a inscribir es menor que 2 <<")
        else:
            #Solicitar nombre de las asignaturas al usuario
            for course in range(courses_number-len(self.courses_list)):
                #Variable que almacena el nombre de la asginatura
                course_name= input("Nombre de la asignatura: ")
                if(course_name in self.courses_list):
                    print("Esa materia ya se encuentra inscrita")
                else:
                    #Añadimos elementos al final de la lista
                    self.courses_list.append(course_name)
            #Imprimir contenido de la lista
            print(self.courses_list)