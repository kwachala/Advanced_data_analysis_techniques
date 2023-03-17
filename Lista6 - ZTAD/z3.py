from scipy import stats
import numpy as np

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

# brak normalności rozkładu - kruskal
alpha = 0.05
# czy nie zrobic tylko miedzy 2, 3 i 4?
p_kruskal = stats.kruskal(first, second, third, fourth)[1]

if p_kruskal > alpha:
    print(
        'Nie ma podstaw do odrzucenia hipotezy zerowej (różnice w medianach nie są istotne statystycznie - kampania nie miała wpływu na sprzedaż)')
else:
    print(
        'Odrzucamy hipotezę zerową (dla przynajmniej jednej próbki mediana z niej jest znacząca inna od median z pozostałych próbek - kampania wpłynęła na sprzedaż)')
