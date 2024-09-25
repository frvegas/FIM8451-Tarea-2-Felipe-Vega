Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import matplotlib.pyplot as plt

# Inicialización de la red y energía total
def initialize_lattice(L):
    spins = 2 * np.random.randint(2, size=(L, L)) - 1
    E = 0
    for i in range(L):
        for j in range(L):
            S = spins[i, j]
            neighbors = spins[(i+1)%L, j] + spins[i, (j+1)%L] + spins[(i-1)%L, j] + spins[i, (j-1)%L]
            E += -S * neighbors
    E /= 2
    return spins, E

# Implementación del procedimiento Markov-Ising
def markov_ising(spins, E, L, T):
    i, j = np.random.randint(0, L, 2)
    h = spins[(i+1)%L, j] + spins[i, (j+1)%L] + spins[(i-1)%L, j] + spins[i, (j-1)%L]
    delta_E = 2 * spins[i, j] * h
    
    if delta_E <= 0 or np.random.rand() < np.exp(-delta_E / T):
        spins[i, j] *= -1
        E += delta_E
    
    return spins, E

# Función para calcular la magnetización absoluta
... def calculate_magnetization(spins):
...     return np.abs(np.sum(spins))
... 
... # Parámetros de simulación
... lattice_sizes = [2,3,4,5,6,7,8]  # Tamaños de las redes
... steps = 100000  # Número de pasos de Monte Carlo
... temperatures = np.linspace(1,5,100)  # Rango de temperaturas
... 
... # Configuración del gráfico
... plt.figure(figsize=(10, 6))
... 
... # Simulación para cada tamaño de red
... for L in lattice_sizes:
...     magnetizations = []
...     
...     for T in temperatures:
...         spins, E = initialize_lattice(L)
...         mag_avg = 0
...         
...         # Realizar simulación de Monte Carlo
...         for step in range(steps):
...             spins, E = markov_ising(spins, E, L, T)
...             if step >= steps // 2:
...                 mag_avg += calculate_magnetization(spins)
...         
...         # Promedio de magnetización absoluta
...         mag_avg /= (steps // 2) * (L * L)
...         magnetizations.append(mag_avg)
...     
...     # Graficar para cada tamaño de red
...     plt.plot(temperatures, magnetizations, marker='o', linestyle='-', label=f'{L}x{L}')
... 
... # Configuración final del gráfico
... plt.xlabel('Temperature (T)')
... plt.ylabel('Absolute magnetization |<m>|')
... plt.title('Absolute Magnetization vs Temperature for different lattice sizes')
... plt.legend(title='Red size')
... plt.grid(True)
