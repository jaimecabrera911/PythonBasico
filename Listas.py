numeros = [1, 2, 3, 4]
listaColores = ["Amarillo", "Azul", "Rojo", "Verde", "Blanco", "Negro"]

print("Imprimir lista completa")
print(listaColores)

print("\nImprimir el primer elemento")
print(listaColores[0])  # Imprimir el primer elemento

print("\nImprimir el ultimo elemento")
print(listaColores[-1])  # Imprimir el ultimo elemento

print("\nImprimir a partir del tercer elemento")
print(listaColores[2:])  # Imprimir a partir del tercer elemento

print("\nImprimir penultimo elemento hasta el final")
print(listaColores[-2:])  # Imprimir penultimo elemento hasta el final

print("\nImprimir desde el segundo elemento hasta el cuarto elemento de la lista")
print(listaColores[1:4])  # Imprimir desde el segundo elemento hasta el cuarto elemento de la lista

print("\nAgregar elementos en una lista")
agregarNumeros = numeros + [5, 6, 7, 8, 9, 10]
print(agregarNumeros)

pares = [1, 3, 4, 7, 8]
print("\nReemplazar el primer elemento de la lista")
pares[0] = 2
print(pares)

print("\nAgregar elemento al final")

pares.append(10)
print(pares)

pares.append(7 * 2)
print(pares)

print("\nReemplazar los 3 primeros elementos")
pares[:2] = [2, 4, 6]
print(pares)

print("\nEliminar los 3 primeros elementos")
pares[:3] = []
print(pares)

print("\nEliminar toda la lista")
pares = []
print(pares)

print("\nContar elementos")
print(len(listaColores))

print("\nUnir Listas en una lista")
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
lista = a, b, c
print(lista)

print("\nAcceder a la segunda lista")
print(lista[1])

print("\nAcceder al segundo elemento de la ultima lista")
print(lista[-1][1])

print("\nCombinar todos los elementos de una lista en una lista")
lista = a + b + c
print(lista)
