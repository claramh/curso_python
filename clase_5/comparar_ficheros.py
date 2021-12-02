import filecmp

dir1 = "../clase_3"
dir2 = "../clase_3copia"

comunes = ["continue.py", "for.py"]

match, mismatch, errors = filecmp.cmpfiles(dir1, dir2, comunes) #comparar dir1 y dir2

print("Verifica los metadatos:")
print("Coinciden:", match)
print("NO coinciden:", mismatch)
print("Errores:", errors, "\n")