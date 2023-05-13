from scipy import stats
import numpy as np
import statsmodels.stats.multicomp as mc
import pingouin as pg
import seaborn as sb




all = [3415, 4556, 5772, 5432, 1593, 1937, 2242, 2794, 1976, 2056, 2240, 2085, 1526, 1594, 1644, 1705, 1538, 1634, 1866,
       1769, 983, 1086, 1135, 1177, 1050, 1209, 1245, 977, 1861, 2087, 2054, 2018, 1714, 2415, 2361, 2424, 1320, 1621,
       1624, 1551, 1276, 1377, 1522, 1412, 1263, 1279, 1350, 1490, 1271, 1417, 1583, 1513, 1436, 1310, 1357, 1468]

first = []
second = []
third = []
fourth = []

for count, value in enumerate(all):
    modulo = (count + 1) % 4
    match modulo:
        case 1:
            first.append(value)
        case 2:
            second.append(value)
        case 3:
            third.append(value)
        case 0:
            fourth.append(value)
alpha = 0.05
# brak normalności rozkładu - kruskal
p_norm_1 = stats.shapiro(first)[1]
if p_norm_1 > alpha:
    print('Powinniśmy zaakceptować hipotezę zerowa (czyli jest rozkład normalny)')
else:
    print('Odrzucamy hipotezę zerową (czyli nie ma rozkładu normalnego)')

p_norm_2 = stats.shapiro(second)[1]
if p_norm_2 > alpha:
    print('Powinniśmy zaakceptować hipotezę zerowa (czyli jest rozkład normalny)')
else:
    print('Odrzucamy hipotezę zerową (czyli nie ma rozkładu normalnego)')

p_norm_3 = stats.shapiro(third)[1]
if p_norm_3 > alpha:
    print('Powinniśmy zaakceptować hipotezę zerowa (czyli jest rozkład normalny)')
else:
    print('Odrzucamy hipotezę zerową (czyli nie ma rozkładu normalnego)')

p_norm_4 = stats.shapiro(fourth)[1]
if p_norm_4 > alpha:
    print('Powinniśmy zaakceptować hipotezę zerowa (czyli jest rozkład normalny)')
else:
    print('Odrzucamy hipotezę zerową (czyli nie ma rozkładu normalnego)')

# czy nie zrobic tylko miedzy 2, 3 i 4?
p_friedman = stats.friedmanchisquare(first, second, third, fourth)[1]

if p_friedman > alpha:
    print(
        'Nie ma podstaw do odrzucenia hipotezy zerowej (różnice w medianach nie są istotne statystycznie - kampania nie miała wpływu na sprzedaż)')
else:
    print(
        'Odrzucamy hipotezę zerową (dla przynajmniej jednej próbki mediana z niej jest znacząca inna od median z pozostałych próbek - kampania wpłynęła na sprzedaż)')

groups = ['group1'] * len(first) + ['group2'] * len(second) + ['group3'] * len(third) + ['group4'] * len(fourth)
data = first + second + third + fourth


tukey_results = mc.MultiComparison(data, groups).tukeyhsd()
print(tukey_results)
sb.boxplot(data)
