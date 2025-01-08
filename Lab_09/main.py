import numpy as np
import matplotlib.pyplot as plt

# Definir las reglas basadas en la tabla de selección
def regla(celda_izq, celda_actual, celda_der):
    if (celda_izq, celda_actual, celda_der) == (0, 0, 0):
        return 0
    elif (celda_izq, celda_actual, celda_der) == (0, 0, 1):
        return 1
    elif (celda_izq, celda_actual, celda_der) == (0, 1, 0):
        return 1
    elif (celda_izq, celda_actual, celda_der) == (0, 1, 1):
        return 1
    elif (celda_izq, celda_actual, celda_der) == (1, 0, 0):
        return 1
    elif (celda_izq, celda_actual, celda_der) == (1, 0, 1):
        return 0
    elif (celda_izq, celda_actual, celda_der) == (1, 1, 0):
        return 0
    elif (celda_izq, celda_actual, celda_der) == (1, 1, 1):
        return 0

# Configurar el autómata celular
def automata_celular(tamano, generaciones, estado_inicial):
    grid = np.zeros((generaciones, tamano), dtype=int)
    grid[0, :] = estado_inicial

    for t in range(1, generaciones):
        for i in range(tamano):
            # Obtener las celdas vecinas considerando condiciones de frontera periódicas
            celda_izq = grid[t - 1, (i - 1) % tamano]
            celda_actual = grid[t - 1, i]
            celda_der = grid[t - 1, (i + 1) % tamano]

            # Aplicar la regla
            grid[t, i] = regla(celda_izq, celda_actual, celda_der)

    return grid

# Parámetros del autómata
n_celdas = 31
generaciones = 15
estado_inicial = np.zeros(n_celdas, dtype=int)
estado_inicial[n_celdas // 2] = 1  # Inicializar con un 1 en el centro

# Ejecutar el autómata
resultado = automata_celular(n_celdas, generaciones, estado_inicial)

# Visualizar el autómata celular con estilo moderno
plt.figure(figsize=(12, 8))
plt.imshow(resultado, cmap="viridis", interpolation="bilinear")
plt.title("Autómata Celular", fontsize=16, fontweight="bold")
plt.xlabel("Celdas", fontsize=12)
plt.ylabel("Generaciones", fontsize=12)
plt.colorbar(label="Estado de la Celda")
plt.grid(visible=False)
plt.tight_layout()
plt.show()
