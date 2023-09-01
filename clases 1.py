class Alumno():
    def ingresoDato(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)
        
    def resultado(self):
        if self.nota < 5:
            print("El alumno ",self.nombre," ha desaprobado")
        else:
            print("El alumno ",self.nombre," ha aprobado")
            
alumno1 = Alumno()
alumno2 = Alumno()

alumno1.ingresoDato("Juanito",7)
alumno2.ingresoDato("Pedrito",4)

alumno1.mostrar()
alumno1.resultado()
print()
alumno2.mostrar()
alumno2.resultado()