import pandas as pd
import ast

df_addresses = pd.read_csv('adresy.csv', index_col=None)
df_estates = pd.read_csv('czyste_mieszkania.csv', index_col=0)
address_dict = {}
for index, row in df_addresses.iterrows():
    address_dict[row.values[0]] = ast.literal_eval(row.values[1])
lat = []
lng = []
for index, row in df_estates.iterrows():
    address = row.values[0]
    lat.append(address_dict[address]['lat'])
    lng.append(address_dict[address]['lng'])

df_estates['lat'] = lat
df_estates['lng'] = lng

df_estates = df_estates[['adres', 'lat', 'lng', 'pokoje', 'metraz', 'cena']]
df_estates.to_csv('mieszkania_z_wspolrzedne.csv')

