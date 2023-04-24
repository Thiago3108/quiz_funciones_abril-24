# Construir una función que reciba un valor entero como parámetro y que determine si su último dígito es 4.

print("-----------------------------------")
print("------VERIFICADODR DE CUATRO-------")
print("-----------------------------------")

def verificador_de_cuatro_digito(x):

    if x % 10 == 4:
        print("su ultimo digito es cuatro")
    else:
        print("Es un entero normal")
    
x = int(input("ingrese el numero entero: "))

verificador_de_cuatro_digito(x)