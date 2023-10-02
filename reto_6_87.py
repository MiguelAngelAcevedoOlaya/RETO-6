from reto_6_7 import raiz_m

numero_1 = float(input("Ingresa el número 1:"))
numero_2 = float(input("Ingresa el número 2:"))
numero_3 = float(input("Ingresa el número 3:"))
numero_4 = float(input("Ingresa el número 4:"))
numero_5 = float(input("Ingresa el número 5:"))

raiz_menor_número = raiz_m(numero_1, numero_2, numero_3, numero_4, numero_5)
print("La raúz cubica del menor número es " +str(raiz_menor_número))
