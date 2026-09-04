# Respuestas: Anualidad y Punto Flotante

## A3. Cancelación (Dic 2022 vs Dic 2023)
ΔP = -1.0 ± 0.7 (error 67%). Se sabe que bajó, pero no cuánto: el error
es casi igual al resultado (cancelación).

## A4. Anualidad
| Año | Delta | Error |
|-----|-------|-------|
| 2025 | -80.0 | 5.8% |
| 2024 | +70.0 | 6.2% |
| 2022 | +60.0 | 10.6% |
| 2023 | +40.0 | 20.8% |

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
