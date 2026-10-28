import numpy as np
import matplotlib.pyplot as plt
from qutip import basis, Qobj, mesolve

# --- 1. Parametros ---
t_max = 50
n_t_steps = 200
tlist = np.linspace(0, t_max, n_t_steps)
N_pos = 201
center = 100
pos_dims = [N_pos]

# --- 2. Hamiltoniano ---
# Matriz de Adyacencia
A_matrix = np.diag(np.ones(N_pos - 1), 1) + np.diag(np.ones(N_pos - 1), -1)
gamma = 0.45  # Parametro de salto ajustado analiticamente
H = gamma * Qobj(A_matrix, dims=[pos_dims, pos_dims])

# --- 3. Estado Inicial y Medicion ---
psi0 = basis(N_pos, center)  # Inicia en |0>

# Proyector para medir la probabilidad en z=10
pos_z10 = center + 10
proj_z10 = basis(N_pos, pos_z10) * basis(N_pos, pos_z10).dag()

# --- 4. Evolucion Temporal ---
# Solucion de la Ecuacion de Schrodinger
result = mesolve(H, psi0, tlist, c_ops=[], e_ops=[proj_z10])

# --- 5. Grafica ---
prob_z10 = result.expect[0]
plt.plot(tlist, prob_z10, color='blue')
plt.show()
