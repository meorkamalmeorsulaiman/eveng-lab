import requests
import json
import os
import ast

def lab_nodes(lab_name):

    lab_url = f'http://'+eveng_ip+'/api/labs/'+lab_name+'.unl/nodes'
    get_lab_nodes = requests.request("GET", lab_url, headers=headers, cookies=cookies)
    json_string = get_lab_nodes.json()
    for a, data in json_string.items():
        if isinstance(data, dict):
            for nodes, details in data.items():
                print("Id:", details['id'], "-", details['name'], "-", details['template'], "-", details['url'], "State:", details['status'])

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
print("Please choose the lab nodes you want to list")
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
    lab_nodes(labs[lab_number])

print("===============================================")
print('Logging out...')
print("===============================================")
logout_url = 'http://'+eveng_ip+'/api/auth/logout'
logout = requests.get(url=logout_url, headers=headers, cookies=cookies)

