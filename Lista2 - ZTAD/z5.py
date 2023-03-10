import numpy as np
from scipy.stats import levene
import scipy

group1 = np.random.normal(loc=27.7, scale=5.5, size=20)
group2 = np.random.normal(loc=32.1, scale=6.3, size=22)

print(np.var(group1), np.var(group2))

f = np.var(group1, ddof=1) / np.var(group2, ddof=1)

stat, p = levene(group1, group2)

print(stat, p)

g = np.var(group1, ddof=1) / np.var(group2, ddof=1)

p_value = 1 - scipy.stats.f.cdf(g, len(group1) - 1, len(group2) - 1)

print(p_value)

'''
W przeprowadzonym teście nie stwierdzono istotnej statystycznie różnicy między odchyleniami standardowymi
w obu grupach badanych nabywców. Nie ma podstaw do potwierdzenia przypuszczenia, że młodsze osoby łatwiej
decydują się na zakup nowych nieznanych produktów.
'''

