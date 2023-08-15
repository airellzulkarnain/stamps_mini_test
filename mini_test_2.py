import urllib.request
import json
from datetime import datetime


key = 'a826c9766973e99eec201a76a009583e'
req = urllib.request.Request(f'http://api.openweathermap.org/geo/1.0/direct?q=Jakarta&limit=1&appid={key}', method='GET')
with urllib.request.urlopen(req) as response:
    res = json.loads(response.read().decode('utf-8'))

lat = res[0]['lat']
lon = res[0]['lon']

req = urllib.request.Request(f'https://api.openweathermap.org/data/2.5/forecast?units=metric&lat={lat}&lon={lon}&appid={key}', method='GET')
with urllib.request.urlopen(req) as response:
    res = json.loads(response.read().decode('utf-8'))

forecast5 = dict()
for r in res['list']:
    forecast5[f'{datetime.fromtimestamp(r["dt"]).strftime(r"%a, %d %b %Y")}'] = f'{r["main"]["temp"]}°C'

print("Weather Forecast:")
print(*[f'{k}: {v}' for k, v in forecast5.items()], sep='\n')
