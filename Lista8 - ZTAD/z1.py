import pandas as pd

df = pd.read_excel('254271.xls', sheet_name='Dane')
print(df)
df['status pozyczki'] = df['status pozyczki'].apply(lambda x: 'dobry' if x in ['splacona_cz', 'splacona'] else 'zły')

df.drop('opóźnienie spłaty', axis=1, inplace=True)

column = df.pop('status pozyczki')
df['status pozyczki'] = column

print(df.head(10))

df['wiek'] = pd.cut(df['wiek'], bins=5, labels=False)

print(df)
df.to_excel('254271L3 1.xlsx')
