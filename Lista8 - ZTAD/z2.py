import pandas as pd

df = pd.read_excel('254271.xls', sheet_name='Dane')

to_drop = df[(df['status pozyczki'] == 'odmowa') | (df['kwota otrzymana'] > 900)]
df.drop(to_drop.index, inplace=True)
df.drop('status pozyczki', axis=1, inplace=True)
print(df.head(10))

df.to_excel('254271L3 2.xlsx')