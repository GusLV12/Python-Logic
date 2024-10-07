import numpy as np

arr = np.array([1, 2, 3, 4, 5])
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arrList = np.array(list)
print(f"Arr: {arr}")
print(f"List: {arrList}")

# Create an array with a range of numbers
arrPar = np.arange(2,11,2)
print(arrPar)

# Matriz de ceros
matrizCeros = np.zeros((3,3))
print(matrizCeros)

# Matriz de 40 elementos
matrizForty = np.linspace(1, 40, 40)
print(matrizForty)

#Matriz de 3x3
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)

# Matriz de 3x3 con 1 en la diagonal (Identidad)
matrizIdentidad = np.eye(3)
print(matrizIdentidad)

# Matriz aleatoria
matrizRandom = np.random.rand(3,3)
print(matrizRandom)
# Matriz aleatoria de enteros
matrizrandomInt = np.random.randint(1, 100, 5)
print(matrizrandomInt)

## Tamaños de arrays
matrizSize = np.random.randint(1, 101, 30)
print(matrizSize)
matriz3x3 = matrizSize.reshape(3,10)
print(matriz3x3)