'''Escriba un programa que permita cargar por teclado un vector de 10 posiciones, con
números enteros, luego debe mostrar los números pero si el número termina en 3 8 4 9 debe
agregar un * antes de mostrar el número (investigue cómo obtener un ultimo digito de un
número).'''

import array as arr

def cargaNumInt(texto):
    while True:
        try:
            num = int(input(texto))
            return num
        except ValueError:
            print("ERROR: ", ValueError)
            input("Debe ser un valor entero. Pulse Enter para continuar")

def comprobarDesc(lista):
    descarte = [3,8,4,9]
    for i in lista:
        temp = i % 10
        if temp in descarte:
            print("*",i,end=' ')
        else:
            print(i,end=' ')

vector = arr.array('i', [])

for x in range(10):
    vector.append(cargaNumInt("Ingrese un numero entero: "))

comprobarDesc(vector)