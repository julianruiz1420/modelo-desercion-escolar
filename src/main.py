import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_preprocessing import cargar_datos, transformar_datos
from src.limpieza_datos import limpiar_datos
from src.model import entrenar_regresion_lineal


# Paso 1: Cargar y limpiar

df = cargar_datos("data/educacion_limpia.csv")
df = limpiar_datos(df)
df = transformar_datos(df)

print(df.head())

# Paso 2: Entrenar modelo

modelo, reporte = entrenar_regresion_lineal(df)

# Paso 3: Mostrar resultados

print("Reporte de evaluación:")
for k, v in reporte.items():
    print(f"{k}: {v}")
