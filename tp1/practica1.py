#1
palabra = input("palabra: ")
print (len(palabra))

#2
palabra2 = input("palabra2: ")
print((palabra2[4:6]).upper())

#3
nombre_y_apellido = input("nombre y apellido: ")
print("hola", nombre_y_apellido)

#4
nombre = input("nombre: ")
apellido1 = input("apellido1: ")
apellido2 = input("apellido2: ")
print((nombre[0] + apellido1[0] + apellido2[0]).upper())

#5
num1 = int(input("num1: "))
num2 = int(input("num2: "))
num3 = int(input("num3: "))
print((num1 + num2 + num3)/ 3)

#6 
minutos = int(input("minutos: "))
print(minutos//60, "horas", minutos%60, "minutos")

#7
sueldo_base = int(input("sueldo base: "))
venta1 = int(input("venta1: "))
venta2 = int(input("venta2: "))
venta3 = int(input("venta3: "))
venta4 = int(input("venta1: "))
comision = (venta1*0.1 + venta2*0.1 + venta3*0.1 + venta4*0.1)
print("comisión por ventas", comision)
print("sueldo total:", sueldo_base+comision )

#8
aprobadas = int(input("respuestas correctas: "))
desaprobadas = int(input("respuestas incorrectas: "))
blanco = int(input("respuestas en blanco: "))
print("La nota final es",((aprobadas*4 + desaprobadas*-1) * 100 / ((aprobadas+desaprobadas+blanco)*4) ),"%")

#Ejercicio en grupo I - Compra de una casa
valor_total = int(input("costo de la casa: "))
porcentaje_deposito = valor_total* 0.25
cantidad_ahorrada = 0
inversion_mensual = 0.04/12
sueldo_anual = int(input("sueldo anual: "))
porcentaje_ahorrado = float(input("porcentaje a ahorrar: "))
sueldo_mensual = sueldo_anual/12
contador = 0

while True:
    
    if cantidad_ahorrada<porcentaje_deposito:
        cantidad_ahorrada += (sueldo_mensual*porcentaje_ahorrado+sueldo_mensual*inversion_mensual)
        contador += 1
    else:
        break

print("Va a tardar",contador, "meses en ahorrar el deposito")
