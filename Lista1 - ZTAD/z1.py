import numpy as np
import numpy.matlib

print('--------------- Macierz zer ---------------')
print(np.zeros((2,4)))

print('--------------- Macierz jedynek ---------------')
print(np.ones((2,4)))

print('--------------- Macierz jednostkowa ---------------')
X = np.eye(3)
print(X)

print('--------------- Twarzenie macierzy złożonej z kopii podanej macierzy ---------------')
np.matlib.repmat(X, 2, 2)

print('--------------- Macierz wypełniona liczbami z rozkładu płaskiego (0,1) ---------------')
print(np.random.rand(4,3))

print('--------------- Macierz wypełniona liczbami z rozkładu normalnego o średniej 0 i wariancji 1 ---------------')
print(np.random.randn(4,3))

print('--------------- Rozmiary macierzy ---------------')
print(X.shape)
print(X.size)

print('--------------- Macierze tworzone ręcznie ---------------')
A = np.array([[1,2,3,4],[5,6,7,8],[9,1,2,3]])
B = np.array([[1,2],[3,4]])

print(A)
print(B)

print('--------------- Transpozycja macierzy ---------------')
print(np.transpose(A))

print('--------------- Suma/Różnica/Mnożenie macierzy ---------------')
C = np.random.rand(3,3)
print(C)
print(X+C)
print(X-C)

x1 = np.arange(9.0).reshape((3, 3))
x2 = np.arange(3.0)
print(np.matmul(x2,x1))

print('--------------- Mnożenie elementów macierzy ---------------')
print(X*C)

print('--------------- Konkretny element macierzy ---------------')
print(x1[1,2])
