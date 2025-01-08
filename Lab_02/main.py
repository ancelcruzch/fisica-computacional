import math

# Constantes universales
G = 6.67430e-11  # Constante gravitacional (m^3 kg^-1 s^-2)
M = 1.989e30     # Masa del Sol (kg)

# Función para solicitar un valor positivo
def solicitar_valor_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("El valor debe ser un número positivo mayor que cero.")
            else:
                return valor
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Solicitar valores con restricciones
r = solicitar_valor_positivo("Ingrese la distancia entre el planeta y la estrella en metros (r): ")
a = solicitar_valor_positivo("Ingrese el semieje mayor de la órbita en metros (a): ")

# Solicitar excentricidad, que debe estar entre 0 y 1
while True:
    try:
        e = float(input("Ingrese la excentricidad de la órbita (debe estar entre 0 y 1): "))
        if 0 <= e < 1:
            break
        else:
            print("La excentricidad debe estar entre 0 y 1.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Función para calcular la velocidad orbital utilizando la ley de gravitación universal
def velocidad_orbital(G, M, r):
    return math.sqrt(G * M / r)

# Función para calcular la posición del planeta en la órbita (utilizando la fórmula de una elipse)
def posicion_orbital(a, e, theta):
    # Ecuación de una órbita elíptica en coordenadas polares
    r_orbita = (a * (1 - e**2)) / (1 + e * math.cos(theta))
    return r_orbita

# Cálculo de la velocidad orbital
velocidad = velocidad_orbital(G, M, r)
print(f"\nVelocidad orbital del planeta: {velocidad:.2f} m/s")

# Solicitar ángulo theta en grados, convertir a radianes y verificar que esté entre 0° y 360°
while True:
    try:
        theta = float(input("\nIngrese el ángulo theta (en grados, entre 0 y 360) para calcular la posición del planeta en la órbita: "))
        if 0 <= theta <= 360:
            theta_rad = math.radians(theta)  # Convertir a radianes
            break
        else:
            print("El ángulo debe estar entre 0° y 360°.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Cálculo de la órbita (distancia desde el centro)
posicion = posicion_orbital(a, e, theta_rad)
print(f"\nLa distancia del planeta a la estrella en esa posición de la órbita es: {posicion:.2f} metros")
