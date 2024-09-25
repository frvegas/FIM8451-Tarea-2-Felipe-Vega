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
... N_values = [10, 100, 1000, 10000, 100000,1000000,10000000,100000000]
... runs = 20
... 
... pi_estimates = []
... 
... # Realiza las simulaciones
... for N in N_values:
...     hits_over_N = []
...     for _ in range(runs):
...         N_hits = direct_pi(N)
...         hits_over_N.append((N_hits / N) * 4) 
...     
...     # Calcula el valor promedio estimado de pi
...     pi_estimates.append(np.mean(hits_over_N))
... 
... # Grafica los resultados
... plt.figure(figsize=(10, 6))
... plt.plot(N_values, pi_estimates, marker='o', linestyle='-', color='r', label='Estimación de π')
... plt.axhline(y=np.pi, color='b', linestyle='--', label='Valor real de π')
... plt.xlabel('N')
... plt.ylabel('Estimación de π')
... plt.title('Estimación de π vs Número de Ensayos (N)')
... plt.legend()
... plt.grid(True)
