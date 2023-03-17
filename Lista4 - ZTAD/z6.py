from scipy import stats

data17 = [172.72, 157.48, 170.18, 172.72, 175.26, 170.18, 154.94, 149.86, 157.48, 154.94, 175.26, 167.64000000000001,
          157.48, 157.48, 154.94, 177.8]

alpha = 0.05
p1 = stats.shapiro(data17)[1]

print('Sprawdzenie normalności rozkładu:')

if p1 > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')
