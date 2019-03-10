# Encontramos 3 operadores especiales para realizar operaciones lógicas. Normalmente se utilizan para agrupar, excluir y negar expresiones.
# Puede ayudar echar un vistazo a esta explicación sobre las tablas de la verdad:
# Not
# And
# Or
# Operadores lógicos
#
print("Not (Negación lógica)")
print(not True)
print(not False)
print(not False == True)

print("\nAnd (Conjunción lógica)")
print(True and True)
print(True and False)
print(False and False)
a = 45
print(a > 10 and a < 20)

c = "Hola Mundo"
print(len(c) <= 20 and c[0] == "H")

print("\nOr (Disyunción lógica)")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("Ejemplo:")
c = "OTRA COSA"
print(c == "EXIT" or c == "OTRA COSA" or c == "SALIR")
print(c == "EXIT" or c == "OTRA" or c == "SALIR")
