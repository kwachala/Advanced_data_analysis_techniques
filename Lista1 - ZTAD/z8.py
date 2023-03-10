import matplotlib.pyplot as plt
import numpy as np

x = np.array([8.5, 7.6, 9.3, 5.5, 11.4, 6.9, 6.5, 12.9, 8.7, 4.8, 4.2, 8.1, 6.5, 5.8, 6.7, 2.4, 11.1, 7.1, 8.8, 7.2])

#jaki wynik?
#y = np.array([np.mean(x), np.median(x), np.std(x)])

plt.subplot(211)
plt.boxplot(x)
plt.subplot(212)
plt.hist(x)
plt.show()

print(f'Średnia: {np.mean(x)} Mediana: {np.median(x)} Odchylenie standardowe: {np.std(x)}')
