Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... import matplotlib.pyplot as plt
... 
... def markov_pi(N, delta):
...     # Inicialización
...     N_hits = 0
...     x, y = 1.0, 1.0  # Posición inicial
...     
...     # Generador de números aleatorios
...     rng = np.random.default_rng()
...     
...     for _ in range(N):
...         # Genera movimientos aleatorios
...         delta_x = rng.uniform(-delta, delta)
...         delta_y = rng.uniform(-delta, delta)
...         
...         # Condición de aceptación de movimiento
...         if abs(x + delta_x) < 1 and abs(y + delta_y) < 1:
...             x += delta_x
...             y += delta_y
...         
...         # Condición de estar dentro del círculo
...         if x**2 + y**2 < 1:
...             N_hits += 1
...     
...     return N_hits
... 
... # Parámetros del experimento
... N = 100000  # Número de pasos
... delta_values = np.linspace(0, 3, 100)  # Valores de delta
... pi_over_4 = np.pi / 4
... 
... # Variables para almacenar resultados
... mean_squared_deviation = []
... rejection_rates = []
... 
... # Realiza las simulaciones para diferentes valores de delta
for delta in delta_values:
    N_hits = markov_pi(N, delta)
    hits_over_N = N_hits / N
    
    # Calcula la desviación cuadrática media
    deviation = (hits_over_N - pi_over_4)**2
    mean_squared_deviation.append(deviation)
    
    # Tasa de rechazo
    rejection_rate = 1 - (N_hits / N)
    rejection_rates.append(rejection_rate)

# Graficar la desviación cuadrática media vs delta
plt.figure(figsize=(10, 6))
plt.plot(delta_values, mean_squared_deviation, label="Desviación Cuadrática Media", color='b')
plt.xlabel('δ')
plt.ylabel('Desviación Cuadrática Media')
plt.title('Desviación Cuadrática Media vs δ')
plt.grid(True)
plt.legend()
plt.show()

# Graficar la tasa de rechazo vs delta
plt.figure(figsize=(10, 6))
plt.plot(delta_values, rejection_rates, label="Tasa de Rechazo", color='r')
plt.xlabel('δ')
plt.ylabel('Tasa de Rechazo')
plt.title('Tasa de Rechazo vs δ')
plt.grid(True)
plt.legend()
