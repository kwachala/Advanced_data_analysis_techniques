import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv('absolwenci.txt', sep=';')

rolnictwo = df[df.COLLEGE == 'Rolnictwo']
pedagogika = df[df.COLLEGE == 'Pedagogika']

rolnictwo = np.array(rolnictwo['SALARY'])
pedagogika = np.array(pedagogika['SALARY'])

alpha = 0.05

p_value = stats.shapiro(rolnictwo)[1]

if p_value > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')

p_value = stats.shapiro(pedagogika)[1]

if p_value > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')