n = int(input("Ingrese el numero de estudiantes: "))
nombre = [None] * n
corte_1 = [None] * n
corte_2 = [None] * n
corte_3 = [None] * n
definitiva = [None] * n
condicion = [None] * n

def calcular_cortes():
    for i in range(n):
        estudiante = input("Nombre: ")
        nombre[i] = estudiante
        j=0
        y = 0
        z = 0
        suma = 0.0
        suma_2 = 0.0
        while j < 2:
            nota = float(input(f"Nota {j + 1}: "))
            suma = suma + (nota * 0.1)
            j = j + 1
        nota = float(input(f"Nota {j + 1}: "))
        suma = suma + (nota * 0.2)
        corte_1[i] = suma/0.40

        while y < 2:
            nota = float(input(f"Nota {y + 4}: "))
            suma_2 = suma_2 + (nota * 0.2)
            y = y + 1
        corte_2[i] = suma_2/0.4

        nota = float(input(f"Nota 6: "))
        corte_3[i] = nota


def calcular_definitiva():
    for i in range(n):
        definitiva[i] = (corte_1[i] * 0.4) + (corte_2[i] * 0.4) + (corte_3[i] * 0.2)


def validar():
    for i in range(n):
        if definitiva[i] > 3.9 and definitiva[i] < 5.1:
            condicion[i] = "Excelente"
        elif definitiva[i] > 2.9 and definitiva[i] < 4.0:
            condicion[i] = "Bueno"
        else:
            condicion[i] = "Repite"

def mostrar():
    print("////////////////////////////////")
    for i in range(n):
        print(f"Estudiante: {nombre[i]} \n" +
              f"Corte 1: {corte_1[i]} \n" +
              f"Corte 2: {corte_2[i]} \n" +
              f"Corte 3: {corte_3[i]} \n" +
              f"Definitiva: {definitiva[i]} \n" +
              f"Condicion: {condicion[i]} \n"
              f"////////////////////////////////")

def main():
    calcular_cortes()
    calcular_definitiva()
    validar()
    mostrar()

main()