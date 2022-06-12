from operator import contains
import requests
from lcu import LcuInfo
import psutil
import os
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def Started_Client():
  ClientStarted = False
  ClientUXStarted = False
  for proc in psutil.process_iter():
    if "LeagueClientUx.exe" in proc.name():
      ClientUXStarted = True
      print(f'Process: {proc.name()}')
    if "Riot" in proc.name():
      print(f'Process: {proc.name()}')
      ClientStarted = True
  if ClientStarted and ClientUXStarted == True:
    print('Connected to LCU.')
  if ClientStarted == False:
    os.startfile("C:\\Riot Games\\League of Legends\\LeagueClient.exe")
    print("Starting League of Legends..")
    time.sleep(5)

Started_Client()


def get_lcu_info(username,password):
  lcu_info = LcuInfo()
  lcu_port = lcu_info.access_port
  lcu_endpoint = f'https://127.0.0.1:{lcu_port}/rso-auth/v1/session/credentials'
  lcu_password = lcu_info.remoting_auth_token
  lcu_user = 'riot'


  print(f'LCU Token Access: {lcu_password}.')
  print(f'LCU Port: {lcu_port}.')

  user_nickname = 'Erenamur3'
  user_password = '!DonOtEaTtheYe11OwSnow'

  payload = {
    'username': user_nickname,
    'password': user_password,
    'persistLogin': False
  }

  response = requests.put(lcu_endpoint, json=payload, verify=False, auth=(lcu_user, lcu_password))

  print(response.json())





