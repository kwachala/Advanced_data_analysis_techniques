from scipy import stats

#Hipoteza alternatywna: Osoby poniżej 30 lat są bardziej dowcipne niż osoby po 30.
#Hipoteza zerowa: Nie ma istotnej różnicy w średnim poziomie 'rozbawienia' między osobami poniżej 30 a powyżej 30 lat.

alpha = 0.05

mniej30 = [6, 7, 10, 9]
po30 = [5, 6, 2, 3]


#normalność rozkładu
p1 = stats.shapiro(mniej30)[1]
p2 = stats.shapiro(po30)[1]

if p1 > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')

if p2 > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')

#równość wariancji
p3 = stats.levene(mniej30, po30)[1]

if p3 > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')

#stopień swobody to (n1 + n2 - 2) = (4+4-2) = 6
p_value = stats.ttest_ind(mniej30, po30, equal_var=True, alternative='greater')[1]
print(p_value)

if p_value > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')