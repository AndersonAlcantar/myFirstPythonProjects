import numpy as np

datos_entrada = np.loadtxt("agenda.txt", delimiter="#", dtype=str)


def buscar_celular(nombre):
    if nombre in datos_entrada:
        for i in range(len(datos_entrada)):
            if datos_entrada[i] == nombre:
                print(f"Numero de celular: {datos_entrada[i + 2]}")
    else:
        print("El nombre no se encuentra registrado")


def agregar(nombre_completo, celular, cedula):
    datos = np.array([nombre_completo, cedula, celular])
    nuevos_datos = np.append(datos_entrada, datos)
    np.savetxt("agenda.txt", nuevos_datos, delimiter=" ", fmt="%s")


def eliminar(cedula):
    if cedula in datos_entrada:
        for i in range(len(datos_entrada)):
            if datos_entrada[i] == cedula:
                archivo_nuevo = np.delete(datos_entrada, ((i - 1), i, (i + 1)))
        np.savetxt("agenda.txt", archivo_nuevo, delimiter=" ", fmt="%s")
        print("Eliminado con exito")
    else:
        print(f"La cedula {cedula} no existe")


def mostrar_agenda():
    agenda = open("agenda.txt", "r")
    print(agenda.read())


def mostrar_nombre(letra):
    for p in datos_entrada:
        if p[0] == letra or p[0] == letra.upper():
            indice = np.where(datos_entrada == p)[0]
            print(*datos_entrada[indice])
            print(*datos_entrada[indice + 1])
            print(*datos_entrada[indice + 2])


def op1():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    nombre_completo = nombre + " " + apellido
    buscar_celular(nombre_completo)


def op2():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    cedula = input("Ingrese el numero de cedula: ")
    celular = input("Ingrese el numero de celular: ")
    nombre_completo = nombre + " " + apellido
    if (cedula in datos_entrada) == False:
        agregar(nombre_completo, celular, cedula)
        print("Registro exitoso")
    else:
        print(f"El numero de cedula {cedula} ya existe")


def op3():
    cedula = input("Ingrese el numero de cedula a eliminar: ")
    eliminar(cedula)


def op4():
    mostrar_agenda()


def op5():
    letra = input("Ingrese una letra: ")
    mostrar_nombre(letra)


def main():
    print("Funciones: \n"
          "Opcion 1: Encuentra en el archivo agenda.txt el número de celular de un beneficiario, dados su nombre y apellido. \n"
          "Opcion 2: Añade un nuevo beneficiario en la agenda.txt, al final del archivo. \n"
          "Opcion 3: Borra un beneficiario de la agenda.txt dado su número de cédula. \n"
          "Opcion 4: Muestra en consola el listado completo de los beneficiarios del archivo agenda.txt. \n"
          "Opcion 5: Muestra en consola el listado de los beneficiarios cuyo nombre empieza por una letra determinada.")
    op = int(input("Ingrese la opcion a ejecutar: "))

    if(op == 1):
        op1()
    elif(op == 2):
        op2()
    elif(op == 3):
        op3()
    elif(op == 4):
        op4()
    elif(op == 5):
        op5()
    else:
        print("Opcion no valida")


main()
