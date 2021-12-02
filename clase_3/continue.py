for num in range(2,10):
    if num % 2 == 0:
        print("Encontrado un número par: ", num)
        continue # continúa a iterar sobre el for, no sale de él como break
    print("Encontrado un número impar: ", num)


