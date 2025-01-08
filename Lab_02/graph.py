import matplotlib.pyplot as plt

# Solicitar los valores al usuario
m = float(input("Ingrese la masa del móvil (kg): "))
vi = float(input("Ingrese la velocidad inicial (m/s): "))
vf = float(input("Ingrese la velocidad final (m/s): "))
t = float(input("Ingrese el tiempo que tarda en realizar el cambio (s): "))

# Calcular la aceleración
a = (vf - vi) / t

# Calcular la fuerza
F = m * a

print(f"La fuerza ejercida sobre el móvil es: {F:.2f} N")

# Graficar el proceso
tiempos = [0, t]
velocidades = [vi, vf]

plt.plot(tiempos, velocidades, marker='o')
plt.title('Cambio de velocidad del móvil')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)
plt.show()
