
print("Introduzca numeros (o 0< para calcular)")
#pedimos al usuario que introduzca numeros y cuando decee calcular dijite 0 
numero = int(input("Introduzca los Numeros para realizar la Media Aritmetica:   "))
#inicializo la lista vacia
numeros = []
#en el ciclo white mientas ingrese cualquier numero que no sea 0 
#utilizara el metodo append para incluir los valores a la lista he imprimirla
#al introducir numero negativo luego de mensaje del error pedimos nuevamente que ingrese numeros positivos,
# al introducir 0 salimos del ciclo y calculamos despues de imprimir la media.
while (numero > 0):
     
    numeros.append(numero)
    numero = int(input("Introduzca los Numeros positivos para realizar la Media Aritmetica:   "))    
    print(numeros)
    if numero < 0  :
        print("opcion equivocada")
        numero = int(input("Introduzca los Numeros para realizar la Media Aritmetica:   "))
    
#utilizamos el metodo len para calcular la cantidad de elementos de la lista 
#con el metodo sum. sumamamos los elementos de la lista /  dividimos ambos para sacar la Mediapor la cantidad de la misma 
# he imprimimos indicando solo dos digitos flotantes
media = sum(numeros) / len(numeros)
print(f"la media de los numeros introducidos es : {media:.2f}")

