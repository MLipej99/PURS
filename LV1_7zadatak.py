import requests


response = requests.get("http://ip.jsontest.com/")

# Provjerite je li zahtjev bio uspješan
print(response.status_code)
print(response.json().get('ip'))