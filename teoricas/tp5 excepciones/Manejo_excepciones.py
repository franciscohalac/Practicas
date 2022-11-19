#Manejo de Excepciones con Python

import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b -cmath.sqrt(d)/(2*a))
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

#Para pensar 🤔: ¿Qué tipo de error se obtiene al ejecutar el programa? 
# ¿En dónde se encuentra el error? 
# ¿Cómo te das cuenta?

# primero da error de que falta cerrar paréntesis
# el otro problema fue la divición por 0, la cual se vio en clases.
# ZeroDivisionError: division by zero

>>> print(divisor)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'divisor' is not defined

# Para pensar 🤔: ¿Qué nos dice el mensaje de excepción? ¿Qué es la excepción de nombre?

#La exepción "name" es de que no está definido ese elemento. 

>>> 0 + "2"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

#Para pensar 🤔: ¿Qué nos dice el último mensaje de excepción? ¿Qué es la excepción de tipo?

#Ese tipo de excepción nos indica que no podemos utilizar el operador suma
#para string u numero. (int and str) es decir que el "2" de la suma es "str".

try:
    # aquí ponemos el código que puede lanzar excepciones
except:
    # entrará aquí en caso que se haya producido una excepción

#Para pensar 🤔: ¿Qué tipo de excepción se maneja en el código anterior?

#Todo tipo de excepciones.



#🧗‍♀️Desafio II: Creá una función denominada mitades que tenga como argumento un número 
# e imprima el resultado de la división de ese número por 2

#Para pensar 🤔: ¿Qué crees que ocurrirá cuando ingresas un 9 como parámetro? ¿Y con un 0?

#🧗‍♀️Desafio III: ¿Cómo mejorarías tu función para que sea capaz de manejar el error
#  de la división por cero? Reescribí la función incorporando una declaración try-except

try:
    def mitades (numero):
        return numero/2
except:
    "Divición por cero"

#cuando ingrese el 9 me va a devolver 4,5.
#cuando ingrese el 0 me va a retornar ZeroDivisionError: 

