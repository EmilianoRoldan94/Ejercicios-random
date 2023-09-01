'''Realizar un programa que tenga una clase Persona con las
siguientes características. La clase tendrá como
atributos el nombre y la edad de una persona. Implementar
los métodos necesarios para
inicializar los atributos utilizando el constructor (__init__),
mostrar los datos e indicar si la persona es
mayor de edad o no.
¡Utilice el constructor!'''

class Persona():
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        
    def legal(self):
        if self.edad < 18:
            print(self.nombre,"es MENOR DE EDAD.\n")
        else:
            print(self.nombre,"es mayor de edad.\n")
            
person1 = Persona("Juanito", 24)
person2 = Persona("Lara", 1)

person1.mostrar()
person1.legal()
person2.mostrar()
person2.legal()