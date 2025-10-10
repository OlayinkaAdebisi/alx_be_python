import requests

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "key": "35cdc33f1843181d109362ed5a6d8ef5",
    "q": "Lagos",
    "aqi": "no"
}
response = requests.get(url, params=params)
print(response)