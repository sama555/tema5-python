
print("-------------Triangulo----------------")
altura = float(input("Ingrese la altura del triangulo: "))
base = float (input("Ingrese la base del trinangulo: "))
def areaT(a,b):
    return altura*base/2

print("El area del trinagulo es: ",areaT(altura,base))

print ("------------------Circulo----------------")
radio=float(input("Ingrese el area de un circulo: "))
def areaC(radio):
    return 3.14*radio**2

print("El area de un circulo: ", areaC(radio))