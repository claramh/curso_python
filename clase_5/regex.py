import re


## Encontrar incidencias
texto = "Hoy es un día magnífico y    maravilloso"
exp_reg = re.search("^Hoy.*oso", texto) # regex entre comillas y variable donde buscar esa regex
print(exp_reg)

exp_reg2 = re.findall("ma", texto) # search sólo encuentra una coincidencia, findall te da todas las coincidencias
print(exp_reg2)

exp_reg3 = re.sub ("\s", "    ", texto) # substituye el primer argumento por el segundo
print(exp_reg3)