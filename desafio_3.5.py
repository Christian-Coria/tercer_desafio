numeros = [1, 3, 6, 9]
# pedimos que el usuario ingrese un numero entero
num = int(input("ingrese un numeros entre 0 y 9:  "))
# iniciamos el ciclo while 
while num  % 3 != 0:
    if  num != 1:  
        print("Numero ingresado no esta en lista, Continuamos...")
        num = int(input("ingrese un numeros entre 0 y 9:  "))
    
    # en esta instancia nos aseguramos que si no esta dentro del rango 
    # vueva a pedir el numero hasta que sea correcto
    else:     
        break
        # imprimimos el mensaje y el valor boolean de si esta o no en lista el numero ingresado
print("El numero es ingresado,se encuentra en la lista, tiene un valor booleano de :")
print(num in numeros)