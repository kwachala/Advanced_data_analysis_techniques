#P(Z < 2) = 0,9772
#P(|Z| < 2) = 1 - 0,0456 = 0,9544

from scipy import stats

print(stats.norm.cdf(2))
print(stats.norm.cdf(2)-stats.norm.cdf(-2))