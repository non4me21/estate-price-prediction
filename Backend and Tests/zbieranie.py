import bs4 as bs
from selenium import webdriver
import urllib.request
from time import sleep
from pandas import DataFrame

url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/wroclaw?distanceRadius=0&market=ALL&locations=%5Bcities_6-39%5D&viewType=listing&lang=pl&searchingCriteria=sprzedaz&searchingCriteria=mieszkanie&searchingCriteria=cala-polska&page='

addresses = []
price = []
rooms = []
area = []

driver = webdriver.Safari()
for i in range(1,300):
    driver.get(url + str(i))
    sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)
    page = driver.execute_script('return document.body.innerHTML')
    soup = bs.BeautifulSoup(''.join(page), 'html.parser')
    adresses = soup.find_all('p', {"class": "css-80g06k es62z2j12"})
    other_parametres = soup.find_all('div', {"class": "css-153eqh1 eclomwz3"})
    adres = [elem.text for elem in adresses]
    addresses = addresses + adres
    for elem in other_parametres:
        params = elem.find_all('span')
        price.append(str(params[0].text).replace('zł', '').replace(' ', ''))
        rooms.append(str(params[2].text).split(' ')[0])
        area.append(float(str(params[3].text).split(' ')[0]))
    df = DataFrame({'adres': addresses,
                    'pokoje': rooms,
                    'metraz': area,
                    'cena': price})
    df = df[df.cena != 'Zapytaj o cenę']
    df.to_csv('mieszkania.csv')
    print(f'Zapisano {i}')



