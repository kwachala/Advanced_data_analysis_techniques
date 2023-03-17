from scipy.io import loadmat
from scipy import stats

data_set = loadmat("anova_data.mat")

df1 = data_set['wombats']
df2 = data_set['wombat_groups']

df1 = df1[0]
df2 = df2[0]

group1 = []
group2 = []
group3 = []

for count, value in enumerate(df1):
    group = df2[count]
    match group:
        case 1:
            group1.append(value)
        case 2:
            group2.append(value)
        case 3:
            group3.append(value)

alpha = 0.05
p_anova = stats.f_oneway(group1, group2, group3)[1]
print(p_anova)
print('------------------------------------ANOVA------------------------------------')

if p_anova > alpha:
    print(
        'Nie ma podstaw do odrzucenia hipotezy zerowej (próbki pochodzą z populacji o jednakowych wartościach średnich)')
else:
    print(
        'Odrzucamy hipotezę zerową (dla przynajmniej jednej próbki średnia z niej jest znacząca inna od średnich z pozostałych próbek)')
