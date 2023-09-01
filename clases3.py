'''Desarrollar un programa que cargue los datos de un triángulo.
Implementar una clase con los métodos para inicializar los
atributos, imprimir el valor del lado con un tamaño mayor y el
tipo de triángulo que es (equilátero, isósceles o escaleno).
'''

class Triangulador():
    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def mayor(self):
        print("El lado mayor mide: ",max(self.lado1,self.lado2,self.lado3),"cmts")
    
    def tipo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Es Equilatero.\n")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("Es isoseles.\n")
        else:
            print("Es Escaleno.\n")
    
tri1 = Triangulador(15,20,3)
tri2 = Triangulador(10,10,10)
tri3 = Triangulador(3,23,23)

tri1.mayor()
tri1.tipo()
tri2.mayor()
tri2.tipo()
tri3.mayor()
tri3.tipo()