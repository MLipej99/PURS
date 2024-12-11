import requests

podatci = {
    'username': 'PURS',
    'password':'1234'
}

response = requests.post('http://192.168.194.5/login', json= podatci)
print(response.text)
print(response.status_code)


#Postavljanje pogrešne lozinke
podatci['password']='1234'

response = requests.post('http://192.168.194.5/login', json= podatci)
print(response.text)
print(response.status_code)