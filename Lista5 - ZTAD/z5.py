from scipy import stats
import pandas as pd

df = pd.read_csv(r'C:\Users\drago\PycharmProjects\ZTAD\Lista4 - ZTAD\dane z koronografii.csv')

time_group1 = df.loc[df['group'] == 1]
time_group1 = time_group1['time']

time_group2 = df.loc[df['group'] == 2]
time_group2 = time_group2['time']

# nie ma rozkladu normalnego

alpha = 0.1
p1 = stats.ranksums(time_group1, time_group2)[1]
print(p1)
if p1 > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową (czas ćwiczenia zależy od stanu zdrowia)')
