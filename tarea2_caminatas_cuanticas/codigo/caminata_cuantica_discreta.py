import numpy as np
import matplotlib.pyplot as plt
from qutip import tensor, basis, qeye, Qobj

# --- 1. Parametros ---
n_steps = 100
N_pos = 2 * n_steps + 1
center = n_steps

# Dimensiones
coin_dims = [2]
pos_dims = [N_pos]

# --- 2. Operadores ---
# Moneda Hadamard
H_matrix = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
C_H = Qobj(H_matrix, dims=[coin_dims, coin_dims])
C_op = tensor(C_H, qeye(N_pos))

# Operador de Desplazamiento (S)
proj_up = tensor(basis(2, 0) * basis(2, 0).dag(), qeye(N_pos))
proj_down = tensor(basis(2, 1) * basis(2, 1).dag(), qeye(N_pos))

shift_right = Qobj(np.diag(np.ones(N_pos - 1), 1), dims=[pos_dims, pos_dims])
shift_left = Qobj(np.diag(np.ones(N_pos - 1), -1), dims=[pos_dims, pos_dims])

S_op = tensor(qeye(2), shift_right) * proj_up + \
       tensor(qeye(2), shift_left) * proj_down

# Operador de evolucion U = S * C
U = S_op * C_op

# --- 3. Estado Inicial (Asimetrico) ---
# |psi_0> = |arriba> tensor |0>
psi_0 = tensor(basis(2, 0), basis(N_pos, center))

# Figura 4 (simetrica): descomentar estas lineas para usar la moneda |+y>
# coin_state_y = (basis(2, 0) + 1j * basis(2, 1)).unit()
# psi_0 = tensor(coin_state_y, basis(N_pos, center))

# --- 4. Evolucion ---
psi_n = (U ** n_steps) * psi_0

# --- 5. Probabilidades ---
final_state_vec = psi_n.full().flatten()
prob_up = np.abs(final_state_vec[0:N_pos]) ** 2
prob_down = np.abs(final_state_vec[N_pos:2 * N_pos]) ** 2
total_prob = prob_up + prob_down

# Grafica (paridad par)
z_axis = np.arange(-n_steps, n_steps + 1)
plt.bar(z_axis[::2], total_prob[::2], width=2, color='purple')
plt.show()
