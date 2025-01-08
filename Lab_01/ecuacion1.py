def calculate_missing_value():
    print("Bienvenido. Esta fórmula calcula uno de los siguientes valores:")
    print("1. Delta x (desplazamiento)")
    print("2. v (velocidad)")
    print("3. Delta t (tiempo)")

    to_calculate = input("¿Cuál valor deseas calcular? (1 para Delta x, 2 para v, 3 para Delta t): ")

    if to_calculate == '1':
        try:
            v = float(input("Introduce el valor de la velocidad (v): "))
            delta_t = float(input("Introduce el valor del tiempo (Delta t): "))
            if delta_t <= 0:
                print("Error: El tiempo debe ser mayor que cero.")
                return
            delta_x = v * delta_t
            print(f"El valor de Delta x (desplazamiento) es: {delta_x}")
        except ValueError:
            print("Error: Por favor ingresa valores numéricos válidos.")

    elif to_calculate == '2':
        try:
            delta_x = float(input("Introduce el valor del desplazamiento (Delta x): "))
            delta_t = float(input("Introduce el valor del tiempo (Delta t): "))
            if delta_t <= 0:
                print("Error: El tiempo debe ser mayor que cero.")
                return
            v = delta_x / delta_t
            print(f"El valor de v (velocidad) es: {v}")
        except ValueError:
            print("Error: Por favor ingresa valores numéricos válidos.")
        except ZeroDivisionError:
            print("Error: El tiempo no puede ser cero.")

    elif to_calculate == '3':
        try:
            delta_x = float(input("Introduce el valor del desplazamiento (Delta x): "))
            v = float(input("Introduce el valor de la velocidad (v): "))
            if v <= 0:
                print("Error: La velocidad debe ser mayor que cero.")
                return
            delta_t = delta_x / v
            print(f"El valor de Delta t (tiempo) es: {delta_t}")
        except ValueError:
            print("Error: Por favor ingresa valores numéricos válidos.")
        except ZeroDivisionError:
            print("Error: La velocidad no puede ser cero.")
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")

calculate_missing_value()
