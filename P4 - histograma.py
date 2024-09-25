Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import matplotlib.pyplot as plt

# Wolff step algorithm for a single cluster flip
def wolff_step(spins, L, T):
    """
    Realiza un paso del algoritmo de Wolff para el modelo de Ising.
    
    spins: array bidimensional de las espines.
    L: tamaño de la red.
    T: temperatura.
    
    Devuelve la nueva configuración de espines.
    """
    # Probabilidad de añadir un spin al cluster
    beta = 1 / T
    p_add = 1 - np.exp(-2 * beta)
    
    # Elegir un spin aleatoriamente
    i, j = np.random.randint(0, L, size=2)
    cluster = [(i, j)]
    old_spin = spins[i, j]
    new_spin = -old_spin
    spins[i, j] = new_spin
    to_check = [(i, j)]

    # Crear el cluster
    while to_check:
        x, y = to_check.pop()
        neighbors = [(x, (y+1) % L), (x, (y-1) % L), ((x+1) % L, y), ((x-1) % L, y)]
        for nx, ny in neighbors:
            if spins[nx, ny] == old_spin and np.random.rand() < p_add:
                spins[nx, ny] = new_spin
                cluster.append((nx, ny))
                to_check.append((nx, ny))
    
    return spins, cluster

# Magnetization calculation
def magnetization(spins):
    """
    Calcula la magnetización total de una configuración de espines.
    """
    return np.sum(spins)

# Binder cumulant calculation
def binder_cumulant(magnetizations):
    """
    Calcula el cumulante de Binder a partir de una lista de magnetizaciones.
    """
    m2 = np.mean(np.square(magnetizations))
    m4 = np.mean(np.power(magnetizations, 4))
    return 1 - (m4 / (3 * m2**2))

# Simulation parameters
L_values = [6, 16, 32, 64]  # Tamaños de las redes
temperatures = np.linspace(1.0, 3.5, 20)  # Intervalo de temperatura
n_steps = 10000  # Número de pasos de Monte Carlo
n_equilibration = 1000  # Pasos de equilibración

# Arrays para almacenar los resultados
magnetizations_all = {L: [] for L in L_values}
binder_cumulants = {L: [] for L in L_values}
... 
... # Monte Carlo Simulation using Wolff Algorithm
... for L in L_values:
...     spins = np.ones((L, L), dtype=int)  # Configuración inicial de espines
... 
...     for T in temperatures:
...         # Equilibración
...         for _ in range(n_equilibration):
...             spins, _ = wolff_step(spins, L, T)
... 
...         magnetizations = []
...         # Medición de observables
...         for _ in range(n_steps):
...             spins, _ = wolff_step(spins, L, T)
...             mag = magnetization(spins)
...             magnetizations.append(mag)
... 
...         # Almacenar magnetización media y Binder cumulant
...         magnetizations_all[L].append(np.mean(magnetizations) / (L**2))
...         binder_cumulants[L].append(binder_cumulant(magnetizations))
... 
... # Plotting magnetization histograms
... for L in L_values:
...     plt.hist(magnetizations_all[L], bins=50, alpha=0.6, label=f'L={L}')
... plt.title('Histograms of Magnetization for Different Lattice Sizes')
... plt.xlabel('Magnetization')
... plt.ylabel('Frequency')
... plt.legend()
... plt.show()
... 
... # Plotting Binder cumulant as a function of temperature
... plt.figure()
... for L in L_values:
...     plt.plot(temperatures, binder_cumulants[L], label=f'L={L}')
... plt.title('Binder Cumulant vs Temperature')
... plt.xlabel('Temperature')
... plt.ylabel('Binder Cumulant')
... plt.legend()
... plt.show()
