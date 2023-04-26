# verificar la sig curiosidad matematica: el cuadrado de un numero entero positivo n es igual a la suma de los primeros n numeros impares... Ejm 7**2 = 49 or 7*2=14 and 1+3+5+7+9+11+13 = 49
print("------------------------------------------")
print("----------CURIOSIDAD MATEMATICA-----------")
print("------------------------------------------")
def cuadrados(n):
    x = 0
    rta = "|"
    for i in range(1, n*2):
        
        if i % 2 != 0:
            x += i
            rta = rta + str(i) + "+"        
    rta = rta.rstrip("+") + "|"
    print(f"El valor: {n}² = {rta}")  
    print(f"==>{rta} = {x}")
    print(f"==>{n}² = {n**2}") 

n = int(input("Ingrese un numero: "))
cuadrados(n)
