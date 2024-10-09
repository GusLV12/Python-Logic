import pandas as pd

# Leyendo un archivo csv
df_ventas = pd.read_csv('ventas.csv',sep=';')
#Imprimiendo el dataframe
print(df_ventas)

# Valores faltantes
df_ventas.fillna(0, inplace=True)
print("Valores faltantes: ")
print(df_ventas)

# Nueva columna cantidad * precio unitario
df_ventas['Ingresos'] = df_ventas['Cantidad'] * df_ventas['Precio_Unitario']
print("Ingresos: ")
print(df_ventas)

# Agregar los datos por tienda y producto. Calcular loa precios totales de cada tienda
ingresos_tienda = df_ventas.groupby(['Tienda', 'Producto'])['Ingresos'].sum().reset_index()
print("Ingresos por tienda: ")
print(ingresos_tienda)

# Encontrar el producto con mayores ingresos de cada tienda
producto_max_ingresos = ingresos_tienda.sort_values(['Tienda', 'Ingresos'], ascending=[True, False]).groupby('Tienda').first().reset_index()
print("Producto con mayores ingresos: ")
print(producto_max_ingresos)

# Resumen de la cantidad de productos vendidos a lo largo del mes y guardar en un archivo csv
resumen = df_ventas.groupby('Producto')['Cantidad'].sum().reset_index()
print("Resumen de la cantidad de productos vendidos: ")
print(resumen)
resumen.to_csv('Resumen_productos.csv', index=False)
