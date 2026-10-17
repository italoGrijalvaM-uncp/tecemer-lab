import numpy as np
import time

# algunas funciones de numpy para crear arrays y matrices
a = np.array([1, 2, 3, 4, 5], dtype=np.int32)
ceros = np.zeros((5, 4))
rango = np.arange(0, 12, 3)
espaciado = np.linspace(0, 1, 20)

print("Array base:", a)
print("Matriz de ceros:\n", ceros)
print("Rango:", rango)
print("Espaciado:", espaciado)
# calculo del tiempo de ejecucion de operaciones con listas y arrays usando la libreria time
n = 1_000_000
lista = list(range(n))
array = np.arange(n)

inicio = time.time()
resultado_lista = [x + 10 for x in lista]
print("Tiempo con lista:", time.time() - inicio)
inicio = time.time()
resultado_array = array + 10
print("Tiempo con array:", time.time() - inicio)

# prueba de funciones estadisticas de la libreria numpy
temperaturas = np.array([12.5, 14.0, 11.8, 13.2, 15.1, 10.9, 12.7])

print("Promedio:", temperaturas.mean())
print("Desviación estándar:", temperaturas.std())
print("Mínima:", temperaturas.min())
print("Máxima:", temperaturas.max())
