import requests
podatci={
    'temperatura':24
}

response = requests.post('http://192.168.194.5/temperatura', json=podatci)


if response.headers.get('Content-Type')=='application/text':
    print(response.text().get('temperatura'))
print(response.status_code)
print(response.text)