def calcular_fuerza():
    try:
        masa = float(input("Ingrese la masa (en kg): "))
        aceleracion = float(input("Ingrese la aceleración (en m/s²): "))
        fuerza = masa * aceleracion
        print(f"La fuerza calculada es {fuerza} N")
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos.")

def calcular_masa():
    try:
        fuerza = float(input("Ingrese la fuerza (en N): "))
        aceleracion = float(input("Ingrese la aceleración (en m/s²): "))
        if aceleracion == 0:
            print("Error: La aceleración no puede ser cero.")
        else:
            masa = fuerza / aceleracion
            print(f"La masa calculada es {masa} kg")
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos.")

def calcular_aceleracion():
    try:
        fuerza = float(input("Ingrese la fuerza (en N): "))
        masa = float(input("Ingrese la masa (en kg): "))
        if masa == 0:
            print("Error: La masa no puede ser cero.")
        else:
            aceleracion = fuerza / masa
            print(f"La aceleración calculada es {aceleracion} m/s²")
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos.")

def mostrar_menu():
    print("\nMenú - Segunda Ley de Newton")
    print("1. Calcular Fuerza (F = m * a)")
    print("2. Calcular Masa (m = F / a)")
    print("3. Calcular Aceleración (a = F / m)")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            calcular_fuerza()
        elif opcion == '2':
            calcular_masa()
        elif opcion == '3':
            calcular_aceleracion()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
