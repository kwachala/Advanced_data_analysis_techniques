from scipy import stats
import statsmodels.stats.descriptivestats
import matplotlib.pyplot as plt

w1 = [88, 69, 86, 59, 57, 82, 94, 93, 64, 91, 86, 59, 91, 60, 57, 92, 70, 88, 70, 85]
w2 = [73, 68, 75, 54, 53, 84, 84, 86, 66, 84, 78, 58, 91, 57, 59, 88, 71, 84, 64, 85]

p1 = stats.wilcoxon(w1, w2)[1]

alpha = 0.05

if p1 > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową (czyli dieta działa)')

plt.subplot(211)
plt.boxplot(w1)
plt.subplot(212)
plt.boxplot(w2)
plt.show()
