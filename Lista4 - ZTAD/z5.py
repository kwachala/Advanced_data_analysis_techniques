from scipy import stats

data13 = [175.26, 177.8, 167.64000000000001, 160.02, 172.72, 177.8, 175.26, 170.18, 157.48, 160.02, 193.04, 149.86,
          157.48, 157.48, 190.5, 157.48, 182.88, 160.02]

alpha = 0.05
p1 = stats.shapiro(data13)[1]

print('Sprawdzenie normalności rozkładu:')

if p1 > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')

p2 = stats.ttest_1samp(data13, 169.051)[1]

print('Test T dla jednej próby:')

if p2 > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')
