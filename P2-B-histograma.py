Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import matplotlib.pyplot as plt

# Definición del algoritmo gray-flip
def gray_flip(spins):
    N = len(spins) - 1
    k = spins[0]
    
    if k > N:
        return None, spins
    
    spins[k - 1] = spins[k]
    spins[k] = k + 1
    
    if k != 1:
        spins[0] = 1
        
    return k, spins

# Enumerate-ising algorithm
def enumerate_ising(L, periodic_boundary=True):
    N = L * L
    spins = [i + 1 for i in range(N + 1)]
    spins[0] = 0
    sigma = [-1] * N
    
    E = -2 * N
    M = np.sum(sigma)
    
    energies = []
    magnetizations = []
    
    for i in range(1, 2**(N-1)):
        k, spins = gray_flip(spins)
        if k is None:
            break
        
        # Calcular el campo en el sitio k
        h = 0
        for neighbor in get_neighbors(k-1, L, periodic_boundary):
            h += sigma[neighbor]
        
        E += 2 * sigma[k-1] * h
        M += 2 * sigma[k-1]
        
        energies.append(E)
        magnetizations.append(M)
        
        sigma[k-1] *= -1
    
    return energies, magnetizations

# Función auxiliar para obtener los vecinos de un sitio en la red
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
...     
...     if col > 0:
...         neighbors.append(row * L + col - 1)
...     elif periodic_boundary:
...         neighbors.append(row * L + (L - 1))
...     
...     if col < L - 1:
...         neighbors.append(row * L + col + 1)
...     elif periodic_boundary:
...         neighbors.append(row * L)
...     
...     return neighbors
... 
... # Graficar los histogramas de energía y magnetización
... def plot_histograms(energies, magnetizations, L):
...     plt.figure(figsize=(12, 6))
...     
...     # Histograma de energías
...     plt.subplot(1, 2, 1)
...     plt.hist(energies, bins=20, color='b', alpha=0.7)
...     plt.xlabel('Energía (E)')
...     plt.ylabel('Frecuencia')
...     plt.title(f'Histograma de Energía - Red {L}x{L}')
...     
...     # Histograma de magnetizaciones
...     plt.subplot(1, 2, 2)
...     plt.hist(magnetizations, bins=20, color='r', alpha=0.7)
...     plt.xlabel('Magnetización (M)')
...     plt.ylabel('Frecuencia')
...     plt.title(f'Histograma de Magnetización - Red {L}x{L}')
...     
...     plt.tight_layout()
...     plt.show()
... 
... # Ejemplo de uso para redes 2x2, 4x4, 6x6 y 8x8
... for L in [2, 4, 6, 8]:
...     print(f"Generando histogramas para una red {L}x{L}...")
...     energies, magnetizations = enumerate_ising(L, periodic_boundary=True)
...     plot_histograms(energies, magnetizations, L)
