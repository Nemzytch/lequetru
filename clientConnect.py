from operator import contains
import requests
from lcu import LcuInfo
import psutil
import os
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def connect(username,password):
  lcu_info = LcuInfo()
  lcu_port = lcu_info.access_port
  lcu_endpoint = f'https://127.0.0.1:{lcu_port}/rso-auth/v1/session/credentials'
  lcu_password = lcu_info.remoting_auth_token
  lcu_user = 'riot'
  
  print(f'LCU Token Access: {lcu_password}.')
  print(f'LCU Port: {lcu_port}.')

  payload = {
    'username': username,
    'password': password,
    'persistLogin': False
  }
  response = requests.put(lcu_endpoint, json=payload, verify=False, auth=(lcu_user, lcu_password))
  #print the complete request
  print("request: ", response.request.body)
  print(response)
  print(response.json())

def Connection_State():
  ClientStarted = False
  ClientUXStarted = False
  
  for proc in psutil.process_iter():
    if "LeagueClientUx.exe" in proc.name():
      ClientUXStarted = True
      # print(f'Process: {proc.name()}')
    if "Riot" in proc.name():
      # print(f'Process: {proc.name()}')
      ClientStarted = True
  return ClientStarted, ClientUXStarted



def stay_connected(username,password):
  print("hello from stay connected")
  print("username: ", username)
  print("password: ", password)
  ClientStarted = Connection_State()[0]
  ClientUXStarted = Connection_State()[1]
  if ClientStarted == False:
    os.startfile("C:\\Riot Games\\League of Legends\\LeagueClient.exe")
    print("Starting League of Legends..")
    time.sleep(15)
    connect(username,password)
  if ClientStarted == True and ClientUXStarted == False:
    print("Connection client started but not connected to LCU.")
    time.sleep(5)
    connect(username,password)
  if ClientStarted == True and ClientUXStarted == True:
    print("Connected to LCU, chill.")
    time.sleep(5)
    







