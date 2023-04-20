from scipy.io import loadmat
import statsmodels.stats.multicomp as mc
from scipy.stats import f_oneway

data_set = loadmat("anova_data.mat")

df = data_set['popcorn']

group1 = []
group2 = []
group3 = []

for sample in range(len(df)):
    group1.append(df[sample][0])
    group2.append(df[sample][1])
    group3.append(df[sample][2])

f_statistic, p_value = f_oneway(group1, group2, group3)
if p_value < 0.05:
    print('Różnica między średnimi jest statystycznie znacząca')
else:
    print('Różnica między średnimi nie jest statystycznie znaczaca')

groups = ['group1'] * len(group1) + ['group2'] * len(group2) + ['group3'] * len(group3)
data = group1 + group2 + group3

tukey_results = mc.MultiComparison(data, groups).tukeyhsd()

print(tukey_results)

# hipoteza o rownosci srednich odrzucona dla g1 - g2 i g1 - g3
