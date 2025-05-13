import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def limpiar_datos(df):

    mediana_internet = df['SEDES_CONECTADAS_A_INTERNET'].median()
    df['SEDES_CONECTADAS_A_INTERNET'] = df['SEDES_CONECTADAS_A_INTERNET'].fillna(mediana_internet)

    media_grupo = df['TAMAÑO_PROMEDIO_DE_GRUPO'].mean()
    df['TAMAÑO_PROMEDIO_DE_GRUPO'] = df['TAMAÑO_PROMEDIO_DE_GRUPO'].fillna(media_grupo)

    media_desercion = df['DESERCIÓN_TRANSICIÓN'].mean()
    df['DESERCIÓN_TRANSICIÓN'] = df['DESERCIÓN_TRANSICIÓN'].fillna(media_desercion)


    df['DEPARTAMENTO'] = df['DEPARTAMENTO'].str.strip() \
        .str.replace(' ', '_') \
        .str.replace('á', 'a') \
        .str.replace('é', 'e') \
        .str.replace('í', 'i') \
        .str.replace('ó', 'o') \
        .str.replace('ú', 'u') \
        .str.replace(',', '') \
        .str.upper()

    df['DEPARTAMENTO'] = df['DEPARTAMENTO'].replace({'BOGOTA_DC': 'BOGOTA_D.C.'})
    
    if 'AÑO' in df.columns:
        df['AÑO'] = pd.to_numeric(df['AÑO'], errors='coerce')

    if 'DEPARTAMENTO' in df.columns:
        df['DEPARTAMENTO'] = df['DEPARTAMENTO'].astype('category')


    # Guardar en carpeta procesada
    output_dir = r"D:\mi_proyecto\data\processed"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "educacion_limpia.csv")
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"Archivo limpio guardado en '{output_path}'")

    return df
