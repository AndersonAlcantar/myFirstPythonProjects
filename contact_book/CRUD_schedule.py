import numpy as np

import os
# file = open("agenda.txt", "w")
# file.write("vacio")
# file.close()



def buscar_celular(nombre):
    datos_entrada = np.loadtxt("agenda2.txt", delimiter="#", dtype=str)
    if nombre in datos_entrada:
        for i in range(len(datos_entrada)):
            if datos_entrada[i] == nombre:
                print(f"{datos_entrada[i]}")
                print(f"{datos_entrada[i + 1]}")
                print(f"{datos_entrada[i + 2]}")
    else:
        print("No se encuentra el beneficiario en la agenda")


def agregar(nombre_completo, celular, cedula):
    datos_entrada = np.loadtxt("agenda2.txt", delimiter="#", dtype=str)
    if "vacio" in datos_entrada:
        datos = np.array([nombre_completo, cedula, celular])
        np.savetxt("agenda2.txt", datos, delimiter=" ", fmt="%s")
    else:
        datos = np.array([nombre_completo, cedula, celular])
        nuevos_datos = np.append(datos_entrada, datos)
        np.savetxt("agenda2.txt", nuevos_datos, delimiter=" ", fmt="%s")


def eliminar(cedula):
    datos_entrada = np.loadtxt("agenda2.txt", delimiter="#", dtype=str)
    if cedula in datos_entrada:
        for i in range(len(datos_entrada)):
            if datos_entrada[i] == cedula:
                archivo_nuevo = np.delete(datos_entrada, ((i - 1), i, (i + 1)))
        np.savetxt("agenda2.txt", archivo_nuevo, delimiter=" ", fmt="%s")
        print("El usuario ha sido eliminado del listado")
    else:
        print(f"La cedula no existe")


def mostrar_agenda():
    datos_entrada = np.loadtxt("agenda2.txt", delimiter="#", dtype=str)
    for i in range(len(datos_entrada)):
        print(datos_entrada[i])
    # agenda = open("agenda.txt", "r")
    # print(agenda.read())
    # agenda.close()

def mostrar_nombre(letra):
    datos_entrada = np.loadtxt("agenda2.txt", delimiter="#", dtype=str)
    print("Listado filtrado de beneficiarios: ")
    for p in datos_entrada:
        if p[0] == letra or p[0] == letra.upper():
            indice = np.where(datos_entrada == p)[0]
            print(*datos_entrada[indice])
            print(*datos_entrada[indice + 1])
            print(*datos_entrada[indice + 2])


def op1():
    print("Digite el nombre y apellido del beneficiario a buscar: ")
    nombre = input("")
    #apellido = input("Ingrese el apellido: ")
    nombre_completo = nombre #+ " " + apellido
    buscar_celular(nombre_completo)


def op2():
    print("Digite la información del beneficiario a agregar: ")
    nombre = input("nombre: ")
    #apellido = input("Ingrese el apellido: ")
    cedula = input("cedula: ")
    celular = input("celular: ")
    nombre_completo = nombre #+ " " + apellido
    agregar(nombre_completo, celular, cedula)
    print("El beneficiario ha sido agregado")
    # datos_entrada = np.loadtxt("agenda.txt", delimiter="#", dtype=str)
    # if (cedula in datos_entrada) == False:
    #     agregar(nombre_completo, celular, cedula)
    #     print("El beneficiario ha sido agregado al listado")
    # else:
    #     print(f"El numero de cedula {cedula} ya existe")


def op3():
    print("Digite la cedula del beneficiario a borrar: ")
    cedula = input("")
    eliminar(cedula)


def op4():
    print("Listado de beneficiarios: ")
    mostrar_agenda()


def op5():
    print("Digite la letra por la que empiezan los beneficiarios:")
    letra = input("")
    mostrar_nombre(letra)


def main():

    while True:
        print("Menu Principal: \n"
              "Opcion 1: Ver listado \n"
              "Opcion 2: Ver listado filtrado \n"
              "Opcion 3: Agregar beneficiario \n"
              "Opcion 4: Buscar beneficiario \n"
              "Opcion 5: Borrar beneficiario \n"
              "Opcion 6: Salir")
        print("Opcion: ")
        op = int(input(""))
        if(op == 1):
            op4()
        elif(op == 2):
            op5()
        elif(op == 3):
            op2()
        elif(op == 4):
            op1()
        elif(op == 5):
            op3()
        elif(op == 6):
            print("Hasta pronto")
            break
        else:
            print("Opcion no valida")


main()
