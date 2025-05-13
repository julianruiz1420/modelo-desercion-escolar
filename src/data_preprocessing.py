import pandas as pd


def cargar_datos(ruta):
       
    return pd.read_csv(r"D:\mi_proyecto\data\raw\educacion_original.csv")



def transformar_datos(df):
       
       df['DEPARTAMENTO'] = df['DEPARTAMENTO'].replace({'BOGOTA_DC': 'BOGOTA_D.C.'})
       
       columnas_a_eliminar = ["POBLACIÓN_5_16","AÑO","CÓDIGO_DEPARTAMENTO","TASA_MATRICULACIÓN_5_16","CODIGO_DIVIPOLA","COBERTURA_BRUTA","COBERTURA_BRUTA_TRANSICIÓN","COBERTURA_BRUTA_PRIMARIA","COBERTURA_BRUTA_SECUNDARIA"
                            ,"COBERTURA_BRUTA_MEDIA","APROBACIÓN","APROBACIÓN_TRANSICIÓN","APROBACIÓN_PRIMARIA","APROBACIÓN_SECUNDARIA"
                            ,"APROBACIÓN_MEDIA","REPITENCIA_TRANSICIÓN","REPITENCIA_PRIMARIA","REPITENCIA_SECUNDARIA","REPITENCIA_MEDIA",
                            "COBERTURA_NETA_TRANSICIÓN","COBERTURA_NETA_PRIMARIA","COBERTURA_NETA_SECUNDARIA","COBERTURA_NETA_MEDIA","REPROBACIÓN_TRANSICIÓN",
                            "REPROBACIÓN_PRIMARIA","REPROBACIÓN_SECUNDARIA","REPROBACIÓN_MEDIA", "DEPARTAMENTO","DESERCIÓN_TRANSICIÓN","DESERCIÓN_PRIMARIA","DESERCIÓN_SECUNDARIA","DESERCIÓN_MEDIA"]
       
       
       return df.drop(columns = columnas_a_eliminar, errors='ignore')