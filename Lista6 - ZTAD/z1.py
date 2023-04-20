from scipy.io import loadmat
from scipy import stats
from statsmodels.api import qqplot
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_set = loadmat("anova_data.mat")

df = data_set['koala']

group1 = []
group2 = []
group3 = []

for sample in range(len(df)):
    group1.append(df[sample][0])
    group2.append(df[sample][1])
    group3.append(df[sample][2])

alpha = 0.05
p_independence = stats.chi2_contingency([group1, group2, group3])[1]

if p_independence > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej (czyli próbki są niezależne)')
else:
    print('Odrzucamy hipotezę zerową (czyli próbki są zależne)')

p_norm_1 = stats.shapiro(group1)[1]
p_norm_2 = stats.shapiro(group2)[1]
p_norm_3 = stats.shapiro(group3)[1]

if p_norm_1 > alpha:
    print('Powinniśmy zaakceptować hipotezę zerowa (czyli jest rozkład normalny)')
else:
    print('Odrzucamy hipotezę zerową (czyli nie ma rozkładu normalnego)')

if p_norm_2 > alpha:
    print('Powinniśmy zaakceptować hipotezę zerowa (czyli jest rozkład normalny)')
else:
    print('Odrzucamy hipotezę zerową (czyli nie ma rozkładu normalnego)')

if p_norm_3 > alpha:
    print('Powinniśmy zaakceptować hipotezę zerowa (czyli jest rozkład normalny)')
else:
    print('Odrzucamy hipotezę zerową (czyli nie ma rozkładu normalnego)')

p_var = stats.levene(group1, group2, group3)[1]

if p_var > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej (czyli jest homogeniczność wariancji)')
else:
    print('Odrzucamy hipotezę zerową (występują różnice między wariancjami w porównywanych grupach)')

p_anova = stats.f_oneway(group1, group2, group3)[1]
print('------------------------------------ANOVA------------------------------------')
if p_anova > alpha:
    print(
        'Nie ma podstaw do odrzucenia hipotezy zerowej (próbki pochodzą z populacji o jednakowych wartościach średnich)')
else:
    print(
        'Odrzucamy hipotezę zerową (dla przynajmniej jednej próbki średnia z niej jest znacząca inna od średnich z pozostałych próbek)')

group1 = np.array(group1)
group2 = np.array(group2)
group3 = np.array(group3)

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(6, 8))

qqplot(group1, line='45', fit=True, ax=axes[0])
qqplot(group2, line='45', fit=True, ax=axes[1])
qqplot(group3, line='45', fit=True, ax=axes[2])

axes[0].set_title('Group 1')
axes[1].set_title('Group 2')
axes[2].set_title('Group 3')

plt.tight_layout()
plt.show()
