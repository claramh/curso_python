# Verifica si un número es primo
for n in range(2,10):
    for x in range(2,n): # n es cada número de 2 al 9
        if n % x == 0: # n divido por 1,2,3,4,5... x es una cadena de números ascendentes --> % indica número entero
                        # si llega a dividir
            print(n, "equivale a", x, "*", n//x)
            break
    else: # else aquí pertenece al ciclo for, no al if: el else se ejecuta cuando no hay ningún break
        # El bucle sigue sin encontrar un factor
        print(n, "es un número primo")