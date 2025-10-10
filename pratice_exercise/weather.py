import requests

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "key": "",
    "q": "Lagos",
    "aqi": "no"
}
response = requests.get(url, params=params)
print(response)
