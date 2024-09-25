Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import matplotlib.pyplot as plt

# Función para inicializar la red de spins (tamaño LxL)
def initialize_lattice(L):
    return np.random.choice([-1, 1], size=(L, L))

# Función para obtener los vecinos de un spin con condiciones de borde periódicas
def get_neighbors(i, j, L):
    neighbors = [
        ((i-1) % L, j),  # Arriba
        ((i+1) % L, j),  # Abajo
        (i, (j-1) % L),  # Izquierda
        (i, (j+1) % L)   # Derecha
    ]
    return neighbors

# Algoritmo Wolff (Cluster-Ising)
def cluster_ising(lattice, L, J, T):
    i, j = np.random.randint(0, L, size=2)
    cluster = [(i, j)]
    cluster_set = set(cluster)
    to_check = [(i, j)]
    spin_value = lattice[i, j]
    p_add = 1 - np.exp(-2 * J / T)
    
    while to_check:
        i, j = to_check.pop()
        for neighbor in get_neighbors(i, j, L):
            ni, nj = neighbor
            if (ni, nj) not in cluster_set and lattice[ni, nj] == spin_value:
                if np.random.rand() < p_add:
                    cluster.append((ni, nj))
                    to_check.append((ni, nj))
                    cluster_set.add((ni, nj))
    
    for (i, j) in cluster:
        lattice[i, j] *= -1
    
    return lattice

# Función para calcular la energía del sistema
def calculate_energy(lattice, L, J):
    energy = 0
    for i in range(L):
        for j in range(L):
            spin = lattice[i, j]
            neighbors = get_neighbors(i, j, L)
            for ni, nj in neighbors:
                energy -= J * spin * lattice[ni, nj]
    return energy / 2  # Evitar contar dos veces las interacciones

# Función para calcular la magnetización
def calculate_magnetization(lattice):
    return np.sum(lattice)

# Simulación de Monte Carlo
def monte_carlo_simulation(L, J, T, steps):
    lattice = initialize_lattice(L)
    energies = []
    magnetizations = []
    
    for step in range(steps):
        lattice = cluster_ising(lattice, L, J, T)
        energy = calculate_energy(lattice, L, J)
        magnetization = calculate_magnetization(lattice)
        
        energies.append(energy)
        magnetizations.append(abs(magnetization))  # Magnetización absoluta
    
    return np.array(energies), np.array(magnetizations)

# Parámetros
J = 1  # Constante de interacción
steps = 50000  # Número de pasos de Monte Carlo
red_sizes = [6, 16, 32]  # Diferentes tamaños de la red
temperaturas = np.linspace(1.5, 3.5, 50)  # Rango de temperaturas

# Inicializamos listas para almacenar resultados
results_energia = {}
results_calor = {}

... # Simulación para cada tamaño de red
... for L in red_sizes:
...     energias_promedio = []
...     calores_especificos = []
...     
...     for T in temperaturas:
...         energias, magnetizaciones = monte_carlo_simulation(L, J, T, steps)
...         energia_promedio = np.mean(energias)
...         calor_especifico = np.var(energias) / (T**2)
...         
...         energias_promedio.append(energia_promedio)
...         calores_especificos.append(calor_especifico)
...     
...     results_energia[L] = energias_promedio
...     results_calor[L] = calores_especificos
... 
... # Graficar energía promedio y calor específico para diferentes tamaños de red
... plt.figure(figsize=(12, 6))
... 
... # Gráfico de la energía promedio para cada tamaño de red
... plt.subplot(1, 2, 1)
... for L in red_sizes:
...     plt.plot(temperaturas, results_energia[L], 'o-', label=f'Red {L}x{L}')
... plt.xlabel('Temperatura (T)')
... plt.ylabel('Energía promedio')
... plt.title('Energía promedio vs Temperatura')
... plt.legend()
... 
... # Gráfico del calor específico para cada tamaño de red
... plt.subplot(1, 2, 2)
... for L in red_sizes:
...     plt.plot(temperaturas, results_calor[L], 's-', label=f'Red {L}x{L}')
... plt.xlabel('Temperatura (T)')
... plt.ylabel('Calor específico')
... plt.title('Calor específico vs Temperatura')
... plt.legend()
... 
... plt.tight_layout()
... plt.show()
