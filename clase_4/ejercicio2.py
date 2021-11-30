# Preguntar al usuario un número y mostrar si es par o impar. Si el número es múltiplo de 4 imprimir el mensaje apropiado al usuario

num = input("Dame un número: ")
num = int(num)

if num % 2 == 0:
    print(num, "es un número PAR")
else:
    print(num, "es un número IMPAR")
