class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2


#identificá la interfaz y el estado de la misma:
"""
Al conjunto de mensajes que cada objeto expone lo llamaremos interfaz
El estado es el conjunto de atributos de un objeto.
"""

#Modificá el método volar de la clase Golondrina visto en la clase de 
#teoría de manera que no pueda volar si al hacerlo la energía toma el 
# valor 0 o valor negativo.

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def volar(self, kms):
    if 10 + kms < self.energia:
        self.energia -= 10 + kms
    else:
        print("si vuela esa cantidad de kms morirá")

pepita = Golondrina(30)

pepita.volar(30)


class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def descuento(self, porcentaje):
        self.precio = self.precio - (self.precio * (porcentaje/100))

    def precioactual(self):
        return self.precio
    
notebook1 = Notebook("Asus", "R538l", 8000)
notebook1.descuento(50)
print(notebook1.precioactual())

#4
class Contador:
    def __init__ (self, valor):
        self.valor = valor
        self.ultimo = None

    def inc(self):
        self.valor += 1
        self.ultimo ="incrementar"

    def dis(self):
        self.valor -= 1
        self.ultimo = "disminuir"

    def reset(self):
        self.valor = 0
        self.ultimo = "resetear"

    def valoractual(self):
        print(self.valor)
    

    def valornuevo(self, nuevovalor):
        self.valor = nuevovalor
        self.ultimo = "valornuevo"

    def ultimoComando(self):
        return self.ultimo

class Calculadora:
    def _init_(self):
        self.valor = None
    
    def cargar(self, num):
        self.valor = num
    
    def sumar(self, num):
        self.valor += num
    
    def restar(self, num):
        self.valor -= num
    
    def multiplicar(self, num):
        self.valor *= num

    def valorActual(self):
        print(self.valor)

calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
calculadora.valorActual()
