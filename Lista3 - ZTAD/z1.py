import numpy as np
import matplotlib.pyplot as plt

controlB=[0.08, 0.10, 0.15, 0.17, 0.24, 0.34, 0.38, 0.42, 0.49, 0.50, 0.70, 0.94, 0.95,
1.26, 1.37, 1.55, 1.75, 3.20, 6.98, 50.57]

d = np.arange(20)/float(20)

plt.plot(controlB,d, marker='o')
plt.show()