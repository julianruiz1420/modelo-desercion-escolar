🌍 Resumen del Proyecto

Este proyecto de ciencia de datos tiene como objetivo predecir la deserción escolar en los niveles de transición, primaria, secundaria y media en Colombia, a partir de indicadores recopilados por el Ministerio de Educación Nacional. Utilizando datos oficiales por departamento y año, se busca identificar los factores que inciden en la desercion escolar para orientar intervenciones tempranas y políticas educativas.

📆 Dataset utilizado

Fuente: Datos Abiertos Colombia

Archivo: MEN_ESTADISTICAS_EN_EDUCACION_EN_PREESCOLAR__B_SICA_Y_MEDIA_POR_DEPARTAMENTO_20250504.csv

Periodo: Varios años (longitudinal)

Cobertura: Departamentos de Colombia


📊 Variables del Dataset

Target variable (objetivo):

DESERCIÓN, DESERCIÓN_TRANSICIÓN, DESERCIÓN_PRIMARIA, DESERCIÓN_SECUNDARIA, DESERCIÓN_MEDIA


Variables predictoras:

AÑO, DEPARTAMENTO

POBLACIÓN_5_16, TASA_MATRÍCULACIÓN_5_16

COBERTURA_NETA_*, COBERTURA_BRUTA_*

APROBACIÓN, REPROBACIÓN, REPITENCIA

TAMAÑO_PROMEDIO_DE_GRUPO, SEDES_CONECTADAS_A_INTERNET


🚀 Objetivos Específicos

Analizar y visualizar los patrones históricos de la desercion escolar por nivel educativo y departamento.

Construir un modelo predictivo de desercion a partir de variables socioeducativas.

Evaluar el desempeño del modelo con métricas apropiadas.

Identificar los factores más influyentes asociados a la desercion.


📅 Paso a paso del Proyecto

Recolección y carga de datos:

Lectura del CSV, inspección general, limpieza de valores faltantes y tipos.

Análisis Exploratorio de Datos (EDA):

Estadísticas descriptivas

Correlaciones entre variables

Visualizaciones: mapas, series temporales, boxplots por región

Preprocesamiento:

Encoding de DEPARTAMENTO

Normalización / estandarización de variables numéricas

Tratamiento de outliers y nulos

Feature engineering:

Variables derivadas (p. ej., tasas por cada 1000 estudiantes)

Combinaciones de cobertura y conectividad

Modelado:

Algoritmos: regresión lineal, Random Forest, Gradient Boosting

Validación cruzada (K-Fold)

División en entrenamiento/test (80/20)

Evaluación:

Métricas: MAE, RMSE, R^2

Feature importance

Conclusiones y Recomendaciones

Acciones para mitigar desercion según hallazgos

Ingeniería de características
En src/feature_engineering.py:

Crear nuevas variables útiles como:

TASA_DESERCION = DESERCIÓN / MATRÍCULA_TOTAL

Promedios móviles por departamento y nivel educativo

Agrupar datos por año o departamento si se requiere



🔹 Indicadores clave

Tasa de desercion general y por nivel

Cobertura neta y bruta

Relación aprobación-reprobación

Conectividad escolar por región


🤔 Motivación

En muchos estudios sobre calidad educativa en Colombia, se priorizan indicadores de cobertura y aprobación, dejando en segundo plano las tasas de desercion y sus causas. Este proyecto pretende cambiar ese enfoque proponiendo un sistema predictivo accesible que ayude a formular mejores políticas educativas.


🎨 Futuras extensiones

Predicción de repitencia o reprobación

Modelos por región o municipio

Visualizaciones interactivas con dashboards

Integración con datos socioeconómicos (DANE, Sisbén)