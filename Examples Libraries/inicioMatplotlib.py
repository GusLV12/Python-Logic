import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 200, 200)
y = x + x**2

#Crreando grafico
plt.plot(x, y, 'blue')
plt.title('Mi grafica')
plt.xlabel('Eje x')
plt.ylabel('Eje y')

#mostar grafico
plt.show()

#Subplot de graficos
plt.subplot(1,2,1)
plt.plot(x, y, 'red')
plt.subplot(1,2,2)
plt.plot(y, x, 'green')
plt.show()