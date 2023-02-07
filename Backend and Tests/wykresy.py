import matplotlib.pyplot as plt
import pandas as pd
from numpy import mean

df = pd.read_csv('mieszkania_z_wspolrzedne.csv', index_col=0)

y_ticks = [i*200000 for i in range(11)]
area = df['metraz']
price = df['cena']

plt.scatter(area,price)
plt.xlabel('Metraz [m2]')
plt.ylabel('Cena [mln zl]')
plt.show()

numbers_of_rooms = []
list_mean_price = []
for i in sorted(set(df['pokoje'].values)):
    dfh = df[df['pokoje'] == i]
    sr_cena = mean(dfh['cena'].values)
    numbers_of_rooms.append(i)
    list_mean_price.append(sr_cena)
print(list_mean_price)
plt.xlabel('Liczba pokoi')
plt.ylabel('Średnia cena z mieszkanie [mln zł]')
plt.bar(numbers_of_rooms, list_mean_price)
plt.show()




