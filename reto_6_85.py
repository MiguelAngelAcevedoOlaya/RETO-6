from reto_6_7 import ordes_

numero_1 = float(input("Ingresa el número 1:"))
numero_2 = float(input("Ingresa el número 2:"))
numero_3 = float(input("Ingresa el número 3:"))
numero_4 = float(input("Ingresa el número 4:"))
numero_5 = float(input("Ingresa el número 5:"))

orden_descendente = ordes_(numero_1, numero_2, numero_3, numero_4, numero_5)
print("El orden descendente de los números es " +str(orden_descendente))
