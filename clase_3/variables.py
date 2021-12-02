# ejemplo de variable local

def subrutina():
    variable = 10
    print(variable)
    return

variable = 20
print("esta es la variable local:")
subrutina()
print("esta es la variable fuera de la función:", variable)


# ejemplo de variable global
def subrutina():
    global var_global
    print(var_global)
    var_global = 10
    return

var_global = 5
subrutina()
print(var_global)