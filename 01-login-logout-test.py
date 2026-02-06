import requests
import os

username = os.getenv('EVENG_USER')
password = os.getenv('EVENG_PASSWORD')
eveng_ip = os.getenv('EVENG_SERVER')

login_url = 'http://'+eveng_ip+'/api/auth/login'
cred = '{"username":"'+username+'","password":"'+password+'","html5":"-1"}'
headers = {'Content-type': 'application/json'}

print('Logging in...')
login = requests.post(url=login_url, data=cred)
cookies = login.cookies
print(cookies)
        
print('Logging out...')
logout_url = 'http://'+eveng_ip+'/api/auth/logout'
logout = requests.get(url=logout_url, headers=headers, cookies=cookies)
print(logout)
