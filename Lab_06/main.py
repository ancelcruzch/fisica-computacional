import numpy as np
import sys

def solicitar_float(mensaje, min_val=None, max_val=None):
    while True:
        try:
            valor = float(input(mensaje))
            if min_val is not None and valor < min_val:
                print(f"Error: El valor debe ser mayor o igual a {min_val}.")
            elif max_val is not None and valor > max_val:
                print(f"Error: El valor debe ser menor o igual a {max_val}.")
            else:
                return valor
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

def solicitar_entero(mensaje, min_val=None, max_val=None):
    while True:
        try:
            valor = int(input(mensaje))
            if min_val is not None and valor < min_val:
                print(f"Error: El valor debe ser mayor o igual a {min_val}.")
            elif max_val is not None and valor > max_val:
                print(f"Error: El valor debe ser menor o igual a {max_val}.")
            else:
                return valor
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

def ecuacion_calor(u0, r, timesteps):
    n = len(u0)
    u = np.zeros((n, timesteps + 1))
    u[:, 0] = u0

    for j in range(timesteps):
        for i in range(1, n - 1):
            u[i, j+1] = (1 - 2 * r) * u[i, j] + r * (u[i + 1, j] + u[i - 1, j])
    return u

def ecuacion_onda(u0, u1, r, timesteps):
    n = len(u0)
    u = np.zeros((n, timesteps + 1))
    u[:, 0] = u0
    u[:, 1] = u1

    for j in range(1, timesteps):
        for i in range(1, n - 1):
            u[i, j+1] = 2 * (1 - r**2) * u[i, j] + r**2 * (u[i + 1, j] + u[i - 1, j]) - u[i, j-1]
    return u

def ejecutar_ecuacion_calor():
    n = solicitar_entero("Ingrese el número de puntos en la barra (mínimo 5): ", min_val=5)
    u0 = np.linspace(0, 100, n)
    r = solicitar_float("Ingrese el valor de r (debe ser <= 0.5 para estabilidad): ", max_val=0.5)
    timesteps = solicitar_entero("Ingrese el número de pasos de tiempo: ", min_val=1)

    resultado = ecuacion_calor(u0, r, timesteps)
    print("Resultado de la simulación para la ecuación de calor:")
    print(resultado)

def ejecutar_ecuacion_onda():
    n = solicitar_entero("Ingrese el número de puntos en la cuerda (mínimo 5): ", min_val=5)
    u0 = np.sin(np.linspace(0, np.pi, n))
    u1 = np.sin(np.linspace(0, np.pi, n)) * 0.9
    r = solicitar_float("Ingrese el valor de r para la ecuación de onda (debe ser <= 1.0 para estabilidad): ", max_val=1.0)
    timesteps = solicitar_entero("Ingrese el número de pasos de tiempo: ", min_val=1)

    resultado = ecuacion_onda(u0, u1, r, timesteps)
    print("Resultado de la simulación para la ecuación de onda:")
    print(resultado)

def menu():
    print("\n--- Simulación de Ecuaciones Diferenciales Parciales ---")
    print("1. Ecuación de Calor")
    print("2. Ecuación de Onda")
    print("3. Salir")
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("Error: Seleccione una opción válida (1, 2 o 3).")
        except ValueError:
            print("Error: Por favor, ingrese un número entero.")

def main():
    while True:
        opcion = menu()

        if opcion == 1:
            print("\n--- Ecuación de Calor ---")
            ejecutar_ecuacion_calor()

        elif opcion == 2:
            print("\n--- Ecuación de Onda ---")
            ejecutar_ecuacion_onda()

        elif opcion == 3:
            print("Saliendo del programa...")
            sys.exit()

if __name__ == "__main__":
    main()
