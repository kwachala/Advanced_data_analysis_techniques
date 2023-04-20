import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.api import qqplot
import matplotlib.pyplot as plt

df = pd.read_csv('pacjenci.csv')
df = np.array(df['cukier'])

alpha = 0.05
p_value = stats.shapiro(df)[1]

if p_value > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')
print(df)
qqplot(df, line='45',fit=True)
plt.show()