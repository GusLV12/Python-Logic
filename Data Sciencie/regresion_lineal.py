import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Crear conjunto de datos con gastos en ventas
datos = {
    'Gastos_publicidad': [23, 26, 30, 34, 43, 48, 52, 57, 58],
    'Ventas': [651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518]
}

# Crear dataframe
df = pd.DataFrame(data=datos)

# Separamos las variables en predictora y objetivo, asegurando que x sea 2D
x = df[['Gastos_publicidad']]
y = df['Ventas']

# División en conjunto de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(x_train, y_train)

# Hacer predicciones
y_pred = model.predict(x_test)

# Coeficientes, pendiente e intersección
print('Coeficientes: ', model.coef_)
print('Intersección: ', model.intercept_)
print('Pendiente: ', model.coef_[0])

# Evaluar el modelo
print('Error cuadrático medio: ', mean_squared_error(y_test, y_pred))
print('Coeficiente de determinación (R^2): ', r2_score(y_test, y_pred))

# Visualizar el modelo
plt.scatter(x_test, y_test, color='blue')
plt.plot(x_test, y_pred, color='red', linewidth=3)
plt.title('Regresión lineal simple')
plt.xlabel('Gastos en publicidad')
plt.ylabel('Ventas')
plt.show()
