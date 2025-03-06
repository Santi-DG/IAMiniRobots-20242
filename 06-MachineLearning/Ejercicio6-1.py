import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Generar el conjunto de datos
x = np.linspace(-5, 5, 1000)
y = np.sin(x)

# Dividir los datos en conjuntos de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Entrenar un modelo de regresión de bosque aleatorio
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(x_train.reshape(-1, 1), y_train)

# Generar 10 ejemplos de valores de entrada
x_examples = np.random.uniform(-5, 5, 10)

# Calcular las predicciones del modelo
y_pred = model.predict(x_examples.reshape(-1, 1))

# Calcular los valores reales de la función seno
y_true = np.sin(x_examples)

# Imprimir los resultados
print("Valores de entrada:", x_examples)
print("Predicciones del modelo:", y_pred)
print("Valores reales de la función seno:", y_true)

# Calcular el error cuadrático medio
mse = mean_squared_error(y_true, y_pred)
print("Error cuadrático medio:", mse)