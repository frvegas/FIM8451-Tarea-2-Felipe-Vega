Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... import matplotlib.pyplot as plt
... from collections import defaultdict
... 
... def gray_flip(spins):
...     N = len(spins) - 1
...     k = spins[0]
...     
...     if k > N:
...         return None, spins
...     
...     spins[k - 1] = spins[k]
...     spins[k] = k + 1
...     
...     if k != 1:
...         spins[0] = 1
...         
...     return k, spins
... 
... def enumerate_ising(L, periodic_boundary=True):
...     N = L * L
...     spins = [i + 1 for i in range(N + 1)]
...     spins[0] = 0
...     sigma = [-1] * N
...     
...     E = -2 * N
...     M = -N
...     density_of_states = defaultdict(int)
...     density_of_states[(E, M)] += 1
...     
...     for i in range(1, 2**(N-1)):
...         k, spins = gray_flip(spins)
...         if k is None:
...             break
...         
...         # Calcular el campo en el sitio k
...         h = 0
        for neighbor in get_neighbors(k-1, L, periodic_boundary):
            h += sigma[neighbor]
        
        E += 2 * sigma[k-1] * h
        M += 2 * sigma[k-1]
        density_of_states[(E, M)] += 1
        sigma[k-1] *= -1
    
    return density_of_states

def get_neighbors(index, L, periodic_boundary):
    row, col = divmod(index, L)
    neighbors = []
    
    if row > 0:
        neighbors.append((row - 1) * L + col)
    elif periodic_boundary:
        neighbors.append((L - 1) * L + col)
    
    if row < L - 1:
        neighbors.append((row + 1) * L + col)
    elif periodic_boundary:
        neighbors.append(col)
    
    if col > 0:
        neighbors.append(row * L + col - 1)
    elif periodic_boundary:
        neighbors.append(row * L + (L - 1))
    
    if col < L - 1:
        neighbors.append(row * L + col + 1)
    elif periodic_boundary:
        neighbors.append(row * L)
    
    return neighbors

def calculate_probability(density_of_states, L, T):
    N = L * L
    Z = 0  # Partición de función
    prob = defaultdict(float)
    
    for (E, M), count in density_of_states.items():
        weight = count * np.exp(-E / T)
        prob[M / N] += weight
        Z += weight
    
    for m in prob:
        prob[m] /= Z  # Normalización
    
    return prob

def binder_cumulant(prob):
    m2 = sum(m**2 * p for m, p in prob.items())
    m4 = sum(m**4 * p for m, p in prob.items())
    return 1 - (m4 / (3 * m2**2))

# Ejemplo de uso para L=2,4 y T en un rango
L_values = [2, 4, 6]
T_values = np.linspace(1.0, 4.0, 50)

binder_results = {}

for L in L_values:
    binder_values = []
    for T in T_values:
        dos = enumerate_ising(L, periodic_boundary=True)
        prob = calculate_probability(dos, L, T)
        B_T = binder_cumulant(prob)
        binder_values.append(B_T)
    
    binder_results[L] = binder_values

# Graficar los resultados
plt.figure(figsize=(10, 6))
for L, binder_values in binder_results.items():
    plt.plot(T_values, binder_values, label=f'L={L}')

plt.axvline(2/np.log(1+np.sqrt(2)), color='red', linestyle='--', label=r'$T_c$')
plt.xlabel('T')
plt.ylabel('Binder cumulant B(T)')
plt.title('Binder Cumulant vs Temperature for 2x2, 4x4 and 6x6 Ising Models')
plt.legend()
plt.grid(True)
