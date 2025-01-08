import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect, newton

# Funciones dadas en el problema
def f1(x):
    return np.log(x - 2)

def f2(x):
    return np.exp(-x)

def f3(x):
    return np.exp(x) - x

def f4(x):
    return 10 * np.exp(x / 2) * np.cos(2 * x)

def f5(x):
    return x**2 - 2

def f6(x):
    return np.sqrt(x - 2) - 1  # Ajustamos para igualar a 0

def f8(x):
    return 2 / x - 1  # Ajustamos para igualar a 0

# Gráfico para explorar funciones
def plot_function(func, x_range, title):
    x_vals = np.linspace(x_range[0], x_range[1], 1000)
    y_vals = [func(x) for x in x_vals]

    plt.plot(x_vals, y_vals, label=title)
    plt.axhline(0, color="black", linestyle="--")  # Línea y=0
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()

# Soluciones usando métodos
print("Solución para cada ecuación:")

# 1. Método Newton-Raphson para f1
try:
    root1 = newton(lambda x: np.log(x - 2), x0=3)
    print(f"1. Solución Newton-Raphson para y = ln(x-2): x = {root1:.6f}")
except Exception as e:
    print(f"1. Error: {e}")

# 2. Método Newton-Raphson para f2
try:
    root2 = newton(lambda x: np.exp(-x) - 0, x0=0.5)
    print(f"2. Solución Newton-Raphson para y = e^(-x): x = {root2:.6f}")
except Exception as e:
    print(f"2. Error: {e}")

# 3. Método Newton-Raphson para f3
try:
    root3 = newton(lambda x: np.exp(x) - x, x0=0.5)
    print(f"3. Solución Newton-Raphson para y = e^x - x: x = {root3:.6f}")
except Exception as e:
    print(f"3. Error: {e}")

# 4. Método de Bisección para f4 (con gráfica para encontrar intervalo)
print("\nGráfico para y = 10e^(x/2)cos(2x) entre [0, 5]:")
plot_function(f4, [0, 5], "y = 10e^(x/2)cos(2x)")

try:
    root4 = bisect(f4, 1.5, 2.5)  # Intervalo corregido tras graficar
    print(f"4. Solución Bisección para y = 10e^(x/2)cos(2x): x = {root4:.6f}")
except Exception as e:
    print(f"4. Error: {e}")

# 5. Método de Bisección para f5
try:
    root5 = bisect(f5, 0, 3)
    print(f"5. Solución Bisección para y = x^2 - 2: x = {root5:.6f}")
except Exception as e:
    print(f"5. Error: {e}")

# 6. Método Newton-Raphson para f6 (ajustada)
try:
    root6 = newton(lambda x: np.sqrt(x - 2) - 1, x0=3)
    print(f"6. Solución Newton-Raphson para y = sqrt(x-2): x = {root6:.6f}")
except Exception as e:
    print(f"6. Error: {e}")

# 8. Método de Bisección para f8 (ajustada)
try:
    root8 = bisect(f8, 1, 3)
    print(f"8. Solución Bisección para y = 2/x: x = {root8:.6f}")
except Exception as e:
    print(f"8. Error: {e}")
