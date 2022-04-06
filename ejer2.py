

#Escribe una función que pueda decirte si un número (número entero) es primo o no

num=int(input("Ingrese un numero: "))
def primo(num1):
    pr=0
    for i in range (1,num1+1):
        if num1%i==0: 
            pr+=1
    if pr==2:
        return "Es primo"
    else:
        return "No es primo"

print("El numero ",num,primo(num))










