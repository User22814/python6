import requests
import json


headers = {
    'X-Yandex-API-Key': 'e659058a-dab4-4afe-bba3-988a4e18c4ca'
}
response = requests.get(url="https://api.weather.yandex.ru/v2/informers?lat=51.169392&lon=71.449074", headers=headers)

obj = response.json()


print(f"In Nur-Sultan at {obj['now_dt']}")
print(f"Temperature now: {obj['fact']['temp']} | Feels like: {obj['fact']['feels_like']} | "
      f"Condition: {obj['fact']['condition']}")
print(f"FORECAST:\n"
      f"{obj['forecast']['parts'][0]['part_name']}\n"
      f"Temperature min: {obj['forecast']['parts'][0]['temp_min']} | Temperature avg: {obj['forecast']['parts'][0]['temp_avg']} |"
      f" Temperature max: {obj['forecast']['parts'][0]['temp_max']}\n"
      f"{obj['forecast']['parts'][1]['part_name']}\n"
      f"Temperature min: {obj['forecast']['parts'][1]['temp_min']} | Temperature avg: {obj['forecast']['parts'][1]['temp_avg']} |"
      f" Temperature max: {obj['forecast']['parts'][1]['temp_max']}")

with open('weather.json', "w") as file:
    file.write(response.text)
