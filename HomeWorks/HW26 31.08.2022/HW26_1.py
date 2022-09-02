import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}
url = "https://nationalbank.kz/ru/exchangerates/ezhednevnye-oficialnye-rynochnye-kursy-valyut"
response1 = requests.get(url=url, headers=headers)
# print(response1.text)
soup2 = BeautifulSoup(response1.text, 'html.parser')
objs3 = soup2.find_all('tr')
# objs4 = objs3[0].text.strip().split('\n')

for element in objs3:
    objs4 = element.text.strip().split('\n')
    print(f"{objs4[0]} = {objs4[2]} KZT")
