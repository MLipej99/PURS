import requests

params = {
    'id':26
}

response = requests.delete('http://192.168.194.5/temperatura', params=params)
print(response.status_code)
print(response.text)