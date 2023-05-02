import pandas as pd
import requests
import csv
API_KEY = 'GEOCODING_API_KEY'

base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

df = pd.read_csv('czyste_mieszkania.csv', index_col=0)
set_of_addresses = set(df.adres.values.tolist())
counter = 0
dict_to_save = {}
for address in set_of_addresses:
    params = {
        'key': API_KEY,
        'address': address
    }
    response = requests.get(base_url, params=params).json()
    location = response['results'][0]['geometry']['location']
    lat = location['lat']
    lng = location['lng']
    dict_to_save[address] = {'lat': lat, 'lng': lng}
    counter += 1
    print(counter)
w = csv.writer((open("adresy.csv", "w")))
for key, val in dict_to_save.items():
    w.writerow([key, val])
