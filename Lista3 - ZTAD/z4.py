import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv('pacjenci.csv')
df = df.drop(['waga','cukier'], axis=1)

df_m = df[df.plec == 'M']
df_k = df[df.plec == 'K']

hm = np.array(df_m['wzrost'])
hk = np.array(df_k['wzrost'])

alpha = 0.05
p_value = stats.ks_2samp(hm, hk)[1]

if p_value > alpha:
    print('Powinniśmy zaakceptować hipotezę zerowa Zgodnie z przeprowadzonym testem, różnica pomiędzy obiema próbkami nie jest statystycznie znacząca aby móc stwierdzić, iż oba te rozkłady sąróżne.')
else:
    print('Odrzucamy hipotezę zerową')

p_value = stats.shapiro(hm)[1]



if p_value > alpha:
    print('Powinniśmy zaakceptować hipotezę zerowa')
else:
    print('Odrzucamy hipotezę zerową')

p_value = stats.shapiro(hk)[1]


if p_value > alpha:
    print('Powinniśmy zaakceptować hipotezę zerowa')
else:
    print('Odrzucamy hipotezę zerową')

