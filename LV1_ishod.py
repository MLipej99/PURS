import requests

podatci = {
    'ime': 'Martin',
    'prezime':'Lipej',
    'ip': '192.168.194.112'
}


response = requests.post('http://192.168.194.5', json=podatci)

print(response.status_code)
print(response.text)

params = {
    "id":"202"
}

response = requests.get('http://192.168.194.5/hocu_bod', params=params)
print(response.status_code)
print(response.text)
print(response.headers)


response = requests.post('http://192.168.194.5/svi_bodovi')
print(response.status_code)
print(response.text)
print(response.headers)