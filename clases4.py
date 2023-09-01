'''Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el
método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método
para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.'''

class Calculadora():
    num1 = 0
    num2 = 0
    def __init__(self):
        self.num1 = int(input("Dame un entero: "))
        self.num2 = int(input("Dame otro entero: "))
        
    def suma(self):
        print(self.num1,"+",self.num2,"=",self.num1+self.num2)
    def resta(self):
        print(self.num1,"-",self.num2,"=",self.num1-self.num2)
    def multi(self):
        print(self.num1,"*",self.num2,"=",self.num1*self.num2)
    def div(self):
        print(self.num1,"/",self.num2,"=",self.num1/self.num2)
        
ejer1 = Calculadora()

ejer1.suma()
ejer1.resta()
ejer1.multi()
ejer1.div()