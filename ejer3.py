def bisiesto(año):
	return not año % 4 and (año % 100 or not año % 400)


anio = int(input("Ingrese un año: "))

if bisiesto(anio):
    print("Es bisiesto")
else:
    print("No es bisiesto")
    