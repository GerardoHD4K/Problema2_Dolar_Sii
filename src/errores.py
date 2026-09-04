import numpy as np
import matplotlib.pyplot as plt
from cargar_datos import cargar_csv

# Cargamos los datos
meses, precios = cargar_csv()
monto = 1000000 # El millón de pesos inicial

print("--- RESPUESTAS SECCIÓN A ---")

# A1. Error de representación mes a mes
precios_2c = np.where(precios < 1000, np.round(precios, -1), np.round(precios, -2))

# Calculamos los errores (esto ya está vectorizado de forma nativa)
errores_absolutos = np.abs(precios - precios_2c)
errores_relativos = (errores_absolutos / precios) * 100

idx_max_err = np.argmax(errores_relativos)
print(f"\nA1. Mayor error relativo al redondear: {meses[idx_max_err]} con {errores_relativos[idx_max_err]:.2f}%")
print(f"(Precio real: {precios[idx_max_err]}, Guardado como: {precios_2c[idx_max_err]})")


# A2. Evaluación entre dos puntos (una compra-venta)
idx_compra = 1 # Índice 1 = Febrero 2022
idx_venta = 9  # Índice 9 = Octubre 2022
p_compra = precios_2c[idx_compra]
p_venta = precios_2c[idx_venta]

print(f"\nA2. Simulando compra en {meses[idx_compra]} y venta en {meses[idx_venta]}")
usd = monto / p_compra
pesos_final = usd * p_venta
ganancia = pesos_final - monto

# Propagamos el error sumando los relativos
err_rel_total = errores_relativos[idx_compra] + errores_relativos[idx_venta]
err_abs_final = (err_rel_total / 100) * pesos_final

print(f"Ganancia: {ganancia:.1f} +- {err_abs_final:.1f} pesos")
print(f"Error porcentual: {(err_abs_final/ganancia)*100:.2f}%")


# A5. Mejor compra y mejor venta 
idx_min = np.argmin(precios)
idx_max = np.argmax(precios)
p_min_aprox = precios_2c[idx_min]
p_max_aprox = precios_2c[idx_max]

print(f"\nA5. El mes más barato fue {meses[idx_min]} y el más caro fue {meses[idx_max]}")

ganancia_max = (monto / p_min_aprox) * p_max_aprox - monto
err_rel_max_jugada = errores_relativos[idx_min] + errores_relativos[idx_max]
err_abs_max = (err_rel_max_jugada / 100) * ((monto / p_min_aprox) * p_max_aprox)

print(f"Jugada maestra: Ganancia {ganancia_max:.1f} +- {err_abs_max:.1f} pesos")

#GRÁFICOS 
# Gráfico 1: Serie mensual del dólar observado 2022-2025
plt.figure(figsize=(10, 5))
plt.plot(meses, precios, marker='o', color='b')
plt.title("1. Serie mensual del dólar observado 2022-2025")
plt.xlabel("Meses")
plt.ylabel("Precio (CLP)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("../Problema2_Dolar_Sii/graficos/grafico1_serie_mensual.png")
plt.close()

# Gráfico 3: Error de representación por mes
plt.figure(figsize=(10, 5))
plt.bar(meses, errores_absolutos, color='r')
plt.title("3. Error de representación absoluto por mes al usar 2 cifras sig.")
plt.xlabel("Meses")
plt.ylabel("Error Absoluto (CLP)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("../Problema2_Dolar_Sii/graficos/grafico3_error_representacion.png")
plt.close()

# Gráfico 4: Rentabilidad de comprar en el mínimo y vender después
rentabilidades = []
errores_renta = []
meses_post = meses[idx_min:]

# Calculamos la rentabilidad y propagamos el error para los meses posteriores a la compra
for i in range(idx_min, len(precios)):
    gan_temp = (monto / p_min_aprox) * precios_2c[i] - monto
    rent = (gan_temp / monto) * 100
    rentabilidades.append(rent)
    errores_renta.append(errores_relativos[idx_min] + errores_relativos[i])

plt.figure(figsize=(10, 5))
plt.errorbar(meses_post, rentabilidades, yerr=errores_renta, fmt='-o', color='g', ecolor='red', capsize=4)
plt.title("4. Rentabilidad comprando en el mínimo y vendiendo cada mes posterior")
plt.xlabel("Meses")
plt.ylabel("Rentabilidad (%)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("../Problema2_Dolar_Sii/graficos/grafico4_rentabilidad.png")
plt.close()

print("\nGráficos 1, 3 y 4 guardados en ../Problema2_Dolar_Sii/graficos/")