# Parametros opcionales
def hola(nombre, apellido="Feliz"):
    print("hola Mundo")
    # Se llama PARAMETRO
    print(f"Bienvenido {nombre} {apellido}")


nombres = input("escribir tu nombre ")
apellidos = input("escribir tu apellido ")
# El valor se llama ARGUMENTO
hola(nombres, apellidos)
hola("Chanchito")


# Argunmetos Nombrados
hola(apellido="cardozo", nombre="dulce")
