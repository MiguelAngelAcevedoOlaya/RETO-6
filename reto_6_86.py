from reto_6_7 import may_elev_men

numero_1 = float(input("Ingresa el número 1:"))
numero_2 = float(input("Ingresa el número 2:"))
numero_3 = float(input("Ingresa el número 3:"))
numero_4 = float(input("Ingresa el número 4:"))
numero_5 = float(input("Ingresa el número 5:")) 

mayor_numero_elevado_al_menor = may_elev_men(numero_1, numero_2, numero_3, numero_4, numero_5)
print("El mayor número elevado al menor es " +str(mayor_numero_elevado_al_menor))
