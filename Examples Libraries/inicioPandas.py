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

#Nueva columna
dataframe["lechuga"] = 40
print('Nueva columna: ')
print(dataframe)
dataframe["total"] = dataframe['leche'] + dataframe['huevos'] + dataframe['pan'] + dataframe['carne'] + dataframe['lechuga']
print('Total: ')
print(dataframe)

#Nueva fila
dataframe.loc['tienda5'] = [23, 45, 23, 43, 23, 157]
print('Nueva fila: ')
print(dataframe)

# eliminar colujmna
dataframe = dataframe.drop('huevos', axis=1) #Se utiliza axis=1 para indicar que es una columna
print('Eliminar columna: ')
print(dataframe)

#condificiones en dataframes
print('Condiciones en dataframes: ')
condicion = dataframe > 200
print(dataframe[condicion])

#Añadiendo inidices
newColumn = [1,2,3,4,5]
dataframe['indice'] = newColumn #Agregando inidce
print('Añadiendo indices: ')
dataframe = dataframe.set_index('indice') #Cambiando el datatframe
print(dataframe)

#Eliminando indice
print('Eliminando indice: ')
dataframe = dataframe.reset_index() #Eliminando el indice
print(dataframe)

#Union de dataframes
data1 = {'A': [1,2,3], 'B': [4,5,6]}
data2 = {'C': [7,8,9], 'D': [10,11,12]}
dataframe1 = pd.DataFrame(data1)
dataframe2 = pd.DataFrame(data2)
print('Union de dataframes: ')
print(pd.concat([dataframe1, dataframe2], axis=1)) #Union de dataframes por columnas

#Union de dataframes por filas
print('Union de dataframes por filas: ')
dataframe3 = pd.concat([dataframe1, dataframe2], axis=0)
print(dataframe3) #Union de dataframes por filas

#Rellenar valores faltantes
media = dataframe.mean()
print(f'La media es igual a: {media}')
dataframe3 = dataframe3.fillna(value=media, inplace=True)
print('Rellenar valores faltantes: ')
print(dataframe3)

# Datos unicos
print('Datos unicos: ')
print(dataframe['leche'].unique()) #unique nos devuelve los valores unicos de una columna

#contar cuantos valores se repiten
print('Contar cuantos valores se repiten: ')
print(dataframe['pan'].value_counts())

#Obtener columnas
print('Obtener columnas: ')
print(dataframe.columns)

#Obtener indices
print('Obtener indices: ')
print(dataframe.index)

#Obtener filas
print('Obtener filas: ')
dataframe = pd.DataFrame(data, row, column)
dataframe['indice'] = [1, 2, 3, 4]
dataframe = dataframe.set_index('indice')
print(dataframe)

#Obtener por coluimna
print(dataframe.sort_values(['pan'])) #Ordenar por columna

#Describir dataframe
print('Describir dataframe: ')
print(dataframe.describe())

#Pasar dataframe a un archivo CSV
print('Pasar dataframe a un archivo CSV: ')
dataframe.to_csv('DataFrame.csv')
print(dataframe)

#Cargar archivo CSV
print('Cargar archivo CSV: ')
dataFrameRead = pd.read_csv('DataFrame.csv')
print(dataFrameRead)
