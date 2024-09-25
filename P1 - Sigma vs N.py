Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... import matplotlib.pyplot as plt
... 
... def direct_pi(N):
...     N_hits = 0
...     for _ in range(N):
...         x = np.random.uniform(-1, 1)
...         y = np.random.uniform(-1, 1)
...         if x**2 + y**2 < 1:
...             N_hits += 1
...     return N_hits
... 
... # Parámetros del experimento
... N_values = [10, 100, 1000, 10000, 100000,10000000,100000000]
... runs = 20
... pi_over_4 = np.pi / 4
... 
... # Variables para almacenar resultados
... mean_squared_deviation = []
... 
... # Realiza las simulaciones
... for N in N_values:
...     hits_over_N = []
...     for _ in range(runs):
...         N_hits = direct_pi(N)
...         hits_over_N.append(N_hits / N)
...     
...     # Calcula la desviación cuadrática media
...     mean_deviation = np.mean([(x - pi_over_4)**2 for x in hits_over_N])
...     mean_squared_deviation.append(mean_deviation)
... 
... # Grafica los resultados en log-log
... plt.figure(figsize=(10, 6))
... plt.plot(N_values, mean_squared_deviation, marker='o', linestyle='-', color='b')
... plt.xscale('log')
... plt.yscale('log')
... plt.xlabel('N')
plt.ylabel('Desviación Cuadrática Media')
plt.title('Desviación Cuadrática Media vs N (Escala Log-Log)')
plt.grid(True, which="both", ls="--")
plt.show()
