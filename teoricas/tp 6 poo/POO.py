"""🧗🏻‍♀️ Desafio I: Ahora te toca a vos:

   - Creá a la golondrina maria con 42 puntos de energía inicial
   - Creá al dragón chimuelo, con 200 dientes y 1000 de energía inicial
   - Definí el método esta_debil, que nos dice si nuestras "aves" tiene menos 
de 10 puntos de energía (golondrinas) o menos de 50 puntos de energía (dragones)
   - Definí el método esta_feliz, que nos dice si nuestras "aves" tiene más de 500
puntos de energía (sin importar de qué clase sean)
   - Hace a hipo, entrenador de dragones: sabe aceptar a dragones, quienes son sus entrenados 
y hacerlos entrenar todos los dias, haciendoles dar 20 vueltas en circulos y luego comer su 
comida favorita hasta saciarse (3 peces)
   - Hacé que hipo pueda entrenar a las golondrinas. ¿Qué comportamiento deberían entender las 
golondrinas ahora?
   - Definí el método entrenamiento_intensivo, que hace dar vueltas en circulos a sus entrenados
hasta que estén débiles."""

class Animal_alado:
    
  def esta_feliz(self):
    return self.energia >= 500

class Golondrina(Animal_alado):
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0) 
  def volar(self, kms):
    self.energia -= 10 + kms
    
  def esta_debil(self):
    return self.energia <=10
    

class Dragon(Animal_alado):     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes 

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def esta_debil(self):
    return self.energia <=50

class Entrenador:
   def __init__(self, equipo):
      self.equipo = equipo

   def aceptar_dragon(self, dragon):
      self.equipo.append(dragon)

   def entrenar_dragon(self, dragon):
      for vueltas in range(20):
         dragon.volar_en_circulos()
      dragon.comer_peces(3)

   def entrenar_equipo(self):
      for dragon in self.equipo:
         self.entrenar_dragon(dragon)
      


pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
pendorcho = Golondrina(100)
hipo = Entrenador([])