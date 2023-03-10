import numpy as np

def stat(array):
    return(np.mean(array), np.std(array))

x = np.random.randn(100,100)

print(stat(x))
