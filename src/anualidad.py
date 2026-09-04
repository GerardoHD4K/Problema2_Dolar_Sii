#Gerardo Pinilla, Matias Araya

import numpy as np
import matplotlib.pyplot as plt
from cargar_datos import cargar_csv

# Cargamos los datos usando nuestra función
meses, precios = cargar_csv()


# --- A3. Cancelación (dos meses casi iguales) ---
# Diciembre 2022 = índice 11, Diciembre 2023 = índice 23 (12 meses por año, 0 = Enero 2022)
idx_dic2022 = 11
idx_dic2023 = 23

# Redondeamos a 3 cifras significativas. Como los dos precios son de 3 dígitos
# enteros (800-900), 3 cifras significativas = redondear a la unidad (sin decimales)
dic2022_3c = round(precios[idx_dic2022], 0)
dic2023_3c = round(precios[idx_dic2023], 0)

delta_p = dic2023_3c - dic2022_3c

ea_dic2022 = abs(precios[idx_dic2022] - dic2022_3c)
ea_dic2023 = abs(precios[idx_dic2023] - dic2023_3c)

# Propagación en la resta: se suman los errores absolutos
ea_delta = ea_dic2022 + ea_dic2023
er_delta = (ea_delta / abs(delta_p)) * 100

print("A3.", meses[idx_dic2022], "->", dic2022_3c, " | ", meses[idx_dic2023], "->", dic2023_3c)
print(f"    Delta P = {delta_p:.1f} +- {ea_delta:.1f} pesos  (Error: {er_delta:.1f}%)")


# --- A4. Anualidad (variación enero -> diciembre, por año) ---
anios = [2022, 2023, 2024, 2025]
resultados_anualidad = []  # aquí guardamos (anio, delta, ea, er) de cada año

for i in range(4):
    idx_enero = i * 12          # 0, 12, 24, 36
    idx_diciembre = i * 12 + 11  # 11, 23, 35, 47

    p_enero = precios[idx_enero]
    p_diciembre = precios[idx_diciembre]

    # Redondeo a 2 cifras significativas, igual criterio que en A1
    if p_enero < 1000:
        enero_2c = round(p_enero, -1)
    else:
        enero_2c = round(p_enero, -2)

    if p_diciembre < 1000:
        diciembre_2c = round(p_diciembre, -1)
    else:
        diciembre_2c = round(p_diciembre, -2)

    delta_anual = diciembre_2c - enero_2c

    ea_enero = abs(p_enero - enero_2c)
    ea_diciembre = abs(p_diciembre - diciembre_2c)
    ea_anual = ea_enero + ea_diciembre  # resta -> se suman absolutos

    er_anual = (ea_anual / abs(delta_anual)) * 100 if delta_anual != 0 else float('inf')

    resultados_anualidad.append((anios[i], delta_anual, ea_anual, er_anual))

print("\nA4.")
for anio, delta_anual, ea_anual, er_anual in resultados_anualidad:
    print(f"    {anio}: Delta = {delta_anual:.1f} +- {ea_anual:.1f} pesos  (Error: {er_anual:.1f}%)")


# --- Guardamos todo en un CSV (tabla de salida obligatoria de la sección 8) ---
with open("data/resultados_anualidad.csv", "w") as f:
    f.write("par,delta,error_absoluto,error_relativo_pct\n")
    f.write(f"dic2023_menos_dic2022,{delta_p:.2f},{ea_delta:.2f},{er_delta:.2f}\n")
    for anio, delta_anual, ea_anual, er_anual in resultados_anualidad:
        f.write(f"dic{anio}_menos_ene{anio},{delta_anual:.2f},{ea_anual:.2f},{er_anual:.2f}\n")

print("\nResultados guardados en data/resultados_anualidad.csv")

#GRÁFICO OBLIGATORIO
# 2. Variación mes a mes (Delta P) en barras para ver el efecto cancelación
deltas_mes = np.diff(precios)

# Calculamos el error absoluto de todos los meses para arrastrarlo a las restas
precios_2c_arr = []
for p in precios:
    if p < 1000:
        precios_2c_arr.append(round(p, -1))
    else:
        precios_2c_arr.append(round(p, -2))
precios_2c_arr = np.array(precios_2c_arr)

ea_todos = np.abs(precios - precios_2c_arr)

# Propagación: en la resta de mes a mes, se suman los errores absolutos de ambos meses
ea_deltas = ea_todos[1:] + ea_todos[:-1] 
meses_diff = meses[1:] # Le quitamos enero 2022 porque la primera variación es en febrero

plt.figure(figsize=(14, 6))
# Se usa yerr para agregar las barras de error sobre las barras de variación
plt.bar(meses_diff, deltas_mes, yerr=ea_deltas, capsize=3, color='orange', ecolor='black')
plt.axhline(0, color='black', linewidth=1)
plt.title("2. Variación mes a mes con error propagado (Efecto Cancelación)")
plt.xlabel("Meses")
plt.ylabel("Variación de Precio (CLP)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("../Problema2_Dolar_Sii/graficos/grafico2_variacion_mes.png")
plt.close()

print("\nGráfico 2 guardado en ../Problema2_Dolar_Sii/graficos/")