# Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3
# y a su vez es menor que 10 (es suficiene con mostrar True o False).

texto = input("Ingresa una cadena de texto")

largo=len(texto)

condicion=largo>=3 and largo<=10

print("¿La longitud de la cadena es mayor o igual que 3 y menor que 10?",condicion)



