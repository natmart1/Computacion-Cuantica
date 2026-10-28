import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb  # Para el coeficiente binomial (nCk)

# Parametros de la simulacion
n = 100  # Numero de pasos
z_values = np.arange(-n, n + 1, 2)  # Solo posiciones pares

def get_classical_distribution(n, z_array, p):
    """
    Calcula la distribucion de probabilidad clasica usando la Ecuacion 2.
    """
    probabilities = []
    for z in z_array:
        # k = (n + z)/2 es el numero de pasos a la derecha
        k = (n + z) / 2

        # n - k = (n - z)/2 es el numero de pasos a la izquierda
        n_minus_k = (n - z) / 2

        # Asegurarse de que k es un entero y esta en el rango [0, n]
        if k < 0 or k > n or k != int(k):
            probabilities.append(0)
        else:
            # Esta es la Ecuacion 2
            prob = comb(n, k) * (p ** k) * ((1 - p) ** n_minus_k)
            probabilities.append(prob)

    return np.array(probabilities)

# --- Calcular las 3 distribuciones ---
# p=0.5 (justa, gris en el original)
prob_050 = get_classical_distribution(n, z_values, 0.5)

# p=0.15 (sesgada a la izquierda, oliva en el original)
prob_015 = get_classical_distribution(n, z_values, 0.15)

# p=0.85 (sesgada a la derecha, morada en el original)
prob_085 = get_classical_distribution(n, z_values, 0.85)

# --- Graficar los resultados ---
plt.figure(figsize=(10, 5))
ax = plt.gca()

# Ancho de las barras (es un histograma)
bar_width = 2  # Ancho de 2 para que las barras se toquen

# Usamos los colores mencionados en el articulo
ax.bar(z_values, prob_015, width=bar_width, color='#808000', label='p = 0.15')
ax.bar(z_values, prob_050, width=bar_width, color='#696969', label='p = 0.50')
ax.bar(z_values, prob_085, width=bar_width, color='#800080', label='p = 0.85')

# --- Estilo para que coincida con la Figura 1 ---
ax.set_title(f'Recreacion de la Figura 1: Caminata Aleatoria Clasica (n={n})')
ax.set_xlabel('z (Posicion final)', fontsize=12)
ax.set_ylabel('Pr(z$_n$ = z)', fontsize=12)
ax.set_xlim(-100, 100)
ax.set_ylim(0, 0.12)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar la grafica
plt.show()
