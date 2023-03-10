import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(1000)

plt.hist(x)
plt.show()

print(f'Średnia: {np.mean(x)} Wariancja: {np.var(x)}')

def gen1(x, N):
    m = 8191
    a = 101
    c = 1731
    y = [0]*N
    for i in range(N):
        x = (a * x + c) % m
        y[i] = x / m
    return y

print(gen1(x,20))