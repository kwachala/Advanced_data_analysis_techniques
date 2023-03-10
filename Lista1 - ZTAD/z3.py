import numpy as np
import matplotlib.pyplot as plt

x1=(np.random.randn(300,1))

plt.subplot(211)
plt.plot(x1)
plt.subplot(212)
plt.hist(x1, bins=20)
plt.hist(x1, bins=100)
plt.show()

plt.boxplot(x1)
plt.show()
