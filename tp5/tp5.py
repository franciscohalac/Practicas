"Manejo de excepciones"

lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabón", "alcohol"]
try:
    lista_super + "arroz"
except:
    print("no puedo agregar arroz")

#¿Es correcto el uso del try...except? ¿Qué cosa/s le modificarías?

"Debería agregar al lado del except el tipo de error que espero."

#2
"""Definir una función que tenga como parámetros una lista de números por un lado y
un número por otro y devuelva una lista con la división de cada elemento por el número dado.
 Por ejemplo, si le paso ([2,4,6,8], 2), debería retornar [1,2,3,4]. Tomar las precauciones necesarias."""

try:
    def funcion(lista,num):
        lis = []
        for elem in lista:
            lis.append(elem/int(num))
        print(lis)

    funcion([2,4,6,8], "hola")
    
except ZeroDivisionError:
    print("error divición por cero")
except:
    print("otro error")

#3
"""Definir un procedimiento, que reciba una lista y un número, el cual tiene que agregar
el número a la lista solo si el número es positivo. De lo contrario debería generar un 
error indicando que el número no es positivo."""

try:
    list = []
    while True:
        print("Ingresa los numeros de la lista, escriba 000 para finalizar la lista")
        lista = int(input("introducir numero de lista: "))
    
        if lista != -0:
            list.append(lista)
        else:
            break

    num = int(input("introducir numero: "))
   
    if num >= 0 :
        list.append(num)
        print(list)
    
    else:
        print("numero no ingresado menor a 0")

except ValueError:
    print("Error ValueError, ingresar solo numeros")

except:
    print("otro error")
