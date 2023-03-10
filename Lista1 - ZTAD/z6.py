import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.random.normal(loc=3, scale=2.65, size=1000)

y= np.sort(x)
d = np.arange(1000)/float(1000)

plt.subplot(211)
plt.hist(x)
plt.subplot(212)
plt.plot(y,d, marker='o')
plt.show()