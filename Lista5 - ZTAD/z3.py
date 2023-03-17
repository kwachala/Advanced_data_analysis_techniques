import pandas as pd
from scipy import stats

df = pd.read_csv(r'C:\Users\drago\PycharmProjects\ZTAD\Lista4 - ZTAD\chmiel.csv')

zapylona, niezapylona = df['zapylona'], df['niezapyl']

# nie ma rozkladu normalnego

alpha = 0.05
p1 = stats.ranksums(zapylona, niezapylona)[1]

if p1 > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową (czyli zapylenie ma wpływ na masę nasion)')
