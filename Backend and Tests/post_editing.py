import pandas as pd


df = pd.read_csv('mieszkania.csv', index_col=0)
to_delete = []
print(df)
for index, row in df.iterrows():
    if len(row.adres.split(',')) < 3:
        to_delete.append(index)
df2 = df.drop(to_delete, axis=0)
df2 = df2.reset_index().drop('index', axis=1)
df2 = df2.drop_duplicates(keep='first')
df2 = df2.replace(to_replace='10+', value='10')
prices = df2['cena']
nowe_ceny=[]
for price in prices:
    if ',' in price:
        price = price.replace(',', '.')
    nowe_ceny.append(price)
df2['cena'] = nowe_ceny
df2[["pokoje", "metraz", "cena"]] = df2[["pokoje", "metraz", "cena"]].apply(pd.to_numeric)
df2 = df2[df2['pokoje'] < 7]
df2.to_csv('final_mieszkania.csv')
