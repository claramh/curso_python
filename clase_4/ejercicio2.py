# Preguntar al usuario un número y mostrar si es par o impar. Si el número es múltiplo de 4 imprimir el mensaje apropiado al usuario

def dame_numero():
    num = input("Dame un número: ")
    num = int(num)
    if num % 2 == 0:
        print(num, "es un número PAR")
        if num%4 == 0:
            print(f"El número {num} es PAR y además múltiplo de 4")
    else:
        print(num, "es un número IMPAR")

dame_numero()

