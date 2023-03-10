from scipy import stats
import numpy as np

h = 0.49
x = np.random.normal(loc=0.38, scale=0.14, size=18)

#ttest
print(stats.ttest_1samp(x, h))

#tcdf
m = np.\
    mean(x)
s = np.std(x, ddof=1) # używamy ddof=1 aby obliczyć estymator nieobciążony odchylenia standardowego??

h = 0.49

t_stat = (m - h) / (s / np.sqrt(len(x)))
df = len(x) - 1
p = (stats.t.cdf(t_stat, df) * 2)
print(p)

alpha = 0.01

if p < alpha:
    print("Średni procentowy wzrost wartości nieruchomości różni się istotnie od 49%.")
else:
    print("Nie ma istotnej różnicy między średnim procentowym wzrostem wartości nieruchomości a 49%.")