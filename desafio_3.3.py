#creo variables inicianizandola en cero para definir las mismas
# incluida la variable que iterara la los numeros impares
 
sumando_impares = 0
i = 0   # se itera desde el indice 0
#creamos la lista de numeros del 0 al 99
for i in range(0,100):    
    #al iterar indicamos que revise que el resto no sea igual a cero para saber que separe solo los num impares
    if i % 2 != 0:
        sumando_impares += i  #indicamos que sume uno a uno mientras itera cada valos acumulado en la lista
 
#imprimimos la variable donde almacenamos la lista
print(sumando_impares)
