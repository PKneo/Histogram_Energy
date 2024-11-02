import numpy as np
import matplotlib.pyplot as plt

# Number of symbols to generate
n_symbols = 10000

# Generate random bits (0 or 1) for D1, D2, and D3
D = np.random.randint(0, 2, (n_symbols, 3))

# Calculate the corresponding symbols X_i
X = np.zeros(n_symbols)
for i in range(n_symbols):
    D3i1 = D[i, 0]  # D_{3i+1}
    D3i2 = D[i, 1]  # D_{3i+2}
    D3i3 = D[i, 2]  # D_{3i+3}
    
    # Calculate the value of X_i
    X[i] = (-1)**D3i3 * np.sqrt(2 * (2 * D3i1 + D3i2) + 1)

# Calculate energies
energies = np.abs(X)**2  # E_i = |X_i|^2

# Plot the histogram of energies
plt.figure(figsize=(10, 6))
plt.hist(energies, bins=np.arange(0.5, 8.5, 1), alpha=0.7, edgecolor='black', density=True)
plt.xticks([1, 3, 5, 7])
plt.title('Histogram of Energies of Transmitted Symbols')
plt.xlabel('Energy (E_i)')
plt.ylabel('Probability Density')
plt.grid(axis='y')
plt.show()
