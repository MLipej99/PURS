import requests 

response = requests.get('http://192.168.194.5/login')
print(response.text)
print(response.status_code)
print(response.headers)