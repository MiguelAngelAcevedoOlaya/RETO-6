# -*- coding: utf-8 -*-
"""reto#6.4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yCHF7hTjWIiE7HSrxQHddzqCHME_7Lcn
"""

p_pan: int =300
p_lec: int=3300
p_hue: int=350

#Se definieron de los precios del pan, leche y huevos, como constantes

import math as m #importar libreria math

def vueta_mama(panes:float, leche:float, huevos:float, dinero:float) -> float:
  vueltas_ = (dinero- (panes*p_pan + leche*p_lec + huevos*p_hue))
  return vueltas_  #se definio la variable que devuelva la cantidad de dinero que sobro


if __name__ == "__main__":
  panes = float(input("Cantidad de pan:"))
  leche = float(input("Bolsas de leche:"))
  huevos = float(input("Cantidad de huevos:"))
  dinero = float(input("Cuanto dinero te dio tu mami, por favor ingresa billetes considernado moneda colombiana, ejemplo 1000, 2000, sino deberas hasta la madre perro:"))
  total_vueltas = vueta_mama(panes, leche, huevos, dinero)
  if total_vueltas > 0:
    print("La cantidad de dinero que sobro fue " +str(total_vueltas)+ " pesos, puede comprar dulcesitos en secreto")
  elif total_vueltas ==0:
    print("No te quedo dinero pa")
  elif total_vueltas < 0:
    total_vueltas = total_vueltas*(-1)
    print("Papi debes" +str(total_vueltas))  #codigo if que solucione la función, y estableciendo otras condiciones que digan lo que sobro, si no sobro o si quedo debiendo plata