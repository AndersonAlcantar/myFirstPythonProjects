i = 0
acumulador_total_dias = 0
acumulador_error_dias = 0
acumulador_temp_min = 0
acumulador_temp_max = 0
acumulador_error_ambos_dias = 0
media_temp_minima = 0
media_temp_max = 0
acumulador_ambos_dias = 0
while True:
    i = i + 1
    print(f"Dia {i}")
    temperatura_min = int(input("Ingrese la temperatura minima: "))
    temperatura_max = int(input("Ingrese la temperatura maxima: "))
    acumulador_total_dias = acumulador_total_dias + 1
    if(temperatura_min>temperatura_max):
        print("Fuera de rango")
        break
    if (temperatura_min == 0 and temperatura_max == 0):
        break

    if(temperatura_min < 5 or temperatura_max > 35):
        acumulador_error_dias = acumulador_error_dias + 1

    if(temperatura_min < 5):
        acumulador_temp_min = acumulador_temp_min + 1

    if(temperatura_max > 35):
        acumulador_temp_max = acumulador_temp_max + 1

    if(temperatura_min < 5 and temperatura_max > 35):
        acumulador_error_ambos_dias = acumulador_error_ambos_dias + 1

    if (temperatura_min > 4 and temperatura_max < 36):
        acumulador_ambos_dias = acumulador_ambos_dias + 1
        media_temp_minima = media_temp_minima + temperatura_min
        media_temp_max = media_temp_max + temperatura_max


print("/////////////////////////////////////////////////////")
print(f"Numero total de dias registrados: {acumulador_total_dias-1} \n" +
      f"Numero total de dias registrados con error: {acumulador_error_dias} \n" +
      f"Numero total de dias con temperaturas menores a 5: {acumulador_temp_min} \n" +
      f"Numero total de dias con temperaturas mayores a 35: {acumulador_temp_max} \n" +
      f"Numero total de dias con ambos errores: {acumulador_error_ambos_dias} \n" +
      f"Temperatura media minima: {media_temp_minima / acumulador_ambos_dias} \n" +
      f"Temperatura media maxima: {media_temp_max / acumulador_ambos_dias} \n" +
      f"Porcentaje de dias que se reportaron errores: {int((acumulador_error_dias/(acumulador_total_dias-1))*100)}%")