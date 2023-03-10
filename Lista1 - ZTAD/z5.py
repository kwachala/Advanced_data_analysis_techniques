import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("iris.txt", delimiter=r"\s+")
df2 = pd.read_csv("glass.txt", delimiter=r"\s+")

plt.subplot(211)
plt.hist(df1['PL'].values,bins=7)
plt.subplot(212)
plt.hist(df2['Si'].values,bins=7)
plt.show()