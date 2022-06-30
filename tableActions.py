from threading import activeCount
import pyairtable
from pyairtable import Table
from pyairtable.formulas import match
from pyairtable import Table
import requests
import datetime

with open("../Infos.txt", "r") as f:
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
            
table = Table(API_KEY, 'appHnr7cu8j1HlMC2', 'YUUMI')
table2 = Table(API_KEY, 'appHnr7cu8j1HlMC2', 'ADMIN')



def get_logins():
    account = table.first(sort=["Unban"])['fields']['Account']
    password = table.first(sort=["Unban"])['fields']['Password']
    Time = requests.get("http://worldtimeapi.org/api/timezone/Europe/Paris").json()['utc_datetime']
    for records in table.all():
        if records['fields']['Account'] == account:
            recordId = records['id']
            table.update(recordId, {"Unban": Time})
            
    return account, password


def update_admin(login):
    try:
        for records in table2.all():
            if records['fields']['PcName'] == Pc_Name:
                recordId = records['id']
                table2.update(recordId, {"ConnectedOn": login})
                #LastAction update
                Time = requests.get("http://worldtimeapi.org/api/timezone/Europe/Paris").json()['utc_datetime']
                table2.update(recordId, {"LastActionTime": Time ,"LastAction": 'Connexion'})
    except:
        print("Error when updating the table")
    