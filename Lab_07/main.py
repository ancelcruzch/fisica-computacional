import numpy as np

def monte_carlo_integration(func, a, b, n_points=100000):
    """
    Método Monte Carlo para calcular una integral definida.

    :param func: Función a integrar.
    :param a: Límite inferior de integración.
    :param b: Límite superior de integración.
    :param n_points: Número de puntos aleatorios a generar.
    :return: Aproximación de la integral.
    """
    if a > b:
        raise ValueError("El límite inferior no puede ser mayor que el superior.")

    # Generar puntos aleatorios uniformemente distribuidos en [a, b]
    x_random = np.random.uniform(a, b, n_points)
    y_values = func(x_random)

    # Validar que no existan valores no definidos
    if np.any(np.isnan(y_values)) or np.any(np.isinf(y_values)):
        raise ValueError("La función genera valores no definidos en el rango dado.")

    # Calcular el promedio de la función en los puntos aleatorios
    integral = (b - a) * np.mean(y_values)
    return integral


# Funciones dadas en los ejercicios
def f1(x):
    return np.exp(x**2)

def f2(x):
    return 4 * np.exp(x)

def f3(x):
    return np.sqrt(1 - np.exp(x**2))

def f4(x):
    return x / (1 + x**2)**2

def f5(x):
    return np.exp(x + x**2)

def f6(x):
    return np.exp(-x)

def f7(x):
    return (1 - x**2)**(3/2)


# Resolver cada integral
if __name__ == "__main__":
    try:
        # Ejercicio 1
        print("Ejercicio 1:", monte_carlo_integration(f1, 0, 1))

        # Ejercicio 2
        print("Ejercicio 2:", monte_carlo_integration(f2, -1, 1))

        # Ejercicio 3 (con restricción para evitar valores no definidos)
        print("Ejercicio 3:", monte_carlo_integration(f3, 0, 1))

        # Ejercicio 4 (intervalo infinito, cambiar a un rango muy grande)
        print("Ejercicio 4:", monte_carlo_integration(f4, 0, 100))

        # Ejercicio 5
        print("Ejercicio 5:", monte_carlo_integration(f5, 0, 1))

        # Ejercicio 6 (integral convergente en infinito)
        print("Ejercicio 6:", monte_carlo_integration(f6, 0, 100))

        # Ejercicio 7 (con restricción para valores válidos)
        print("Ejercicio 7:", monte_carlo_integration(f7, 0, 1))

    except ValueError as e:
        print("Error:", e)
