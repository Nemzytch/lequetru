import code
import requests
from requests.auth import HTTPBasicAuth
from lcu import LcuInfo
import psutil
import os
import time
import urllib3


#remove insecure request warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

for proc in psutil.process_iter():
    # check whether the process name contains the given string
    if "LeagueClientUx.exe" in proc.name() or "Riot" in proc.name() or "League" in proc.name():
      print(proc.name())
      proc.kill()
#start league of legends

os.startfile("C:\\Riot Games\\League of Legends\\LeagueClient.exe")
print("Starting League of Legends..")
time.sleep(5)

lcu_info = LcuInfo()

lcu_port = lcu_info.access_port
lcu_endpoint = f'https://127.0.0.1:{lcu_port}/rso-auth/v1/session/credentials'
lcu_password = lcu_info.remoting_auth_token
lcu_user = 'riot'


print(f'LCU Token Access: {lcu_password}.')
print(f'LCU Port: {lcu_port}.')

user_nickname = 'Yandisell'
user_password = '!DonOtEaTtheYe11OwSnow'

payload = {
  'username': user_nickname,
  'password': user_password,
  'persistLogin': False
}

response = requests.put(lcu_endpoint, json=payload, verify=False, auth=(lcu_user, lcu_password))

print(response.json())
