from scipy import stats

# Hipoteza alternatywna: Osoby nerwowe mają większą średnią ilość gestów na minutę podczas swobodnej konwersacji niż osoby spokojne.
# Hipoteza zerowa: Średnia ilość gestów na minutę podczas swobodnej konwersacji jest taka sama dla osób nerwowych i spokojnych.

alpha = 0.05

nerwowi = [3, 3, 4, 5, 5]
spokojni = [4, 6, 7, 9, 9]

# normalność rozkładu
p1 = stats.shapiro(nerwowi)[1]
p2 = stats.shapiro(spokojni)[1]

if p1 > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')

if p2 > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')

# równość wariancji
p3 = stats.levene(nerwowi, spokojni)[1]

if p3 > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')

# stopień swobody to (n1 + n2 - 2) = (5+5-2) = 8
p_value = stats.ttest_ind(nerwowi, spokojni, equal_var=True, alternative='greater')[1]
print(p_value)

if p_value > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')
