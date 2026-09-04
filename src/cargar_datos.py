#Gerardo Pinilla, Matias Araya

import numpy as np

def cargar_csv():
    # Como tu terminal se ejecuta desde la carpeta principal del proyecto,
    # solo le indicamos que entre directamente a "data/"
    precios = np.genfromtxt('data/dolar_observado_sii_2022_2025.csv', delimiter=',', usecols=3)
    
    # Limpiamos si hay encabezado
    if np.isnan(precios[0]):
        precios = precios[1:]
        
    # Armamos a mano la lista de los meses para no perdernos.
    nombres_base = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    meses_texto = []
    for anio in [2022, 2023, 2024, 2025]:
        for mes in nombres_base:
            meses_texto.append(f"{mes} {anio}")
            
    # Devolvemos las dos listas juntas
    return meses_texto, precios

if __name__ == "__main__":
    meses, mis_datos = cargar_csv()
    
    print(f"Total cargado: {len(mis_datos)} meses.")
    print(f"El primer mes es {meses[0]} y el dólar estaba a {mis_datos[0]}")
    print(f"El último mes es {meses[-1]} y el dólar estaba a {mis_datos[-1]}")