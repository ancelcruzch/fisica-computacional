import numpy as np
from scipy.optimize import minimize
from scipy.special import gamma, kv
import matplotlib.pyplot as plt

def mass_attenuation_coefficient(E, coeffs):
    """Calculates the mass attenuation coefficient as a polynomial function."""
    logE = np.log10(E)
    return 10 ** np.polyval(coeffs[::-1], logE)

def objective_function(params, d, T, coeffs, energies):
    """Objective function to minimize the difference between measured and modeled transmission curves."""
    a, b, v, r = params
    um = mass_attenuation_coefficient(energies, coeffs)
    um0 = mass_attenuation_coefficient(max(energies), coeffs)

    # Verificar que no haya divisiones por cero o valores inválidos
    if np.isclose(a, b, atol=1e-2):
        return np.inf

    try:
        T_model = r * (((a * b) / ((d + a) * (d + b))) ** v) * np.exp(-um0 * d)

        # Calcular la matriz de transmisión para todas las combinaciones de d y um
        T_matrix = np.exp(-np.outer(d, um))  # Matriz de forma (50, 100)
        T_model += (1 - r) * T_matrix.sum(axis=1)  # Suma a lo largo del eje de energías
    except FloatingPointError:
        return np.inf

    # Validar que no haya valores NaN o Inf en el modelo de transmisión
    if np.any(np.isnan(T_model)) or np.any(np.isinf(T_model)):
        return np.inf

    return np.linalg.norm(T - T_model)

def reconstruct_spectrum(d, T, energies, coeffs):
    """Reconstructs the energy spectrum using numerical optimization."""
    x0 = np.array([3.0, 4.0, 1.0, 0.5])  # Initial parameters: [a, b, v, r]
    bounds = [(1.0, 5.0), (1.5, 5.0), (0.5, 2.0), (0.0, 1.0)]  # Bounds for [a, b, v, r]

    result = minimize(
        objective_function,
        x0,
        args=(d, T, coeffs, energies),
        bounds=bounds,
        method='L-BFGS-B'
    )

    if result.success:
        a, b, v, r = result.x
        um = mass_attenuation_coefficient(energies, coeffs)
        um0 = mass_attenuation_coefficient(max(energies), coeffs)

        F_brem = (
            r * (np.sqrt(np.pi) * (a * b) ** 2 / gamma(v))
            * (((um - um0) / (a - b)) ** (v - 0.5))
            * np.exp(-0.5 * (a + b) * (um - um0))
            * kv(v - 0.5, 0.5 * (a - b) * (um - um0))
        )
        F_brem = np.nan_to_num(F_brem, nan=0.0, posinf=0.0, neginf=0.0)

        F = F_brem / np.max(F_brem)  # Normalize spectrum

        return energies, F
    else:
        raise RuntimeError("Optimization failed: " + result.message)

# Example usage
if __name__ == "__main__":
    energies = np.linspace(30, 150, 100)  # Energy range in keV
    coeffs = [-0.3, 0.1, -0.01, 0.005, -0.0001]  # Polynomial coefficients for mass attenuation
    measured_d = np.linspace(0.1, 5, 50)  # Thickness in g/cm^2
    measured_T = np.exp(-measured_d * 0.2)  # Simulated transmission curve

    try:
        E, F = reconstruct_spectrum(measured_d, measured_T, energies, coeffs)
        print("Reconstructed energies:", E)
        print("Reconstructed spectrum:", F)
    except RuntimeError as e:
        print(e)

    # Graficar el espectro reconstruido
    plt.figure(figsize=(10, 6))
    plt.plot(energies, F, label="Espectro reconstruido", color="blue")
    plt.xlabel("Energía (keV)")
    plt.ylabel("Intensidad (normalizada)")
    plt.title("Espectro de energía reconstruido")
    plt.legend()
    plt.grid(True)
    plt.show()
