from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

def entrenar_regresion_lineal(df, target_col='DESERCIÓN'):
    
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Dividir los datos en entrenamiento (80%) y prueba (20%)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    # Realizar predicciones sobre el conjunto de prueba
    y_pred = modelo.predict(X_test)

    # Crear un reporte con las métricas de evaluación
    reporte = {
        'R2': r2_score(y_test, y_pred),  # Coeficiente de determinación R2
        'MAE': mean_absolute_error(y_test, y_pred),  # Error absoluto medio
        'RMSE': np.sqrt(mean_squared_error(y_test, y_pred)),  # Raíz del error cuadrático medio
        'Coeficientes': dict(zip(X.columns, modelo.coef_))  # Coeficientes de la regresión lineal
    }

    # Retornar el modelo entrenado y el reporte de evaluación
    return modelo, reporte

