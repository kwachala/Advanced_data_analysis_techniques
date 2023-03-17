from scipy.stats import mannwhitneyu

# Hipoteza zerowa: wzrost studentów z jednej grupy jest równie duży jak wzrost studentów drugiej grupy
# Hipoteza alternatywna: wzrost studentów z jednej grupy nie jest równie duży jak wzrost studentów drugiej grupy

data13 = [175.26, 177.8, 167.64, 160.02, 172.72, 177.8, 175.26, 170.18, 157.48, 160.02, 193.04, 149.86, 157.48, 157.48,
          190.5, 157.48, 182.88, 160.02]
data17 = [172.72, 157.48, 170.18, 172.72, 175.26, 170.18, 154.94, 149.86, 157.48, 154.94, 175.26, 167.64, 157.48,
          157.48, 154.94, 177.8]

stat, p1 = mannwhitneyu(data13, data17)
alpha = 0.05
print(p1)

if p1 > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')
