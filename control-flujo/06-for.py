# for numero in range(5):
#     print(numero)

buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado ,", buscar)
        break
else:
    print("no encontre el resultado")


for char in "Ultimate Python":
    print(char)
