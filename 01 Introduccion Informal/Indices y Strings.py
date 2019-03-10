palabra = "Python"

print(palabra[0])  # imprimir el primer caracter

print(palabra[3])  # imprimir el cuarto caracter

print(palabra[2:])  # imprimir a partir de la tercera posicion de la cadena

print(palabra[:3])  # imprimir desde el primer caracter hasta el tercero se excluye el cuarto

print(palabra[2:4])  # imprimir a partir del 3 caracter hasta el 4

print(palabra[-1])  # imrpimir el ultimo caracte de la cadena

print(palabra[-3:])  # imprimir a partir 3 caracteres empezando desdel el final

print(palabra[:2] + " " + palabra[-2:])  # Imprimir los dos primeros caractetes con los dos ultimos

reemplazarTexto = "N" + palabra[1:]  # Reemplazar un caracter dentro de una cadena de texto

print(reemplazarTexto)

print(len(palabra))  # contar el numero de caracteres de una cadena de texto
