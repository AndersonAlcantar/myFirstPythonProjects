a = int(input("Ingrese el numero A: "))
b = int(input("Ingrese el numero B: "))
c = int(input("Ingrese el numero C: "))

if a > b:
    if a > c:
        if b > c:
            print("A es el mayor, B es el del medio y C el menor")
        elif b < c:
            print("A es el mahor, C el del medio y B el menor")
        else:
            print("A es el mayor, B y C menores e iguales")
    elif a < c:
        print("C es el mayor, A es el del medio y B el menor")
    else:
        print("A y C son mayores e iguales y B el menor")
elif a < b:
    if b > c:
        if a > c:
            print("B es el mayor, A el del medio y C el menor")
        elif a < c:
            print("B es el mayor, C el del medio y A el menor")
        else:
            print("B es el mayor, A y C menores e iguales")
    elif b < c:
        print("C es el mayor, B el del medio y A el menor")
    else:
        print("B y C son mayores e iguales y A el menor")
elif c < a:
    print("C es el mayor, B y A son menores e iguales")
elif c < a:
    print("A y B son mayores e iguales y C el menor")
else:
    print("A, B y C son iguales")


