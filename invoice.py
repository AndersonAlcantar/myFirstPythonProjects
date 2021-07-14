
numero_productos = int(input("Ingrese el numero de productos a registrar: "))
codigo_producto = [None] * numero_productos
numero_unidades = [None] * numero_productos
precio_unitario = [None] * numero_productos
descripcion_producto = [None] * numero_productos
iva_producto = [None] * numero_productos

for i in range(numero_productos):
    codigo = input(f'Ingrese el codigo del producto {i+1}: ')
    codigo_producto[i] = codigo
    descripcion = input("Descripcion del producto: ")
    descripcion_producto[i] = descripcion
    unidades = float(input('Ingrese el numero de unidades: '))
    numero_unidades[i] = unidades
    precio = float(input('Ingrese el precio unitario: '))
    precio_unitario[i] = precio
    iva = float(input('Ingrese el iva del producto: '))
    iva_producto[i] = iva

descuento = int(input('Ingrese el descuento: '))
valor_envio = int(input('Ingrese el valor del envio: '))

def importe():
    importe = [None] * numero_productos
    for i in range(numero_productos):
        importe[i] = precio_unitario[i] * numero_unidades[i]
    return importe

def iva_importe():
    iva_importe = [None] * numero_productos
    for i in range(numero_productos):
        iva_importe[i] = (importe()[i] * (1 + (iva_producto[i] / 100))) - (importe()[i])
    return iva_importe


def sub_total():
    sub_total = 0
    for i in range(numero_productos):
        sub_total = sub_total + importe()[i]
    return sub_total

def valor_descuento():
    valor_descuento = sub_total() - (sub_total()*(descuento/100))
    return valor_descuento

def total_iva():
    total_iva = 0
    for i in range(numero_productos):
        total_iva = total_iva + iva_importe()[i]
    return total_iva

def valor_iva():
    valor_iva = total_iva() + valor_descuento()
    return valor_iva

def valor_total():
    valor_total = valor_iva() + valor_envio
    return valor_total

def mostrar_descripcion():
    print("/////////////////////////////////////////////////")
    for i in range(numero_productos):
        print(f"Código {codigo_producto[i] }" + '\n' +
              f"Descripcion: {descripcion_producto[i]} \n" +
              f"Cantidad: {numero_unidades[i]}" + '\n' +
              f"Importe: {importe()[i]}" + '\n' +
              f"Iva({iva_producto[i]}%): {iva_importe()[i]}" + '\n' +
              "/////////////////////////////////////////////////")
    print(f"Sub Total: {sub_total()} \n" +
          f"Descuento({descuento}%): {sub_total()*(descuento/100)} \n" +
          f"Valor descuento: {valor_descuento()} \n" +
          f"Total Iva: {total_iva()} \n" +
          f"Valor Iva: {valor_iva()} \n" +
          f"Valor envio: {valor_envio} \n" +
          f"Valor total: {valor_total()}")
mostrar_descripcion()


