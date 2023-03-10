import numpy as np
from scipy.stats import chi2

sample = np.random.normal(loc=5, scale=1.3, size=25)
alpha = 0.1
# obliczenie wartości statystyki testowej
n = len(sample)
s = np.var(sample, ddof=1)
print(s)
h0 = 1.6
test_statistic = (n - 1) * (s ** 2) / h0

critical_value = chi2.ppf(1 - alpha, n - 1)
print(test_statistic)
print(critical_value)

if test_statistic < critical_value:
    print("Wariancja próby jest mniejsza niż 1.6 (hipoteza alternatywna)")
else:
    print("Wariancja próby nie jest mniejsza niż 1.6 (hipoteza zerowa)")
