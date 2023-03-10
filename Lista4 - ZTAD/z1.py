from scipy import stats

data13 = [
    175.26, 177.8, 167.64000000000001, 160.02, 172.72, 177.8, 175.26, 170.18, 157.48, 160.02, 193.04, 149.86, 157.48,
    157.48, 190.5, 157.48, 182.88, 160.02]
data17 = [
    172.72, 157.48, 170.18, 172.72, 175.26, 170.18, 154.94, 149.86, 157.48, 154.94, 175.26, 167.64000000000001, 157.48,
    157.48, 154.94, 177.8]

p_value = stats.ttest_ind(data13, data17, equal_var=True, alternative='two-sided')[1]
alpha = 0.05

if p_value > alpha:
    print('Nie ma podstaw do odrzucenia hipotezy zerowej')
else:
    print('Odrzucamy hipotezę zerową')