Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np

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
    density_of_states = {}
    density_of_states[E] = 2
    
    for i in range(1, 2**(N-1)):
        k, spins = gray_flip(spins)
        if k is None:
            break
        
        # Calcular el campo en el sitio k
        h = 0
        for neighbor in get_neighbors(k-1, L, periodic_boundary):
            h += sigma[neighbor]
        
        E += 2 * sigma[k-1] * h
        density_of_states[E] = density_of_states.get(E, 0) + 2
        sigma[k-1] *= -1
    
    return density_of_states

# Función auxiliar para obtener los vecinos de un sitio en la red
def get_neighbors(index, L, periodic_boundary):
    row, col = divmod(index, L)
...     neighbors = []
...     
...     if row > 0:
...         neighbors.append((row - 1) * L + col)
...     elif periodic_boundary:
...         neighbors.append((L - 1) * L + col)
...     
...     if row < L - 1:
...         neighbors.append((row + 1) * L + col)
...     elif periodic_boundary:
...         neighbors.append(col)
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
... # Ejemplo de uso para redes 2x2, 4x4, 6x6
... for L in [2, 4, 6]:
...     print(f"Densidad de estados para una red {L}x{L} con condiciones de borde periódicas:")
...     dos = enumerate_ising(L, periodic_boundary=True)
...     for E, N in sorted(dos.items()):
...         print(f"E = {E}, N(E) = {N}")
...     print()
...     
...     print(f"Densidad de estados para una red {L}x{L} sin condiciones de borde periódicas:")
...     dos = enumerate_ising(L, periodic_boundary=False)
...     for E, N in sorted(dos.items()):
...         print(f"E = {E}, N(E) = {N}")
...     print()
