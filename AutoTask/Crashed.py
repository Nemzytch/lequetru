import os
import sys
import datetime
from pyairtable import Table
import requests
import pyautogui
import time

with open(r"C:\Users\Administrator\Desktop\Infos.txt", "r") as f:
    for line in f:         
        if "PC_NAME" in line:
            Pc_Name = line.strip().split(":")[1]
            print(Pc_Name)
            
        if "API_KEY" in line:
            API_KEY = line.strip().split(":")[1]
            print(API_KEY)
            
        if "BASE_ID" in line:
            BASE_ID = line.strip().split(":")[1]
            print(BASE_ID)

table2 = Table(API_KEY, 'appHnr7cu8j1HlMC2', 'ADMIN')
Time = (requests.get("http://worldtimeapi.org/api/timezone/Europe/Paris").json()['datetime']).replace("T", " ")[:-13]
    
def check_time():
    for records in table2.all():
        if records['fields']['PcName'] == Pc_Name:
                return records['fields']['Last Modified']

def check_crash(last_airtable_action):
    date_crash = datetime.datetime.strptime(last_airtable_action.replace("T", " ")[:-5], '%Y-%m-%d %H:%M:%S')
    utc_2 = date_crash + datetime.timedelta(hours=3)
    if str(Time) > str(utc_2):
        return True
    else:
        return False

def Pause():
    for records in table2.all():
        if records['fields']['PcName'] == Pc_Name:
            recordId = records['id']
            if "Status" in records['fields']:
                print("Play")
            else:
                print("Pause :(")
                time.sleep(600)
                Pause()
                
def just_restarted():         
    for records in table2.all():
        if records['fields']['PcName'] == Pc_Name:
                table2.update(records['id'], {'LastAction':'Just Restarted'})
                table2.update(records['id'], {'N.Crashed': int(records['fields']['N.Crashed'])+1})
                
def discord():
    payload = {
        'content': (Pc_Name + ' crashed at ' + check_time() + ' and restarted at '+ Time),
    }
    headers = {
        'authorization': 'MzczNTI1MDgwNzAzMjM4MTQ1.Yd1yjQ.1EIuHQh2sbo2EIK12Zgs_7djrY8'
    }
    
    (pyautogui.screenshot()).save ('photo.png')
    p = requests.post('https://discord.com/api/v9/channels/996082168411455558/messages', 
                    data=payload,headers=headers, files={'file': open('photo.png', 'rb')})
   
def restart():
    Pause()
    if check_crash(check_time())== True:
        #discord()
        just_restarted()
        print("Restarting PC")
        os.system("shutdown -r -t 0")
        sys.exit()
    else:
        print("PC is not crashed")
        
restart()