# =====================================================
# Implementación del Método de Bisección en Python
# Ejercicio 3: Función Trigonométrica
# Autor: Neo Cordova
# =====================================================

import numpy as np
import matplotlib.pyplot as plt

# Definir la función trigonométrica a evaluar
def f(x):
    return np.cos(x) - x  # Función f(x) = cos(x) - x

# Algoritmo del método de bisección
def biseccion(a, b, tol=1e-5, max_iter=100):
    """ Encuentra la raíz de una función mediante el método de bisección. """
    if f(a) * f(b) >= 0:
        raise ValueError("El método de bisección no es aplicable en el intervalo dado.")

    iteraciones, errores_abs = [], []
    c_old = a  # Variable para calcular el error absoluto

    for _ in range(max_iter):
        c = (a + b) / 2  # Punto medio del intervalo
        iteraciones.append(c)
        error = abs(c - c_old)  # Cálculo del error absoluto
        errores_abs.append(error)

        # Condición de parada
        if abs(f(c)) < tol or error < tol:
            break

        # Determinar el nuevo intervalo
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c_old = c  # Actualizar el valor de c_old

    return iteraciones, errores_abs

# Parámetros iniciales
a, b = 0, 1  # Intervalo donde se encuentra la raíz

# Ejecutar el método de bisección
iteraciones, errores = biseccion(a, b)

# Graficar la convergencia
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(errores) + 1), errores, marker='o', linestyle='-', color='g')
plt.yscale("log")
plt.xlabel("Iteración")
plt.ylabel("Error Absoluto")
plt.title("Convergencia del Método de Bisección (Función Trigonométrica)")
plt.grid()
plt.show()
