import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd
import itertools
from scipy import stats
import matplotlib.pyplot as plt

'''
konwersja danych do listy w konsoli
data = '4,64 5,12 4,64 3,21 3,92 4,95 3,75 2,95 2,95 5,92 6,10 4,32 3,17 3,75 5,22 2,50 3,21 2,80 5,25 4,85 4,13 3,88 4,01 5,16 2,65 3,15 3,63 6,17 4,72 5,17 3,50 4,64 5,35 2,84 3,25 3,85 4,20 5,36 3,77 2,47 3,63 4,35 3,09 2,30 2,19 5,90 5,41 3,85 4,12 3,46 4,89 2,90 2,76 3,32 5,07 5,31 4,12 3,51 4,01 5,61 2,62 3,01 2,68 4,13 4,78 5,07 3,85 3,39 4,98 2,75 2,31 3,35 4,07 5,08 3,25 4,22 3,78 5,77 3,10 2,50 3,12 5,30 4,97 3,49 3,07 3,51 5,23 1,99 2,02 4,11 4,37 5,85 3,65 3,62 3,19 4,76 2,42 2,64 2,90 3,76 5,26 4,10 2,95 4,04 5,15 2,37 2,27 2,75'
data = data.replace(',', '.')
data = data.replace(' ', ',')
'''

data = [4.64, 5.12, 4.64, 3.21, 3.92, 4.95, 3.75, 2.95, 2.95, 5.92, 6.10, 4.32, 3.17, 3.75, 5.22, 2.50, 3.21, 2.80,
        5.25, 4.85, 4.13, 3.88, 4.01, 5.16, 2.65, 3.15, 3.63, 6.17, 4.72, 5.17, 3.50, 4.64, 5.35, 2.84, 3.25, 3.85,
        4.20, 5.36, 3.77, 2.47, 3.63, 4.35, 3.09, 2.30, 2.19, 5.90, 5.41, 3.85, 4.12, 3.46, 4.89, 2.90, 2.76, 3.32,
        5.07, 5.31, 4.12, 3.51, 4.01, 5.61, 2.62, 3.01, 2.68, 4.13, 4.78, 5.07, 3.85, 3.39, 4.98, 2.75, 2.31, 3.35,
        4.07, 5.08, 3.25, 4.22, 3.78, 5.77, 3.10, 2.50, 3.12, 5.30, 4.97, 3.49, 3.07, 3.51, 5.23, 1.99, 2.02, 4.11,
        4.37, 5.85, 3.65, 3.62, 3.19, 4.76, 2.42, 2.64, 2.90, 3.76, 5.26, 4.10, 2.95, 4.04, 5.15, 2.37, 2.27, 2.75]

toxic_group = []

for count in range(len(data)):
    modulo = (count + 1) % 3
    match modulo:
        case 1:
            toxic_group.append('T1')
        case 2:
            toxic_group.append('T2')
        case 0:
            toxic_group.append('T3')

lst = ['Z1', 'Z2', 'Z3']
company_group = list(itertools.chain.from_iterable(itertools.repeat(x, 3) for x in lst))

company_group *= 12

df = pd.DataFrame({'company': company_group, 'toxic_group': toxic_group, 'FED': data})

df_z1_t1 = df.loc[df['company'] == 'Z1']
df_z1_t1 = df_z1_t1.loc[df_z1_t1['toxic_group'] == 'T1']

df_z1_t2 = df.loc[df['company'] == 'Z1']
df_z1_t2 = df_z1_t2.loc[df_z1_t2['toxic_group'] == 'T2']

df_z1_t3 = df.loc[df['company'] == 'Z1']
df_z1_t3 = df_z1_t3.loc[df_z1_t3['toxic_group'] == 'T3']

df_z2_t1 = df.loc[df['company'] == 'Z2']
df_z2_t1 = df_z2_t1.loc[df_z2_t1['toxic_group'] == 'T1']

df_z2_t2 = df.loc[df['company'] == 'Z2']
df_z2_t2 = df_z2_t2.loc[df_z2_t2['toxic_group'] == 'T2']

df_z2_t3 = df.loc[df['company'] == 'Z2']
df_z2_t3 = df_z2_t3.loc[df_z2_t3['toxic_group'] == 'T3']

df_z3_t1 = df.loc[df['company'] == 'Z3']
df_z3_t1 = df_z3_t1.loc[df_z3_t1['toxic_group'] == 'T1']

df_z3_t2 = df.loc[df['company'] == 'Z3']
df_z3_t2 = df_z3_t2.loc[df_z3_t2['toxic_group'] == 'T2']

df_z3_t3 = df.loc[df['company'] == 'Z3']
df_z3_t3 = df_z3_t3.loc[df_z3_t3['toxic_group'] == 'T3']

levene_samples = [df_z1_t1['FED'], df_z1_t2['FED'], df_z1_t3['FED'], df_z2_t1['FED'], df_z2_t2['FED'], df_z2_t3['FED'],
                  df_z3_t1['FED'], df_z3_t2['FED'], df_z3_t3['FED']]

print(stats.shapiro(df_z1_t1['FED']))
print(stats.shapiro(df_z1_t2['FED']))
print(stats.shapiro(df_z1_t3['FED']))
print(stats.shapiro(df_z2_t1['FED']))
print(stats.shapiro(df_z2_t2['FED']))
print(stats.shapiro(df_z2_t3['FED']))
print(stats.shapiro(df_z3_t1['FED']))
print(stats.shapiro(df_z3_t2['FED']))
print(stats.shapiro(df_z3_t3['FED']))
print(stats.levene(df_z1_t1['FED'], df_z1_t2['FED'], df_z1_t3['FED'], df_z2_t1['FED'], df_z2_t2['FED'], df_z2_t3['FED'],
                   df_z3_t1['FED'], df_z3_t2['FED'], df_z3_t3['FED']))

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(6, 8))

sm.qqplot(df_z1_t1['FED'], line='45', fit=True, ax=axes[0])
sm.qqplot(df_z1_t2['FED'], line='45', fit=True, ax=axes[1])
sm.qqplot(df_z1_t3['FED'], line='45', fit=True, ax=axes[2])

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(6, 8))
sm.qqplot(df_z2_t1['FED'], line='45', fit=True, ax=axes[0])
sm.qqplot(df_z2_t2['FED'], line='45', fit=True, ax=axes[1])
sm.qqplot(df_z2_t3['FED'], line='45', fit=True, ax=axes[2])

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(6, 8))
sm.qqplot(df_z3_t1['FED'], line='45', fit=True, ax=axes[0])
sm.qqplot(df_z3_t2['FED'], line='45', fit=True, ax=axes[1])
sm.qqplot(df_z3_t3['FED'], line='45', fit=True, ax=axes[2])

plt.tight_layout()
plt.show()

# ktore dane maja być sprawdzane pod katem wariancji i normalnosci?

'''
H01: średnie FED dla każdego z zakładów są jednakowe
H02: średnie FED dla każdego rodzaju toksycznej substancji są jednakowe
H03: zakład i rodzaj toksycznej substancji nie mają synergicznego wpływu na średnie populacyjne
'''

model = ols('FED ~ C(company) + C(toxic_group) + C(company):C(toxic_group)', data=df).fit()
test_stats = sm.stats.anova_lm(model, typ=2)
print(test_stats)

# Wszystkie hipotezy odrzucamy przy alpha = 0.05
