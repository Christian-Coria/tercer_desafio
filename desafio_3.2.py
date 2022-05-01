
#creamos la variable x donde se almacena el numero entero que introduce el usuario
x = int(input("Introduce un numero Impar :"))
#iniciamos el ciclo while para que mientras sea true el ingreso de un numero par siga solicitando el numero
while x  %2 == 0 :
    print (f"ERROR, el valor {x} introducido es par, Prueba Nuevamente...")
    x = int(input("Introduce un numero Impar :"))  
#al volverse false el ciclo por ser impar imprimimps el mensaje terminando el programa
else:
    print (f"el valor {x} es Impar!")
