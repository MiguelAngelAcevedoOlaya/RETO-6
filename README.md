# RETO-6
### Miguel Angel Acevedo

#### PUNTO 1
Dado la figura de la imagen, desarrolle:

<img src="figura1.png" width="350">


Fuente: https://www.iteramos.com/pregunta/89805/cambiar-el-tamano-de-la-imagen-en-markdown-en-gitlab
Fuente: https://www.iteramos.com/pregunta/89805/cambiar-el-tamano-de-la-imagen-en-markdown-en-gitlab

Fuente: https://www.iteramos.com/pregunta/89805/cambiar-el-tamano-de-la-imagen-en-markdown-en-gitlab
Una función matemática para calcular el volumen y el área superficial.
Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
Revise como utilizar el valor de pi usando import math y math.pi

Para este punto importamos la libreria math, y además importamos math.pi, que nos da el valor exacto del número, permitiendonos obtener valores exactos tanto del area como de la superficie

ESFERA AREA SUPERFICIAL Y VOLUMEN

<img src="esfera.png" width="250">

CONO AREA SUPERFICIAL Y VOLUMEN

<img src="cono.png" width="250">

En base a eso desarrollamos el siguiente codigo:

```
import math as m #importar libreria math
p= m.pi #importar el valor exacto de pi
def Volumen_figura(radio1:float, altura_cono:float, radio2:float) -> float:
  vol = ((4*p*(radio1**3))/3) + ((altura_cono*p*(radio2**2))/3)
  return vol  #se definio la variable del volumen

def Area_superficial_figura(radio1:float, altura_cono:float, radio2:float) -> float:
  area_sup = (4*p*(radio1**2)) + (p*radio2*(radio2+((radio2**2)+(altura_cono**2)**0.5)))
  return area_sup #se definio la variable del area superficial

if __name__ == "__main__":
  radio1 = float(input("El radio de la esfera:"))
  altura_cono = float(input("La altura del cono:"))
  radio2 = float(input("El radio del cono:"))
  volumen = Volumen_figura(radio1, altura_cono, radio2)
  area_superficial = Area_superficial_figura(radio1, altura_cono, radio2)
  print("El volumen de la figura es " + str(volumen)+ " y el area superficial es " +str(area_superficial)) #se puso condicional if que defina las variables con teclado y me imprima los valores de volumeny area superficial

```

#### PUNTO 2

Dado la figura de la imagen, desarrolle:

<img src="figura2.png" width="350">

Una función matemática para calcular el área y el perimetro.
Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
Revise como utilizar el valor de pi usando import math y math.pi

Consideramos el area de una figura como la base por su altura, y el perimetros 2*base + 2*altura y la siguiente imagen para referenciar el area y permietro del circulo:

<img src="perimetro.png" width="350">

```
import math as m #importar libreria math
p= m.pi #importar el valor exacto de pi
def area_2_figura(base:float, altura:float, radio:float) -> float:
  area_2 = (base*altura) + 2*(p*(radio)**2)
  return area_2  #se definio la variable del Area

def perimetro_2_figura(base:float, altura:float, radio:float) -> float:
  per_2 = ((2*base)+(2*altura)) + (2*p*radio)
  return per_2 #se definio la variable del perimetro

if __name__ == "__main__":
  radio = float(input("El radio del circulo:"))
  base = float(input("La base de la figura:"))
  altura = float(input("La altura de la figura:"))
  area_ = area_2_figura(base, altura, radio)
  perimetro_ = perimetro_2_figura(base, altura, radio)
  print("El area de la figura es " + str(area_)+ " y  area superficial es " +str(perimetro_)) #se puso condicional if que defina las variables con teclado y me imprima los valores de area y permietro
```

#### PUNTO 3

Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```
masa_gina: int =6
masa_galo: int=7
masa_poll: int=1

#Se definieron las masas de las gallinas, gallos, pollitos, como constantes

import math as m #importar libreria math

def carne_(gallina:float, gallo:float, pollitos:float) -> float:
  c_carne = (gallina*masa_gina + gallo*masa_galo + pollitos*masa_poll)
  return c_carne  #se definio la variable de cantidad de carne


if __name__ == "__main__":
  gallina = float(input("Cantidad de gallinas:"))
  gallo = float(input("Cantidad de gallos:"))
  pollitos = float(input("Cantidad de pollitos:"))
  carne_total = carne_(gallina, gallo, pollitos)
  print("La cantidad de carne es " + str(carne_total)+ " kilos") #se puso condicional if que defina las variables con teclado y me imprima la cantidad total de carne
```
