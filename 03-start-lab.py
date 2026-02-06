import requests
import json
import os
import ast

username = os.getenv('EVENG_USER')
password = os.getenv('EVENG_PASSWORD')
eveng_ip = os.getenv('EVENG_SERVER')

print("===============================================")
print('Logging in...')

login_url = 'http://'+eveng_ip+'/api/auth/login'
cred = '{"username":"'+username+'","password":"'+password+'","html5":"-1"}'
headers = {'Content-type': 'application/json'}
login = requests.post(url=login_url, data=cred)
cookies = login.cookies

print("===============================================")
print("Please choose the lab number you start")
print("===============================================")

with open('metadata/lab-list.txt', 'r') as f:
    data_string = f.read()
    labs = ast.literal_eval(data_string)

for key, value in labs.items():
    print(key, value)
print("===============================================")
lab_number = int(input("Enter the lab number: "))
print("===============================================")

if lab_number in labs:
    print(lab_number)

# print("Starting lab 1-Base-Template.unl")
# lab_url = f'http://'+eveng_ip+'/api/labs/1-Base-Template.unl/nodes/1/start'
# start_lab = requests.request("GET", lab_url, headers=headers, cookies=cookies)
# print(start_lab.json())

print('Logging out...')
logout_url = 'http://'+eveng_ip+'/api/auth/logout'
logout = requests.get(url=logout_url, headers=headers, cookies=cookies)