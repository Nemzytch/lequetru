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
    list_of_account = []
    list_of_not_available = []
    list_of_available = []
    
    for records in table.all():
        list_of_account.append(records['fields']['Account'])
        
        if records['fields']['FinishedAcc'] == "Finish" :
            list_of_not_available.append(records['fields']['Account'])
            
        if records['fields']['FinishedAcc'] == "Banned ?":
            list_of_not_available.append(records['fields']['Account'])
            
        if records['fields']['FinishedAcc'] == "En Vente":
            list_of_not_available.append(records['fields']['Account'])
        
        if records['fields']['FinishedAcc'] == "Vendu":
            list_of_not_available.append(records['fields']['Account'])
            
    for records in table2.all():
        list_of_not_available.append(records['fields']['ConnectedOn'])
    
    print("Accounts : " + str(len(list_of_account)))
    
    for element in list_of_account:
        if element not in list_of_not_available:
            list_of_available.append(element)
    
    print("Available : " + str(len(list_of_available)))

    for records in table.all(sort=["Unban"]):
        for element in list_of_available:
            if records['fields']['Account'] == element:
                recordId = records['id']
                Time = requests.get("http://worldtimeapi.org/api/timezone/Europe/Paris").json()['utc_datetime']
                table.update(recordId, {"Unban": Time})
                return records['fields']['Account'], records['fields']['Password']

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
        
        
def get_username():
    for records in table2.all():
        if records['fields']['PcName'] == Pc_Name:
            return records['fields']['ConnectedOn']
        
        
def set_blue_essence(IngameName,amount):
    for records in table.all():
        if records['fields']['IngameName'] == IngameName:
            recordId = records['id']
            table.update(recordId, {"BlueEssence": amount})


def set_skin_list(IngameName,skin_list):
    for records in table.all():
        if records['fields']['IngameName'] == IngameName:
            recordId = records['id']
            table.update(recordId, {"SkinList": skin_list})
           
            
def get_account_name(IngameName):
    for records in table.all():
        if records['fields']['IngameName'] == IngameName:
            return records['fields']['Account']
        

def set_low_priority(IngameName,low_priority):
    for records in table.all():
        if records['fields']['IngameName'] == IngameName:
            recordId = records['id']
            table.update(recordId, {"LowPriority": low_priority})
            
            
def check_ingame_name(winloss):
    for records in table.all():
        if records['fields']['WIN/LOSS'] == winloss:
            print(records['fields']['IngameName'])
            if records['fields']['IngameName'] == "None":
                return False
            
            
def set_ingame_name(IngameName,winloss):
    for records in table.all():
        if records['fields']['WIN/LOSS'] == winloss:
            recordId = records['id']
            table.update(recordId, {"IngameName": IngameName})
            return True

def get_account_connected_on():
    for records in table2.all():
        if records['fields']['PcName'] == Pc_Name:
            return records['fields']['ConnectedOn']
            
def set_banned_account():
    for records in table2.all():
        if records['fields']['PcName'] == Pc_Name:
            connected_on = records['fields']['ConnectedOn']
        
    for records in table.all():
        if records['fields']['Account'] == connected_on:
            recordId = records['id']
            table.update(recordId, {"FinishedAcc": "Banned ?"})
            