from scipy import stats
import numpy as np

x = np.random.normal(loc=31.5, scale=5, size=100)
print(stats.ttest_1samp(x,28))

#odrzucamy H0 na poziomie α=0,05.