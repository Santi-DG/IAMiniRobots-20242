# 6.1
Tome una ecuación determinada, por ejemplo una raíz cúbica, o un seno, genere un data set con muchos valores. Con base en ese data set y utilizando una herramienta de ML, encuentre un modelo para el cálculo de la raíz cuadrada. Úselo con 10 ejemplos y compare los resultados con los que da la función del lenguaje.

#### 1. Generación del Conjunto de Datos
` x = np.linspace(-5, 5, 1000) `
` y = np.sin(x) `

#### 2. Dividir los datos en conjuntos de entrenamiento y prueba
` x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42) `

#### 3. Entrenar un modelo de regresión de bosque aleatorio
` model = RandomForestRegressor(n_estimators=100, random_state=42) `
` model.fit(x_train.reshape(-1, 1), y_train) `

#### 4. Generar 10 ejemplos de valores de entrada
` x_examples = np.random.uniform(-5, 5, 10) `

#### 5. Calcular las predicciones del modelo
` y_pred = model.predict(x_examples.reshape(-1, 1)) `

#### Calcular los valores reales de la función seno
` y_true = np.sin(x_examples) `

#### Imprimir los resultados
` print("Valores de entrada:", x_examples) `
` print("Predicciones del modelo:", y_pred) `
` print("Valores reales de la función seno:", y_true) `

#### Calcular el error cuadrático medio
` mse = mean_squared_error(y_true, y_pred) `
` print("Error cuadrático medio:", mse) `
