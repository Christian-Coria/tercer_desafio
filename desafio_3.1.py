

#1) Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
#Mostrar una suma de los dos números
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números
#Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará.
#En caso de no introducir una opción válida, el programa informará de que no es correcta.


print("""Desafío entregable 3 (Clase 5)
Control de flujo
""")
#solicitamos la introduccion de los numeros por teclado almacenandolas en sus rspectivas variables
#seguidamente debe elejir una de cuatro opciones, la cual sera validada dentro de un ciclo while
numero1 = int(input("Ingrese el Primer Numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
print("""
Elija una opcion:
1- Suma
2- Resta
3- Multiplicacion
4- Finalizar
""")
opcion = int(input("Elija una opcion:  "))

while (opcion !=5):
    if opcion == 1:
        resultado = numero1 + numero2
        print (f"El Resultado de la Operacion es {resultado}")
        break
    elif opcion == 2:
        resultado = numero1 - numero2
        print (f"El Resultado de la Operacion es {resultado}")
        break
    elif opcion == 3:
        resultado = numero1 * numero2
        print (f"El Resultado de la Operacion es {resultado}")
        break
    elif opcion == 4:
        print("Programa finalizado.....")
        break
    else:
        print ("La opcion elejida es incorrecta!...")
        break
      
