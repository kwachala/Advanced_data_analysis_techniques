import numpy as np
from scipy import stats

m = 3
x = np.array([1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7])
print((stats.ttest_1samp(x, m))[1])
p = (stats.ttest_1samp(x, m))[1]

alpha = 0.05

if p < alpha:
    print("Średni czas oczekiwania na dostarczenie przesyłki jest istotnie różny od 3 dni.")
else:
    print("Nie ma istotnej różnicy między średnim czasem oczekiwania na dostarczenie przesyłki a 3 dni.")
