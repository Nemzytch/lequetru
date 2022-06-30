from operator import contains
import requests
from lcu import LcuInfo
import psutil
import os
import time
import urllib3
import subprocess

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
  
  print(response)
  if response.status_code == 201:
    print("Got a response from Riot server.")
  if response.status_code != 201:
    print("Didnt get a positive response from Riot server.")
  if response.json()["error"] != "":
    print("Connection attempt failed.")
    print("Error :"+response.json()["error"])
    if response.json()["type"] == "needs_credentials":
      print("Invalid credentials.")
    
  

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
  print(f'Client Started: {ClientStarted}, Client UX Started: {ClientUXStarted}')
  return ClientStarted, ClientUXStarted



def stay_connected(username,password):
  ClientStarted = Connection_State()[0]
  ClientUXStarted = Connection_State()[1]
  if ClientStarted == False:
    os.startfile("C:\\Riot Games\\League of Legends\\LeagueClient.exe")
    print("Starting League of Legends..")
    time.sleep(5)
    connect(username,password)
  if ClientStarted == True and ClientUXStarted == False:
    print("Connection client started but not connected to LCU.")
    time.sleep(5)
    connect(username,password)
  if ClientStarted == True and ClientUXStarted == True:
    PussyDestroyer()
    time.sleep(1)
    stay_connected(username,password)
    
def PussyDestroyer():
  print("Pussy Destroyer")
  os.system('cls' if os.name == 'nt' else 'clear')
  procList = []

  for proc in psutil.process_iter():
      if "Riot" in proc.name():
          procList.append(proc.name())
  for proc in psutil.process_iter():
      if "League" in proc.name():
          procList.append(proc.name())
          
  for _ in procList:
      subprocess.call(["taskkill", "/F", "/IM", _])
      time.sleep(0.1)
  time.sleep(1)
  



