from scipy import stats

# Hipoteza alternatywna: Osoby nerwowe mają większą średnią ilość gestów na minutę podczas swobodnej konwersacji niż osoby spokojne.
# Hipoteza zerowa: Średnia ilość gestów na minutę podczas swobodnej konwersacji jest taka sama dla osób nerwowych i spokojnych.

alpha = 0.05

nerwowi = [3, 3, 4, 5, 5]
spokojni = [4, 6, 7, 9, 9]

u, p1 = stats.mannwhitneyu(nerwowi, spokojni, alternative='greater')

# jak sprawdza się dla less a nie greeater to wychodzi że odrzucamy zerową więc przyjmujemy,
# że nerwowi mają mniejszą tendencje do gestykulacji

if p1 > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')
