# #1
# palabra = input("introducir palabra: ")
# print(palabra[0] == palabra[0].upper())

#2
# numero = int(input("introducir número entero: "))
# if numero > 0 :
#     print("Es positivo")
# elif numero < 0:
#     print("Es negativo")

# if numero == 0:
#     print("Es Cero")

# if numero % 2 == 0:
#     print("Es par")
# else:
#     print("Es impar")

#3
# dado = int(input("Número del dado: "))
# if dado > 0 and dado < 7:
#     print("La cara opuesta del dado es", 7-dado )
# else:
#     print("El número ingresado es incorrecto")

#4
# peso = int(input("peso del paquete en kg: "))
# zona = input("zona a la que enviará su paquete: ")
# if peso > 5 :
#     print("El paquete no puede ser enviado ya que el peso es superior a 5 kg")
# elif zona.upper() == "AMÉRICA DEL SUR":
#     print("El costo es de 10.00 dólares")
# elif zona.upper() == "AMÉRICA CENTRAL":
#     print("El costo es de 15.00 dólares")
# elif zona.upper() == "AMÉRICA DEL NORTE":
#     print("El costo es de 18.00 dólares")
# elif zona.upper() == "EUROPA":
#     print("El costo es de 24.00 dólares")
# elif zona.upper() == "ASIA":
#     print("El costo es de 30.00 dólares")
# else:
#     print("Esta zona no está disponible")

#5
# dia = int(input("introducir numero del día de la semana: "))
# if dia == 1:
#     print("lunes")
# elif dia == 2:
#     print( "martes")
# elif dia == 3:
#     print("miercoles")
# elif dia == 4:
#     print("jueves")
# elif dia == 5 :
#     print("viernes")
# elif dia == 6:
#     print("sabado")
# elif dia == 7:
#     print("domingo")
# else:
#     print("el numero ingresado no corresponde a un dia de la semana")

#6
# lista1 = []
# lista1.append(input("Cadena 1: "))
# lista1.append(input("Cadena 2: "))
# lista1.append(input("Cadena 3: "))
# lista1.append(input("Cadena 4: "))
# lista1.append(input("Cadena 5: "))
# lista1.reverse()
# print(lista1)

#7
# lista=[]

#8
# lista1 = [
#     int(input("ingresar numero 1a: ")),
#     int(input("ingresar numero 2a: ")),
#     int(input("ingresar numero 3a: ")),
#     int(input("ingresar numero 4a: ")),
#     int(input("ingresar numero 5a: ")),]
# lista2 = [
#     int(input("ingresar numero 1b: ")),
#     int(input("ingresar numero 2b: ")),
#     int(input("ingresar numero 3b: ")),
#     int(input("ingresar numero 4b: ")),
#     int(input("ingresar numero 5b: ")),]
# lista3 = []

# lista3.append(lista1[0] + lista2[0])
# lista3.append(lista1[1] + lista2[1])
# lista3.append(lista1[2] + lista2[2])
# lista3.append(lista1[3] + lista2[3])
# lista3.append(lista1[4] + lista2[4])
# print(lista3)

#9

# nombre_edad = {}
# print ("Escriba Nombre-Apellido y Edad. Utilizar * para finalizar")
# while True:
#     nombre_apellido = input("Nombre y apellido: ")
#     edad = input("Edad: ")
#     if nombre_apellido != "*":
#         nombre_edad[nombre_apellido]=edad

#     else:
#         break

# edad_max = 0
# for nombre in nombre_edad:
#     if int(nombre_edad[nombre])  > int(edad_max):
#         edad_max= nombre_edad[nombre] 

# print("la edad maxima es de", edad_max, "años, y es", nombre )

#10
# dic = {}
# palabra = input("introducir palabra: ")
# for letra in set(palabra):
#     dic[letra] = 0
# for letras in palabra:
#     dic[letras] = dic[letras]+1
# print(dic)

#12
# dic = {}
# cantidad = int(input("Cantidad de alumnos a introducir: "))
# while True:
#     print("colocar * para terminar de cargar alumnos")
#     nombre_apellido = input("Nombre y apellido: ")
#     if nombre_apellido != "*":
#         while True:
#             print("cargar notas y colocar numero negativo para pasar al siguiente alumno")
#             nota = int(input("nota: "))
#             if nota > -1 :
#                 if nombre_apellido not in dic:
#                     dic[nombre_apellido] = [nota]
#                 else:
#                     dic[nombre_apellido].append(nota)
#             else: 
#                 break
#     else:
#          break
# final = {}
# for nombre in dic:
#     final[nombre]=(sum(dic[nombre])/len(dic[nombre]))
# print(final)

#13
# def es_multiplo (num1, num2):
#     if num1 / num2 == int(num1/num2) or num2 / num1 == int(num2/num1): 
#         print("son multiplos")
#     else:
#         print("no son multiplos")

#14
# def promedio(max, min):
#     print("temperatura promedio",(max+min)/2, "grados")

# cantidad = int(input("numero de dias ue se van a ingresar: "))
# contador = 0
# while True:
#     if contador < cantidad:
#         maxima = int(input("temperatura maxima: "))
#         minima = int(input("temperatura minima: "))
#         promedio(maxima,minima)
#         contador += 1
#     else:
#         break

#15
dic={
1:["Florencia Ocampo", "14/09/2001", "si"],

2:["David Estévez", "14/09/2001", "si"],

3:["Sofía Cáceres", "14/09/2001", "si"]
}
while True:
    print("cargar numero de socio, para finalizar colocar 0 ")
    numero = int(input("numero de socio: "))
    if numero != 0:
        nombre = input("nombre del socio: ")
        fecha = input("fecha de ingreso: ")
        cuota = input("cuota al dia si/no: ")
        dic[numero]= [nombre, fecha, cuota]
    else:
        break
print("El club tiene", len(dic), "socios.")

verificar = input("¿Verificar cutas de socios? si/no: ")
if verificar.upper() == "SI":
    while True:
        print("Para terminar, ingresa 0")
        socio = int(input("nro de socio: "))
        if socio != 0:
            if socio not in dic:
                print("Socio no existente")
            else:
                if dic[socio][-1].upper() == "SI":
                    print("El socio", dic[socio][0], "NO tiene deudas")
                else:
                    print("El socio", dic[socio][0], "tiene deuda")
        else:
            break
else:
    pass

dic_copy = {}
eliminar = input("Eliminar socio si/no: ")
if eliminar.upper() == "SI":
    while True:
        print("Para terminar, ingresa 0")
        elim = input("nombre de socio: ")
        if elim != "0":
            for elem in dic:
                if elim.upper() != dic[elem][0].upper():
                    dic_copy[elem]=dic[elem]
                    
        else:
            break
else:
    pass
dic = dic_copy

cambiar = input("Cambiar fecha socios si/no: ")
if cambiar.upper() == "SI":
    while True:
        print("Para terminar, ingresa 0")
        elim = input("fecha a cambiar: ")
        if elim != "0":
            fecha_nueva= input("nueva fecha: ")
            for elemento in dic:
                if dic[elemento][1] == elim:
                    dic[elemento][1]=fecha_nueva
        else:
            break
else:
    pass

print(dic)


