def calculate_value():
    print("Este programa puede calcular uno de los siguientes valores:")
    print("1. Desplazamiento (Delta x)")
    print("2. Velocidad inicial (Vi)")
    print("3. Aceleración (alpha)")
    print("4. Tiempo (Delta t)")
    option = input("¿Qué valor deseas calcular? (1 para Delta x, 2 para Vi, 3 para alpha, 4 para Delta t): ")

    try:
        if option == '1':  # Calcular desplazamiento
            Vi = float(input("Introduce el valor de la velocidad inicial (Vi) en m/s: "))
            alpha = float(input("Introduce el valor de la aceleración (alpha) en m/s^2: "))
            delta_t = float(input("Introduce el valor del tiempo (Delta t) en segundos: "))

            if delta_t <= 0:
                print("Error: El tiempo debe ser mayor que cero.")
                return

            delta_x = Vi * delta_t + (alpha * delta_t ** 2) / 2
            print(f"El valor del desplazamiento (Delta x) es: {delta_x} metros")

        elif option == '2':  # Calcular velocidad inicial
            delta_x = float(input("Introduce el valor del desplazamiento (Delta x) en metros: "))
            alpha = float(input("Introduce el valor de la aceleración (alpha) en m/s^2: "))
            delta_t = float(input("Introduce el valor del tiempo (Delta t) en segundos: "))

            if delta_t <= 0:
                print("Error: El tiempo debe ser mayor que cero.")
                return

            Vi = (delta_x - (alpha * delta_t ** 2) / 2) / delta_t
            print(f"El valor de la velocidad inicial (Vi) es: {Vi} m/s")

        elif option == '3':  # Calcular aceleración
            delta_x = float(input("Introduce el valor del desplazamiento (Delta x) en metros: "))
            Vi = float(input("Introduce el valor de la velocidad inicial (Vi) en m/s: "))
            delta_t = float(input("Introduce el valor del tiempo (Delta t) en segundos: "))

            if delta_t <= 0:
                print("Error: El tiempo debe ser mayor que cero.")
                return

            alpha = 2 * (delta_x - Vi * delta_t) / (delta_t ** 2)
            print(f"El valor de la aceleración (alpha) es: {alpha} m/s^2")

        elif option == '4':  # Calcular tiempo
            delta_x = float(input("Introduce el valor del desplazamiento (Delta x) en metros: "))
            Vi = float(input("Introduce el valor de la velocidad inicial (Vi) en m/s: "))
            alpha = float(input("Introduce el valor de la aceleración (alpha) en m/s^2: "))

            if alpha == 0:
                print("Error: La aceleración no puede ser cero para calcular el tiempo.")
                return

            discriminant = Vi**2 - 2 * alpha * (-delta_x)
            if discriminant < 0:
                print("Error: No existen soluciones reales para el valor de tiempo con los datos proporcionados.")
                return

            delta_t_1 = (-Vi + discriminant**0.5) / alpha
            delta_t_2 = (-Vi - discriminant**0.5) / alpha

            # Mostrar las soluciones de tiempo
            print(f"Las posibles soluciones para Delta t son: {delta_t_1} segundos y {delta_t_2} segundos")
            if delta_t_1 > 0:
                print(f"La solución válida para Delta t es: {delta_t_1} segundos")
            elif delta_t_2 > 0:
                print(f"La solución válida para Delta t es: {delta_t_2} segundos")
            else:
                print("Error: No hay soluciones positivas para el tiempo.")

        else:
            print("Opción no válida. Por favor elige entre 1, 2, 3 o 4.")

    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos.")
    except ZeroDivisionError:
        print("Error: El tiempo o la aceleración no pueden ser cero.")

# Ejecutar la función
calculate_value()
