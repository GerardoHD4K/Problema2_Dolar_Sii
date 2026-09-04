# Respuestas: Anualidad y Punto Flotante
## A1 Error de representacion mes a mes
Para aplicar las 2 cifras significativas de la mantisa corta, los precios se redondearon a la decena más cercana (si eran menores a 1000) o a la centena (si eran mayores a 1000). El mes que sufrió el mayor error relativo tras el redondeo fue Abril de 2022. Su precio original era 815.12, y al guardarse con 2 cifras se registró como 820.0. Esto generó un error absoluto de 4.88 pesos, lo que equivale a un error relativo del 0.60%.

## A2 Evaluacion entre dos puntos
Simulando una compra con el precio aproximado de Febrero 2022 y una venta en Octubre 2022 con un monto inicial de *M* = 1000000, la ganancia final obtenida fue de 185.185,2 +- 9.398,6 pesos. Al propagar los errores relativos de ambas operaciones y arrastrarlos a la ganancia, el margen de incertidumbre representa un error porcentual del   5.08% respecto al beneficio total.
## A3. Cancelacion (Dic 2022 vs Dic 2023)
ΔP = -1.0 ± 0.7 (error 67%). Se sabe que bajó, pero no cuánto: el error
es casi igual al resultado (cancelación).

## A4. Anualidad
| Año | Delta | Error |
|-----|-------|-------|
| 2025 | -80.0 | 5.8% |
| 2024 | +70.0 | 6.2% |
| 2022 | +60.0 | 10.6% |
| 2023 | +40.0 | 20.8% |

## A5. Mejor compra y Mejor venta
El mes más barato de todo el período fue Febrero de 2023, mientras que el más caro fue Enero de 2025. Al ejecutar la jugada maestra comprando en el mínimo y vendiendo en el máximo, la ganancia se calcula en 250.000,0 +- 3.674,0 pesos. La conclusión de que esta es la mejor rentabilidad sobrevive totalmente al error, ya que la ganancia es muchísimo mayor que la incertidumbre acumulada.

2023 es el menos confiable: tuvo el cambio más chico, así que el mismo
error de redondeo pesa más.

## B1. Mantisa corta
Pocas cifras significativas = pocos bits de mantisa. Ej: 1000.76 → 1000
(error 0.76).

## B2. Ida y vuelta
Drift ≈ ±1.16×10⁻¹⁰ pesos. Es ruido de la máquina (float64), no tiene
relación con el dólar.

## B4. Cancelación en la máquina
874.67 − 875.66 → float32: -0.98999..., float64: -0.99000000...
float32 pierde más cifras que float64. Mismo problema que A3, ahora en
el hardware.
