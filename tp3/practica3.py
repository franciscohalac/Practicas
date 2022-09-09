import os, glob 

#1
def cuantas_no (letra, erchivo):
    contador = 0
    with open(erchivo, "r") as file:
        for line in file:
            if line[0].upper != letra.upper():
                contador += 1
    print ("Hay", contador, "archivos que no empiezan con", letra)

#2
def leer_n_lineas(archivo, lineas):
    variable = open(archivo, "r").readlines()[:lineas]
    print(*variable)
    
#3
def ultimas_lineas(archivo, ultimas):
    lineas = open(archivo, "r").readlines()[-ultimas:]
    print(*lineas) 

#4
def contar_palabras(archivo):
    file = open(archivo,"r")
    leer = file.read()
    dividir = leer.split()
    print("El archivo tiene", len(dividir), "palabras")
#5
def reemplazar (entrada, salida, letra):
    with open(entrada, "r") as f, open(salida, "w") as s:
        for line in f:
            s.write(line.replace(letra, letra, + "\n"))

reemplazar("documento", "documento2", "f")

#6


#7
def palabra_larga(archivo):
    file = open(archivo,"r")
    leer = file.read()
    dividir = leer.split()
    final = ""
    for palabra in dividir :
        if len(palabra) > len(final):
            final = palabra
    print("la palabra mas larga es", final, "con", len(final), "letras")

#8


#9


#10
def unir_txt (carpeta1, nombre):
    os.chdir(carpeta1)
    textos = glob.glob("*.txt")
    with open("resultado/"+ nombre, "a") as salida:
            for archivo in textos:
                with open(archivo, "r") as texto:
                    salida.write(texto.read()+ "\n")
