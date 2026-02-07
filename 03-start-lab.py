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
                print("Id:", details['id'], "-", details['name'], "-", details['template'], "-", details['url'])

def start_lab_node(lab_name, node_id):

    node_id_to_str = node_id = str(node_id)
    lab_url = f'http://'+eveng_ip+'/api/labs/'+lab_name+'.unl/nodes/'+node_id_to_str+'/start'
    start_lab_node = requests.request("GET", lab_url, headers=headers, cookies=cookies)
    print(start_lab_node.json())

username = os.getenv('EVENG_USER')
password = os.getenv('EVENG_PASSWORD')
eveng_ip = os.getenv('EVENG_SERVER')

print("==============")
print('Logging in...')

login_url = 'http://'+eveng_ip+'/api/auth/login'
cred = '{"username":"'+username+'","password":"'+password+'","html5":"-1"}'
headers = {'Content-type': 'application/json'}
login = requests.post(url=login_url, data=cred)
cookies = login.cookies

print("===========================================================================================")
print("Do you want to start whole nodes in the lab or individual node? whole (A) or individual (B)")
print("===========================================================================================")
start_options = str(input("whole (A) or individual (B): "))

if start_options == "B" or start_options == "b":

    print("===============================================")
    print("Please select which lab you want to start")
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
        
        print("==================================================")
        node_id = int(input("Please select the node Id that you want to start: "))
        print("==================================================")

        start_lab_node(labs[lab_number], node_id)



# print("Starting lab 1-Base-Template.unl")
# lab_url = f'http://'+eveng_ip+'/api/labs/1-Base-Template.unl/nodes/1/start'
# start_lab = requests.request("GET", lab_url, headers=headers, cookies=cookies)
# print(start_lab.json())

print("===============================================")
print('Logging out...')
print("===============================================")
logout_url = 'http://'+eveng_ip+'/api/auth/logout'
logout = requests.get(url=logout_url, headers=headers, cookies=cookies)