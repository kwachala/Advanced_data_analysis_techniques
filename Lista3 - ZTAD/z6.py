import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.diagnostic import lilliefors

df = pd.read_csv('pacjenci.csv')
df = df.drop(['waga','cukier'], axis=1)

df_m = df[df.plec == 'M']
df_k = df[df.plec == 'K']

hm = np.array(df_m['wzrost'])
hk = np.array(df_k['wzrost'])

alpha = 0.05
p_value = lilliefors(hm,'norm')[1]
if p_value > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')

p_value = lilliefors(hk,'norm')[1]
if p_value > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')
