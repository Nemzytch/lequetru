import requests
from pyairtable import Table

#get the time whit World Time API for europe paris and print it in the console
#"http://worldtimeapi.org/api/timezone/Europe"


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


time = requests.get("http://worldtimeapi.org/api/timezone/Europe/Paris").json()['utc_datetime']
print(time)

for records in table2.all():
    if records['fields']['PcName'] == Pc_Name:
        recordId = records['id']
        table2.update(recordId, {"LastActionTime": time,"LastAction": 'Connexion'})