#Para pensar 🤔: ¿Qué usos crees que podemos darle a las expresiones regulares? 
# Proponé una aplicación concreta para tu carrera/disciplina.

"""Nos sirven para identificar patrones en datos por ejempo y de esa forma rescatarlos y luego
utilizarlos para tomar desiciones."""

#Para pensar 🤔: Dado el siguiente texto:

# texto = 'Esta es la linea uno\npalabra en la linea dos\n'
# ¿Cómo crees que darán las siguientes búsquedas?

# expresion regular a: '^palabra'

"Palabra al inicio del linea"

# expresion regular b: '\Apalabra'

"palabra al inicio de texto"

# expresion regular c: 'palabra$'

"palabra al final de linea"

# expresion regular d: 'palabra\Z'

"palabra al final de texto"

# Para pensar 🤔: ¿Qué significará la expresión regular "X(.*)Y"? 
# Ennumera algunas de las posibles strings que cumplen con dicha condición.



# 🧗‍♀️ Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?

"\d{4,}"

# 🧗‍♀️ Desafío II: ¿Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas?

"[a-z]{3,6}"

# 🧗‍♀️ Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del 
# patrón ab en un string?

"ab*"

# 🧗‍♀️Desafio IV: ¿Qué expresión regular usarías para extraer el número de estudiantes que hay en una clase según el siguiente texto:

# texto = 'En la clase de Introducción a la programación hay 30 estudiantes' 

"/d+"
"nota: \d Caracter numércio y + Una o más ocurrencias del patrón"

#Para pensar 🤔: ¿Existe una única respuesta para los ejercicios?
"NO, hay muchas alternativas"

import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.search(patron, texto))

#Para pensar 🤔: ¿Qué resultado obtenemos al ejecutar en la última linea?

"<re.Match object; span=(22, 26), match='amet>'"

# 🧗‍♀️Desafio V: imprimí el fragmento del texto entre la posición 22 y 26 
# ¿Qué resultado obtenés? ¿Qué quiere decir el mensaje span?

print(texto[22:26])

"obtengo la palabra que buscaba, span es un contenedor en línea."


import re
texto2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron2 = "amet"
print(re.match(patron2, texto2))

#Para pensar 🤔: ¿Qué resultado obtenemos con search()?¿Qué diferencias observan con match()?

"""El función match() de re busca el patrón y devuelve la primera aparición y 
solo al principio de la cadena. Si se encuentra una coincidencia en la primera 
línea, devuelve el objeto de coincidencia. Pero, si se encuentra una coincidencia 
en alguna otra línea, devulve un valor nulo."""

import re
texto3 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron3 = "amet"
print(re.search(patron3, texto3).group())

#Para pensar 🤔: ¿Qué resultado obtenemos? ¿Para qué sirve la función group()?

"obtenemos la palabra que buscamos. agrupa el span"

print(re.findall(patron, texto))

# Para pensar 🤔: ¿Qué resultado obtenemos?

"['amet', 'amet']"

print(re.sub(patron, "###", texto))

# Para pensar 🤔: ¿Qué resultado obtenemos? ¿Para qué sirve la función sub?

"""Lorem ipsum dolor sit ###, consectetur adipiscing elit. Amet et ###.
reemplaza el patron por ###"""