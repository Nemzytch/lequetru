from threading import activeCount
from turtle import Screen
from cv2 import add
from matplotlib import image
import pyairtable
from pyairtable import Table
import requests
import time
import pyautogui
import datetime

with open("../../Infos.txt", "r") as f:
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

def check_time():
    for records in table2.all():
        if records['fields']['PcName'] == Pc_Name:
                return records['fields']['Last Modified']

def check_crash(last_airtable_action):
    date_crash = datetime.datetime.strptime(last_airtable_action.replace("T", " ")[:-5], '%Y-%m-%d %H:%M:%S')
    utc_2 = date_crash + datetime.timedelta(hours=3)
    if datetime.datetime.now() > utc_2:
        return True
    else:
        return False

def just_restarted():
    for records in table2.all():
        if records['fields']['PcName'] == Pc_Name:
                table2.update(records['id'], {'LastAction':'Just Restarted'})
