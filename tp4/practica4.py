import re

#1
def caracteres_permitidos(string):
    return bool(re.search("[a-zA-Z0-9]",string))

#2
def todos_caract_permitidos(string):
    return not bool(re.search("[^a-zA-Z0-9]",string))

#3
def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else: 
        return"No se encontró patrón"

def encontrar_patron(string):
    patron = "he+"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else: 
        return"No se encontró patrón"

#
def encontrar_patron(string):
    patron = "he{2,3}"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else: 
        return"No se encontró patrón" 

#4
def palabras_u(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else: 
        return"No se encontró patrón" 

#5
def numero_especifico(numero, string):
    if re.match(str(numero),string) is not None:
        return "Empieza con numero"
    else:
        return "No empieza con numero"

#6
def frase_en_lista(frase, lista):
    for elem in lista:
        if re.search(elem,frase) is  None:
            return "String no se encuentra en la frase"
    else:
        return "Todos los strings en la frase"
print(frase_en_lista("hola mundo", ["hola","casa"]))

def solo (string):
    bool(re.search("[a-zA-Z0-9]",string)) #le falta, no se como poner espacios y que no tenga mas cosas

#Escribir una función que, dado una lista de telefonos, permita validar si estos corresponden 
# o no con un teléfono de CABA.


def telefono (numero):
    patron = "[+]54\s011"
    if re.match(patron, numero) != None:
        print("Es de CABA")
    else:
        print("No es de CABA")

telefono("+54 351 5557162")

#11
def arrancaP(lista):
    contador = 0
    for elem in lista:
        if re.match("^(P)", elem):
            contador += 1
    if contador > 1 :
        print(True)
    else:
        print(not bool)

arrancaP(["Práctica Python", "práctica C++", "Práctica Fortran"])

#8
def numeros(string):
    print(re.findall("\d+", string))
numeros("slbvs4jbv77vdsjv88svjv4")

#9
def entre (string):
    print(re.findall("-(.*?)-", string))

entre("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
