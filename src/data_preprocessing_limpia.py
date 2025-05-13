

import pandas as pd

# Cargar los datos como objeto para llamarlos en mis otros script

def cargar_y_preparar_datos(ruta_csv):
       
       ruta_csv = "D:\mi_proyecto\data\processed\educacion_limpia.csv"
       
       df = pd.read_csv(ruta_csv)
       
       # ver la cantidad de filas y los encabezados de mi dataset
       print(df.columns)
       print("-----------------Dataset---------------------------------")
       # Ver las primeras filas
       print(df.head())
       print("-----------------Tabla info---------------------------------")
       # Ver información general
       print(df.info())

       print("-----------------Tabla describe---------------------------------")
       # Estadísticas descriptivas
       print(df.describe().T)


       df_columnas = ['AÑO','CÓDIGO_DEPARTAMENTO', 'DEPARTAMENTO', 'POBLACIÓN_5_16',
       'TASA_MATRICULACIÓN_5_16', 'COBERTURA_NETA',
       'COBERTURA_NETA_TRANSICIÓN', 'COBERTURA_NETA_PRIMARIA',
       'COBERTURA_NETA_SECUNDARIA', 'COBERTURA_NETA_MEDIA', 'COBERTURA_BRUTA',
       'COBERTURA_BRUTA_TRANSICIÓN', 'COBERTURA_BRUTA_PRIMARIA',
       'COBERTURA_BRUTA_SECUNDARIA', 'COBERTURA_BRUTA_MEDIA',
       'TAMAÑO_PROMEDIO_DE_GRUPO', 'SEDES_CONECTADAS_A_INTERNET', 'DESERCIÓN',
       'DESERCIÓN_TRANSICIÓN', 'DESERCIÓN_PRIMARIA', 'DESERCIÓN_SECUNDARIA',
       'DESERCIÓN_MEDIA', 'APROBACIÓN', 'APROBACIÓN_TRANSICIÓN',
       'APROBACIÓN_PRIMARIA', 'APROBACIÓN_SECUNDARIA', 'APROBACIÓN_MEDIA',
       'REPROBACIÓN', 'REPROBACIÓN_TRANSICIÓN', 'REPROBACIÓN_PRIMARIA',
       'REPROBACIÓN_SECUNDARIA', 'REPROBACIÓN_MEDIA', 'REPITENCIA',
       'REPITENCIA_TRANSICIÓN', 'REPITENCIA_PRIMARIA', 'REPITENCIA_SECUNDARIA',
       'REPITENCIA_MEDIA']

       # Analisis univariado

       # metricas de df_columnas

       df_max = df[df_columnas].max(numeric_only=True) # Solo toma columnas numéricas

       df_min = df[df_columnas].min(numeric_only=True) # Solo toma columnas numéricas

       df_mean = df[df_columnas].mean(numeric_only=True) # Solo toma columnas numéricas

       df_std = df[df_columnas].std(numeric_only=True) # Solo toma columnas numéricas

       df_dtypes = df[df_columnas].dtypes

       df_shape = df[df_columnas].shape

       df_isnull = df.isnull().sum() # Valores faltantes por columna

       df_count = df[df_columnas].count()

       df_nulos_vs_total_de_datos = (df.isnull().sum() / len(df)) * 100


       #df_total_vs_nulos = 


       print(f"El dataset contiene entre filas y colunas", df_shape)


       print("-----------------Tabla resumen--------------------------------")


       tabla_resumen = pd.DataFrame({'Tipo de dato':df_dtypes,"Total de datos": df_count, "Valores nulos": df_isnull,"% nulos":df_nulos_vs_total_de_datos, "Valores Maximos": df_max,
                              "Valores minimos": df_min, "Meadianas": df_mean,"Desviación estandar": df_std})

       print(tabla_resumen)



       # Diccionario de clasificación por región

       region_dict = {
       # Región Andina
       "ANTIOQUIA": "Andina", "BOGOTA_D.C.": "Andina", "BOGOTA_DC": "Andina",
       "BOYACA": "Andina", "CALDAS": "Andina", "CUNDINAMARCA": "Andina",
       "HUILA": "Andina", "NORTE_DE_SANTANDER": "Andina", "QUINDIO": "Andina",
       "RISARALDA": "Andina", "SANTANDER": "Andina", "TOLIMA": "Andina",

       # Región Caribe
        "ATLANTICO": "Caribe", "BOLIVAR": "Caribe", "CESAR": "Caribe",
        "CORDOBA": "Caribe", "LA_GUAJIRA": "Caribe", "MAGDALENA": "Caribe",
        "SUCRE": "Caribe", "ARCHIPIELAGO_DE_SAN_ANDRES_PROVIDENCIA_Y_SANTA_CATALINA": "Caribe",

       # Región Pacífica
        "CAUCA": "Pacífica", "CHOCO": "Pacífica", "NARIÑO": "Pacífica", "VALLE_DEL_CAUCA": "Pacífica",

        # Región Orinoquía
        "ARAUCA": "Orinoquía", "CASANARE": "Orinoquía", "META": "Orinoquía", "VICHADA": "Orinoquía",

       # Región Amazonía
        "AMAZONAS": "Amazonía", "CAQUETA": "Amazonía", "GUAINIA": "Amazonía",
        "GUAVIARE": "Amazonía", "PUTUMAYO": "Amazonía", "VAUPES": "Amazonía"
       }

       # Crear nueva columna

       df["REGIÓN"] = df["DEPARTAMENTO"].map(region_dict)

       print(df.head())

       return df
