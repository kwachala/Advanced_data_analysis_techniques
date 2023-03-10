from scipy import stats
import pandas as pd

df = pd.read_csv('absolwenci.txt', sep=';')
df = df.drop(['GRADUATE', 'COLLEGE', 'GRADDATE', 'DEGREE'], axis=1)
print(df)

'''
Nie, dla tych danych nie można przeprowadzić testu dla prób zależnych, ponieważ brak jest związku między obserwacjami w obu 
grupach (kobiety i mężczyźni). W przypadku testu dla prób zależnych potrzebujemy par obserwacji, gdzie każda para składa 
się z obserwacji dla jednej jednostki w dwóch różnych warunkach. Natomiast w danych podanych w pytaniu nie ma takiej 
zależności między płcią a wynagrodzeniem, ponieważ pomiędzy obserwacjami dla kobiet a mężczyzn nie ma bezpośredniego powiązania
(Nie są to te same osoby).
'''
