import requests
import json
import os
import ast

username = os.getenv('EVENG_USER')
password = os.getenv('EVENG_PASSWORD')
eveng_ip = os.getenv('EVENG_SERVER')

login_url = 'http://'+eveng_ip+'/api/auth/login'
cred = '{"username":"'+username+'","password":"'+password+'","html5":"-1"}'
headers = {'Content-type': 'application/json'}

print('Logging in...')
login = requests.post(url=login_url, data=cred)
cookies = login.cookies

print("===============================================")
print(cookies)

print("===============================================")
print("Labs:")

with open('metadata/lab-list.txt', 'r') as f:
    data_string = f.read()
    labs = ast.literal_eval(data_string)

for key, value in labs.items():
    print(key, value)

print("===============================================")
print("Images available:")

image_url = f'http://'+eveng_ip+'/api/list/templates/'
lab_images = requests.request("GET", image_url, headers=headers, cookies=cookies)
json_string = lab_images.json()

for a, data in json_string.items():
    if isinstance(data, dict):
        for b, details in data.items():
            if "missing" not in details:
                print(details)


print("===============================================")
print('Logging out...')
logout_url = 'http://'+eveng_ip+'/api/auth/logout'
logout = requests.get(url=logout_url, headers=headers, cookies=cookies)
print(logout)
