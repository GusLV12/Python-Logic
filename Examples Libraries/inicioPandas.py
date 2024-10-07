import pandas as pd
import numpy as np

tags = ['a', 'b', 'c', 'd', 'e']
data = np.arange(4,9)
serie = pd.Series(data, index=tags)
print(serie)

#Acceder valor de la serie
print(serie['c'])

#Datos de dis5tintos tipos
data = ['Jose', 60, 'Mar', 46]
serie = pd.Series(data)
print(serie)

#Datos directos
serie = pd.Series([1,2,3,4,5], ['a', 'b', 'c', 'd', 'e'])
print(serie)

#Suma de series
serie1 = pd.Series([1,2,3,4,5], ['ini1', 'ini2', 'ini3', 'ini4', 'ini5'])
serie2 = pd.Series([10,20,30,40,50],['ini1', 'ini2', 'ini3', 'ini4', 'ini5'])
serie3 = serie1 + serie2
print(serie3)

#dataframe
row = ['tienda1', 'tienda2', 'tienda3', 'tienda4']
column = ['leche', 'huevos', 'pan', 'carne']
data = [[224, 34, 234, 343], [23, 43, 23, 43], [203, 23, 43, 23], [23, 43, 23, 43]]
dataframe = pd.DataFrame(data, row, column)
print('Data frame: ')
print(dataframe)

#Selecion de fila
print('Seleccion de fila: ')
print(dataframe.loc['tienda2'])
print(dataframe.loc[['tienda1','tienda2']])

#Seleccion de columna
print('Seleccion de columna: ')
print(dataframe['leche'])

#Valor de una celda
print('Valor de una celda: ')
print(dataframe.loc['tienda2']['carne'])