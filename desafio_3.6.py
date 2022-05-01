print("Todos los números del 0 al 10 [0, 1, 2, ..., 10]")
lista1 = list(range(11))
print(lista1)
 
print("Todos los números del -10 al 0 [-10, -9, -8, ..., 0]")
lista2 = list(range(-10,1))
print(lista2)
 
print("Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]")
lista3 = list(range(0,21))
lista3_1 = lista3[0:21:2]
print(lista3_1)
 
print("Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]")
lista4 = list(range(-19,0))
lista4_1 = lista4[0:20:2]
print(lista4_1)
 
print("Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]")
lista5 = list(range(0,51))
lista5_1 = lista5[0:52:5]
print(lista5_1)
 
 
