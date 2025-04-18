import requests
from IPython.display import clear_output
import time
while True:
    apiKey='b1f4ec0a86974bafb71124001240312'
    city = 'Tashkent'
    city2='London'
    url = f'http://api.weatherapi.com/v1/current.json?key={apiKey}&q={city}&aqi=no'
    url2 = f'http://api.weatherapi.com/v1/current.json?key={apiKey}&q={city2}&aqi=no'
    response = requests.get(url)
    response2 = requests.get(url2)
    data = response.json()
    data2=response2.json()
    from datetime import datetime
    import pytz

    local = datetime.now()

    tz_NY = pytz.timezone('Europe/London')
    datetimeNY = datetime.now(tz_NY)
    time.sleep(1)
    print(f'''Weather in Tashkent {data['current']['condition']['text']}\n Temperature : {data['current']['temp_c']}\n
    Weather in London {data2['current']['condition']['text']}\n Temperature : {data2['current']['temp_c']}\n
    Current Time in Tashkent {local}  | Current Time in London {datetimeNY}''')
    clear_output(wait=True)
#######################################################################################
import bs4 as d
import requests as f
import json

all_data = []
l=[]

for i in range(1, 8):
    url = f'https://damda.uz/en/dacha?cursor={i}'
    l.append(url)
for k in l:
    page = f.get(k)
    soup = d.BeautifulSoup(page.text, 'html.parser')
 
    listings = soup.find_all('div', class_='MuiGrid-root MuiGrid-container MuiGrid-item MuiGrid-spacing-xs-3 MuiGrid-grid-xs-12 MuiGrid-grid-md-9 css-p33wqu')


    for item in listings:
        try:
            title = item.find_all('h2', class_="MuiTypography-root MuiTypography-h2 css-1utvxnj").text.strip()
            location = item.find_all('div', class_='hotelCard_subtitle__tfpNB').text.strip()
            price = item.find_all('p', class_='hotelCard_price__Zwvon').text.strip()
            print(title)
            all_data.append({
                'title': title,
                'location': location,
                'price': price
            })
        except Exception as e:
            print(f'Error while parsing item: {e}')
print(listings)
with open('dacha_listings.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=4)
###########################################################################################################################

  


