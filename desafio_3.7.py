lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

#concatenamos las listas para tener ambas en otra lista y posteriormente convertimos la lista en un sets
# que por su caracteristica no permite valores duplicados
lista_3 = lista_1 + lista_2
lista_3 = set(lista_3)
#convertimos el conjunto set en una lista nuevamente con la funcion list()
lista_3 = list(lista_3)
print(lista_3)
