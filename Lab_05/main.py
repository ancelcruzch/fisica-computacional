import sys

def calcular_energia_mecanica(masa, velocidad, altura):
    g = 9.81  # Aceleración gravitacional (m/s^2)
    energia_cinetica = 0.5 * masa * velocidad ** 2
    energia_potencial = masa * g * altura
    energia_mecanica = energia_cinetica + energia_potencial
    return energia_cinetica, energia_potencial, energia_mecanica

def solicitar_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Error: El valor debe ser positivo.")
            else:
                return valor
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

def menu():
    print("\n--- Conservación de la Energía Mecánica ---")
    print("1. Calcular energía mecánica")
    print("2. Salir")
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion in [1, 2]:
                return opcion
            else:
                print("Error: Seleccione una opción válida (1 o 2).")
        except ValueError:
            print("Error: Por favor, ingrese un número entero.")

def main():
    while True:
        opcion = menu()

        if opcion == 1:
            print("\n--- Ingreso de datos ---")
            masa = solicitar_float("Ingrese la masa del objeto (kg): ")
            velocidad = solicitar_float("Ingrese la velocidad del objeto (m/s): ")
            altura = solicitar_float("Ingrese la altura del objeto (m): ")

            # Cálculo de las energías
            energia_cinetica, energia_potencial, energia_mecanica = calcular_energia_mecanica(masa, velocidad, altura)

            # Resultados
            print("\n--- Resultados ---")
            print(f"Energía Cinética (E_K): {energia_cinetica:.2f} J")
            print(f"Energía Potencial (E_P): {energia_potencial:.2f} J")
            print(f"Energía Mecánica Total (E_m): {energia_mecanica:.2f} J")

        elif opcion == 2:
            print("Saliendo del programa...")
            sys.exit()

if __name__ == "__main__":
    main()
