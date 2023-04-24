print("-------------------------------")
print("-----TABLA DE MULTIPLICAR------")
print("-------------------------------")
def generador_de_tabla(valores, x):
    print(f"TABLA DEL {x}")
    for i in valores:
        print(f"{i} x {x} = {i*x}")
x= int(input("ingrese el valor de la tabla de multiplicar: "))
valores = range(1, 11)
generador_de_tabla(valores, x)