n1 = input("Ingrese un numero=  ")
n2 = input("Ingrese un numero=  ")

n1 = int(n1)
n2 = int(n2)


suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 // n2

mensaje = f"""El resultado de los valores {n1} y {n2} es suma = {suma}, resta = {resta}
    division = {div} y multiplicacion = {multi}
    """

print(mensaje)
