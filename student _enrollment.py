
numero_candidatos = int(input("Ingrese el numero de candidatos: "))
nombre_candidato = [None] * numero_candidatos
apellidos_candidato = [None] * numero_candidatos
edad_candidato = [None] * numero_candidatos
salario_candidato = [None] * numero_candidatos
puntaje_candidato = [None] * numero_candidatos
descuento = [None] * numero_candidatos

matricula = int(input("Ingrese el valor de la matricula: "))
for i in range(numero_candidatos):
    nombre = input(f"Nombre del candidato {i+1}: ")
    nombre_candidato[i] = nombre
    apellidos = input(f"Apellido del candidato {i+1}: ")
    apellidos_candidato[i] = apellidos
    edad = int(input(f"Edad del candidato {i+1}: "))
    edad_candidato[i] = edad
    salario = float(input("Salario familiar: "))
    salario_candidato[i] = salario / 908526
    puntaje = int(input("Puntaje de ingreso: "))
    puntaje_candidato[i] = puntaje


descuento_edad = [None] * numero_candidatos
for i in range(numero_candidatos):
    if edad_candidato[i] >= 15 and edad_candidato[i] <= 18:
        descuento[i] = 0.25
        descuento_edad[i] = 0.25
    elif edad_candidato[i] >= 19 and edad_candidato[i] <= 21:
        descuento[i] = 0.15
        descuento_edad[i] = 0.15
    elif edad_candidato[i] >= 22 and edad_candidato[i] <= 25:
        descuento[i] = 0.10
        descuento_edad[i] = 0.10
    elif edad_candidato[i] > 25:
        descuento[i] = 0.0
        descuento_edad[i] = 0.0
    else:
        print("El estudiante es menor a la edad permitida")

descuento_familiar = [None] * numero_candidatos

for i in range(numero_candidatos):
    if salario_candidato[i] <= 1.0:
        descuento[i] = descuento[i] + 0.30
        descuento_familiar[i] = 0.30
    elif salario_candidato[i] > 1.0 and salario_candidato[i] <= 2.0:
        descuento[i] = descuento[i] + 0.20
        descuento_familiar[i] = 0.20
    elif salario_candidato[i] >= 2.0 and salario_candidato[i] <= 3.0:
        descuento[i] = descuento[i] + 0.10
        descuento_familiar[i] = 0.10
    elif salario_candidato[i] >= 3.0 and salario_candidato[i] <= 4.0:
        descuento[i] = descuento[i] + 0.5
        descuento_familiar[i] = 0.5
    else:
        descuento[i] = descuento[i] + 0.0
        descuento_familiar[i] = 0.0


descuento_examen = [None] * numero_candidatos

for i in range(numero_candidatos):
    if puntaje_candidato[i] >= 80 and puntaje_candidato[i] < 86:
        descuento[i] = descuento[i] + 0.30
        descuento_examen[i] = 0.30
    elif puntaje_candidato[i] >= 86 and puntaje_candidato[i] < 91:
        descuento[i] = descuento[i] + 0.35
        descuento_examen[i] = 0.35
    elif puntaje_candidato[i] >= 91 and puntaje_candidato[i] < 96:
        descuento[i] = descuento[i] + 0.40
        descuento_examen[i] = 0.40
    elif puntaje_candidato[i] >= 96:
        descuento[i] = descuento[i] + 0.45
        descuento_examen[i] = 0.45
    else:
        descuento[i] = descuento[i] + 0.0
        descuento_examen[i] = 0.0

print("///////////////////////////////////////////////////////////////")
for i in range(numero_candidatos):
    print(f"Candidato {i+1} \n" +
        f"Nombre: {nombre_candidato[i]} \n" +
          f"Apellido: {apellidos_candidato[i]} \n" +
          f"Descuento recibido por edad: {round(descuento_edad[i] * 100)}% \n" +
          f"Descuento recibido por ingreso familiar: {round(descuento_familiar[i] * 100)}% \n" +
          f"Descuento recibido por puntaje del examen: {round(descuento_examen[i] * 100)}% \n" +
          f"El descuento total sobre la matricula es de: {round(descuento[i] * 100)}% \n" +
          f"Valor de matricula: {round(matricula - (matricula * descuento[i]))} \n"  
          "///////////////////////////////////////////////////////////////")



