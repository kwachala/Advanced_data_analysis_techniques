from scipy import stats
import pandas as pd

df = pd.read_csv(r'C:\Users\drago\PycharmProjects\ZTAD\Lista4 - ZTAD\czytelnictwo.csv')

data_before, data_after = df['przed'], df['po']

alpha = 0.05
p1 = stats.ranksums(data_before, data_after)[1]

if p1 > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową (czyli zatrudnienie miało wpływ na ilość czasu poświęconego na czytanie prasy)')
