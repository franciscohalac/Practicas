#Lectura & Escritura de archivos con Python

# Desafío II: Investigá sobre los métodos os.mkdir() y os.listdir()

# os.mkdir es una orden de los sistemas operativos UNIX, DOS, OS/2 y Microsoft Windows 
# usada para crear un nuevo subdirectorio o carpeta del sistema de archivos.

# La función os. listdir() devuelve una lista que contiene los nombres de las entradas 
# (archivos y directorios) del directorio indicado (path). La lista no sigue ningún tipo 
# de orden y no se incluyen las entradas

# Desafío III: Abrí el archivo bio.txt y escribí una mini biografía de presentación. 
# Para pensar 🤔:¿Cómo darías formato al texto que estas creando?


with open("bio.txt" , "a") as file:
    file.write("Hola mundo, soy francisco Halac ")

bio = open("bio.txt", "r")
bio.read()

bio = open("bio.txt", "r")
bio.readlines()