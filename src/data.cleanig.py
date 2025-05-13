#  limpieza y transformación de datos
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def limpiar_datos (df_limpia):
    
    from src.data_preprocessing_limpia import cargar_y_preparar_datos

    # Ruta al archivo CSV

    ruta_csv = "D:\mi_proyecto\data\raw\educacion_original.csv"

    # Cargar y procesar los datos

    df = cargar_y_preparar_datos(ruta_csv)


    # limpieza de variable SEDES_CONECTADAS_A_INTERNET

    """print(df["SEDES_CONECTADAS_A_INTERNET"])

    sns.histplot(df["SEDES_CONECTADAS_A_INTERNET"], kde=True)
    plt.title('Distribución de la variable')
    plt.show()

    sns.boxplot(x=df["SEDES_CONECTADAS_A_INTERNET"])
    plt.title('Boxplot de la variable')
    plt.show()

    # Se imputa con la mediana al percibir valores extremos (outliers)."""

    df_mediana = df['SEDES_CONECTADAS_A_INTERNET'].median()

    df['SEDES_CONECTADAS_A_INTERNET'] = df['SEDES_CONECTADAS_A_INTERNET'].fillna(df_mediana)



    # limpieza de variable TAMAÑO_PROMEDIO_DE_GRUPO

    df_median = df['TAMAÑO_PROMEDIO_DE_GRUPO'].mean()

    df['TAMAÑO_PROMEDIO_DE_GRUPO'] = df['TAMAÑO_PROMEDIO_DE_GRUPO'].fillna(df_median)


    # # limpieza de variable TDESERCIÓN_TRANSICIÓN

    df_median = df['DESERCIÓN_TRANSICIÓN'].mean()

    df['DESERCIÓN_TRANSICIÓN'] = df['DESERCIÓN_TRANSICIÓN'].fillna(df_median)


    df_isnull = df.isnull().sum() # Valores faltantes por columna

    print(df_isnull)



    # Renombrar columnas para estandarizar

    # quitar espacios y tildes, pasar a mayúsculas de la columna DEPARTAMENTO

    print(df.columns.tolist())


    df['DEPARTAMENTO'] = df['DEPARTAMENTO'].str.strip().str.replace(' ', '_').str.replace('á', 'a') \
             .str.replace('é', 'e').str.replace('í', 'i').str.replace('ó', 'o') \
             .str.replace('ú', 'u').str.upper().str.replace(',', '')
             
    print(df["DEPARTAMENTO"])

    # Conversión de tipos de datos básicos
    if 'AÑO' in df.columns:
    df['AÑO'] = pd.to_numeric(df['AÑO'], errors='coerce')

    if 'DEPARTAMENTO' in df.columns:
    df['DEPARTAMENTO'] = df['DEPARTAMENTO'].astype('category')
    
    print(df.dtypes)
        
    # Guardar versión limpia (opcional)
    
    df.to_csv("./data/educacion_limpia.csv", index=False, encoding='utf-8')

    print("\nArchivo limpio guardado como 'educacion_limpia.csv'")

    return df_limpia