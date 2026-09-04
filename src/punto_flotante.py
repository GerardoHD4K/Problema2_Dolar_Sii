#Gerardo Pinilla, Matias Araya

import numpy as np
import matplotlib.pyplot as plt
from cargar_datos import cargar_csv

meses, precios = cargar_csv()
monto = 1000000  # El millón de pesos inicial


# --- B1. Cifras significativas = mantisa corta ---
precio_ej = 1000.76
precio_ej_3c = round(precio_ej, -1)  # 1000.76 tiene 4 dígitos enteros -> 3 cifras = redondear a la decena
error_representacion = abs(precio_ej - precio_ej_3c)
print(f"B1. {precio_ej} con 3 cifras significativas -> {precio_ej_3c}  (error: {error_representacion:.2f})")


# --- B2. La ida y vuelta que no vuelve ---
drift_lista = []  # cuánto nos "desviamos" del monto original, mes a mes

for p in precios:
    usd = monto / p              # compramos dólares (división)
    pesos_recuperados = usd * p  # los vendemos de vuelta al mismo precio (multiplicación)
    drift = pesos_recuperados - monto
    drift_lista.append(drift)

drift_array = np.array(drift_lista)

print(f"\nB2. Drift minimo: {drift_array.min():.2e}")
print(f"Drift maximo: {drift_array.max():.2e}")
print(f"Drift promedio: {drift_array.mean():.2e}")

# Gráfico obligatorio #5: deriva de la ida y vuelta en punto flotante
plt.figure(figsize=(10, 5))
plt.plot(meses, drift_array, marker='o')
plt.xticks(rotation=90)
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.title("B2 - Deriva (drift) de la ida y vuelta en punto flotante")
plt.xlabel("Mes")
plt.ylabel("Pesos recuperados - Monto original")
plt.tight_layout()
plt.savefig("graficos/grafico5_puntoflotante_B2.png")
plt.close()
print("Gráfico guardado en graficos/b2_drift_punto_flotante.png")


# --- B4. Cancelación en la máquina ---
a32 = np.float32(874.67)
b32 = np.float32(875.66)
resta_32 = a32 - b32

a64 = np.float64(874.67)
b64 = np.float64(875.66)
resta_64 = a64 - b64

print(f"\nB4. Resta en float32: {resta_32}")
print(f"    Resta en float64: {resta_64}")
print(f"    Diferencia entre ambos resultados: {abs(float(resta_32) - float(resta_64)):.2e}")


# --- Guardamos los resultados de B2 y B4 en CSV ---
with open("data/resultados_punto_flotante.csv", "w") as f:
    f.write("mes,drift_pesos\n")
    for i in range(len(meses)):
        f.write(f"{meses[i]},{drift_array[i]:.2e}\n")

print("\nResultados guardados en data/resultados_punto_flotante.csv")