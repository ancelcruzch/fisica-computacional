import numpy as np
import matplotlib.pyplot as plt

# Constantes
GRAVEDAD = 9.81  # Aceleración debido a la gravedad (m/s^2)

class Vehicle:
    def __init__(self, mass, tire_friction, center_of_gravity_height, wheel_base):
        """Inicializar un vehículo con parámetros clave."""
        self.mass = mass  # Masa del vehículo en kg
        self.tire_friction = tire_friction  # Coeficiente de fricción
        self.center_of_gravity_height = center_of_gravity_height  # Altura del centro de gravedad en metros
        self.wheel_base = wheel_base  # Distancia entre los ejes delantero y trasero (metros)

    def centripetal_force(self, speed, radius):
        """Calcular la fuerza centrípeta necesaria para una velocidad y radio de curva dados."""
        speed_mps = speed / 3.6  # Convertir velocidad de km/h a m/s
        return self.mass * (speed_mps ** 2) / radius

    def max_safe_speed(self, radius):
        """Determinar la velocidad máxima segura para evitar derrapes, basada en la fricción."""
        max_speed_mps = np.sqrt(self.tire_friction * GRAVEDAD * radius)
        return max_speed_mps * 3.6  # Convertir de m/s a km/h

    def rollover_risk(self, speed, radius):
        """Calcular el riesgo de vuelco basado en la velocidad, radio y altura del centro de gravedad."""
        speed_mps = speed / 3.6  # Convertir velocidad de km/h a m/s
        lateral_acceleration = (speed_mps ** 2) / radius
        return lateral_acceleration * self.center_of_gravity_height / self.wheel_base

class Road:
    def __init__(self, radius, bank_angle=0):
        """Inicializar una curva de carretera con un radio y un ángulo de peralte opcional."""
        self.radius = radius
        self.bank_angle = np.radians(bank_angle)  # Convertir el ángulo a radianes

    def effective_friction(self, tire_friction):
        """Calcular la fricción efectiva considerando el ángulo de peralte."""
        return tire_friction + np.tan(self.bank_angle)

    def lateral_force(self, vehicle_mass, speed):
        """Calcular la fuerza lateral que actúa sobre el vehículo debido a la curva."""
        speed_mps = speed / 3.6  # Convertir velocidad de km/h a m/s
        return vehicle_mass * speed_mps ** 2 / self.radius

class Simulation:
    def __init__(self, vehicle, road):
        """Inicializar la simulación con un vehículo y una carretera."""
        self.vehicle = vehicle
        self.road = road

    def simulate(self, speeds):
        """Ejecutar la simulación para un rango de velocidades y devolver los resultados de estabilidad."""
        results = []
        for speed in speeds:
            lateral_force = self.road.lateral_force(self.vehicle.mass, speed)
            friction_limit = self.vehicle.tire_friction * self.vehicle.mass * GRAVEDAD
            rollover_index = self.vehicle.rollover_risk(speed, self.road.radius)
            results.append({
                "speed": speed,
                "lateral_force": lateral_force,
                "friction_limit": friction_limit,
                "stable": lateral_force <= friction_limit,
                "rollover_risk": rollover_index
            })
        return results

    def plot_results(self, results):
        """Graficar los resultados de estabilidad y riesgo de vuelco."""
        speeds = [result["speed"] for result in results]
        lateral_forces = [result["lateral_force"] for result in results]
        friction_limits = [result["friction_limit"] for result in results]
        rollover_risks = [result["rollover_risk"] for result in results]

        plt.figure(figsize=(12, 8))

        # Gráfico de fuerza lateral vs límite de fricción
        plt.subplot(2, 1, 1)
        plt.plot(speeds, lateral_forces, label="Fuerza Lateral", marker="o")
        plt.plot(speeds, friction_limits, label="Límite de Fricción", linestyle="--")
        plt.xlabel("Velocidad (km/h)")
        plt.ylabel("Fuerza (N)")
        plt.title("Estabilidad del Vehículo en una Curva")
        plt.legend()
        plt.grid()

        # Gráfico de riesgo de vuelco
        plt.subplot(2, 1, 2)
        plt.plot(speeds, rollover_risks, label="Índice de Riesgo de Vuelco", color="r", marker="x")
        plt.axhline(y=1, color="k", linestyle="--", label="Umbral de Vuelco")
        plt.xlabel("Velocidad (km/h)")
        plt.ylabel("Índice de Riesgo")
        plt.title("Riesgo de Vuelco del Vehículo")
        plt.legend()
        plt.grid()

        plt.tight_layout()
        plt.show()

# Prueba de la funcionalidad
if __name__ == "__main__":
    # Parámetros del vehículo
    mass = 1200  # kg
    tire_friction = 0.8  # Coeficiente de fricción
    center_of_gravity_height = 0.5  # metros
    wheel_base = 2.5  # metros

    # Parámetros de la carretera
    radius = 30  # Radio de la curva en metros
    bank_angle = 5  # Ángulo de peralte en grados

    # Inicializar objetos
    vehicle = Vehicle(mass, tire_friction, center_of_gravity_height, wheel_base)
    road = Road(radius, bank_angle)
    simulation = Simulation(vehicle, road)

    # Rango de velocidades para la simulación
    speeds = np.linspace(20, 180, 20)  # Velocidades de 20 a 110 km/h

    # Ejecutar la simulación
    results = simulation.simulate(speeds)

    # Imprimir y graficar resultados
    for result in results:
        print(f"Velocidad: {result['speed']:.2f} km/h, Fuerza Lateral: {result['lateral_force']:.2f} N, "
              f"Límite de Fricción: {result['friction_limit']:.2f} N, Estable: {result['stable']}, "
              f"Riesgo de Vuelco: {result['rollover_risk']:.2f}")

    simulation.plot_results(results)
