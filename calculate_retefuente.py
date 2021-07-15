tot_deven = int(input("Ingrese el Total Devengado: "))
salud = tot_deven * 0.04
pension = salud
if tot_deven > (4*908526):
    fondo_sol = 0.01 * tot_deven
else:
    fondo_sol = 0

base_grava = (tot_deven - (salud + pension + fondo_sol))
base_excenta = base_grava * 0.75
expre_uvt = base_excenta / 36308

if expre_uvt > 0 and expre_uvt < 96:
    algoritmo = 0
elif expre_uvt > 95 and expre_uvt < 151:
    algoritmo = (expre_uvt - 95) * 0.19
elif expre_uvt > 150 and expre_uvt < 361:
    algoritmo = ((expre_uvt - 150) * 0.28) + 10
elif expre_uvt > 360 and expre_uvt < 641:
    algoritmo = ((expre_uvt - 360) * 0.33) + 69
elif expre_uvt > 640 and expre_uvt < 946:
    algoritmo = ((expre_uvt - 640) * 0.35) + 162
elif expre_uvt > 945 and expre_uvt < 2301:
    algoritmo = ((expre_uvt - 945) * 0.37) + 268
elif expre_uvt > 2300:
    algoritmo = ((expre_uvt - 2300) * 0.39) + 770




retencion = algoritmo * 36308
print(f"Total devengado: {tot_deven} \n" +
      f"Salud: {salud} \n" +
      f"Pension: {pension} \n" +
      f"Fondo solidaridad: {fondo_sol} \n" +
      f"Base de cotizacion: {base_grava} \n" +
      f"Base excenta (75%): {base_excenta} \n" 
      f"expresado en UVT: {expre_uvt} \n" +
      f"Algoritmo con If anidados: {algoritmo} \n" +
      f"Retencion: {retencion}")
