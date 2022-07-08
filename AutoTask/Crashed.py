import os
import sys
import datetime
from pyairtable import Table
#C:\Users\Administrator\Desktop\Infos.txt
with open("C:\Users\Administrator\Desktop\Infos.txt", "r") as f:
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
            
def restart():
    if check_crash(check_time())== True:
        just_restarted()
        print("Restarting PC")
        os.system("shutdown -r -t 0")
        sys.exit()
    else:
        print("PC is not crashed")
        
restart()