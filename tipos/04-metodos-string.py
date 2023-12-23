animal = "    chaNchiTo feliz    "

# imprime todo en mayuscula
print(animal.upper())

# imprime todo en minuscula
print(animal.lower())

# imprime la primera letra en mayuscula.
# Si hay un espacio al princincio trata de poner en mayuscula el espacio
print(animal.capitalize())
# con esto se arregla
print(animal.strip().capitalize())

# imprime cada en mayuscula la primera letra de cada palabra
print(animal.title())

# QUITA TODOS LOS ESPACIOS en blanco
print(animal.strip())

# para sacar los espacios de la izquierda del string
print(animal.lstrip())

# para sacar los espacios de la derecha del string
print(animal.rstrip())

# para buscar algun caracter y si devuelve -1 significa que no lo encontro,
# devuelve un numero si esta todo correcto, te devuelve el indice
print(animal.upper().find("CH"))

# remplazar el carater por el que quieras
print(animal.replace("iTo", "O"))

# es lo mismo que el find pero con la condicion de que te devuelve un boolean
print("cha" in animal)
print("cha" not in animal)
