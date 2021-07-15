terra = int(input("Ingrese la distancia de Terra: "))
loona = (2*terra)+4
zaibertron = int((loona + terra)/5)


def categoria_planeta(planeta, nombre_planeta):
    if planeta >= 0 and planeta < 21:
        return f"El planeta {nombre_planeta} es de categoria uno"
    elif planeta > 20 and planeta < 31:
        return f"El planeta {nombre_planeta} es de categoria dos"
    elif planeta > 30 and planeta < 51:
        return f"El planeta {nombre_planeta} es de categoria tres"
    else:
        return f"El planeta {nombre_planeta} es de categoria cuatro"


def mostrar(terra,loona, zaibertron, planeta, nombre_planeta):
    print(f"Terra: {terra} \n" +
          f"Loona: {loona} \n" +
          f"Zaibertron: {zaibertron} \n" +
          categoria_planeta(planeta, nombre_planeta))


mostrar(terra, loona, zaibertron, zaibertron, "zaibertron")
