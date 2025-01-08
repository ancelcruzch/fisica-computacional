import numpy as np
from scipy.integrate import quad

# Función para validar que el valor ingresado sea un número positivo (evitando valores negativos o no numéricos)
def validar_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                raise ValueError("El valor debe ser positivo.")
            return valor
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")

# Función para la fuerza variable (en este caso, fuerza de un resorte F(x) = -k * x)
def fuerza_variable(x, k):
    return -k * x

# Solicitar al usuario la constante k del resorte (validación incluida)
print("Cálculo del trabajo realizado por una fuerza variable (F(x) = -k * x)")
k = validar_numero_positivo("Ingresa el valor de la constante del resorte k (N/m): ")

# Solicitar los límites de integración (validación incluida)
while True:
    try:
        x_inicial = float(input("Ingresa el valor del límite inferior de desplazamiento (x_inicial): "))
        x_final = float(input("Ingresa el valor del límite superior de desplazamiento (x_final): "))
        if x_final <= x_inicial:
            raise ValueError("El límite superior debe ser mayor que el límite inferior.")
        break
    except ValueError as e:
        print(f"Error: {e}. Inténtalo de nuevo.")

# Calcular el trabajo usando integración numérica
trabajo, error = quad(fuerza_variable, x_inicial, x_final, args=(k,))

# Mostrar el resultado del trabajo realizado
print(f"\nEl trabajo realizado por la fuerza variable es: {trabajo:.2f} J")
