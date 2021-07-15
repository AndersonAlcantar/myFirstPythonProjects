ndocentes = int(input("Ingrese el numero de docentes: "))


def sbruto(horas, valor_hora):
    if horas <= 40:
        return horas * valor_hora
    else:
        return int((40 * valor_hora) + ((horas - 40) * 1.5 * valor_hora))


def sneto(sbruto, parafiscales, salud, pension):
    return int(sbruto - (parafiscales + salud + pension))


def descuentos(sbruto):
    parafiscales = sbruto * 0.09
    salud = sbruto * 0.04
    pension = sbruto * 0.04
    sueldo_neto = sneto(sbruto, parafiscales, salud, pension)
    print(f"Parafiscales: {parafiscales} \n" +
          f"salud: {salud} \n" +
          f"pension: {pension} \n" +
          f"Sueldo Neto: {sueldo_neto} ")

def provisiones(sbruto):
    prima = sbruto * 0.0833
    cesantias = sbruto * 0.0833
    intereses = sbruto * 0.01
    vacaciones = sbruto * 0.0417
    print(f"Prima: {prima} \n" +
          f"Cesantias: {cesantias} \n" +
          f"Intereses: {intereses} \n" +
          f"Vacaciones: {vacaciones} \n")





for i in range(ndocentes):
    nombre = input(f"Ingrese el nombre del docente {i + 1}: ")
    horas = int(input("horas trabajadas: "))
    valor_hora = int(input("valor por hora: "))
    sbruto = sbruto(horas, valor_hora)
    print("Nombre del docente: ", nombre)
    print(f"Sueldo Bruto: {sbruto}")
    print("\nDescuentos: \n")
    descuentos(sbruto)
    print("\nProvisiones: \n")
    provisiones(sbruto)