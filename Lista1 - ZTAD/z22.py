import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x1=2*(np.random.randn(100,1)+1)
x2=3*(np.random.randn(100,1)-1)

z = [x1, x2]

plt.subplot(211)
sns.boxplot(data=z)
plt.subplot(212)
plt.hist(z[0])
plt.hist(z[1])

plt.show()
