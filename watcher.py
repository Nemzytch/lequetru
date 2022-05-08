import os
from re import L
from sqlite3 import Time
import subprocess
import time
import datetime
import psutil
import pyairtable
import socket
from pyairtable import Table

API_KEY= "key181wgNDrYM2bms"
BASE_ID = "appHnr7cu8j1HlMC2"
table = Table(API_KEY, 'appHnr7cu8j1HlMC2', 'YUUMI')
table2 = Table(API_KEY, 'appHnr7cu8j1HlMC2', 'ADMIN')

def PussyDestroyer():
    
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

    cmdList = []

    #find all cmd.exe processes
    for _ in psutil.process_iter():
        if "cmd.exe" in _.name():
            cmdList.append(_)
            print(_.create_time())


    # sort the list by the time the process was created
    for _ in cmdList:
        for __ in cmdList:
            if _.create_time() < __.create_time():
                cmdList[cmdList.index(_)] = __
                cmdList[cmdList.index(__)] = _
    #remove first process from list


    print("cmd list avant remove: " + str(cmdList))
    cmdList.pop(0)
    print("cmd list apres remove: " + str(cmdList))


    #kill all process in cmdList with their ID
    for _ in cmdList:
        subprocess.call(["taskkill", "/F", "/PID", str(_.pid)])
        print(_)
        time.sleep(0.2)


    #start cmd.exe and run the script "watch.py"
    PathToThisFolder = os.path.dirname(os.path.abspath(__file__))
    p = subprocess.Popen(["start", "cmd", "/k", "python start.py"], cwd= PathToThisFolder, shell = True)
    

    os.startfile("C:\\Riot Games\\League of Legends\\LeagueClient.exe")
    print("Starting League of Legends..")
    time.sleep(125)
    checker()


def checker():
    for records in table2.all():
        if records['fields']['PcName'] == socket.gethostname():
            recordId = records['id']
            now = datetime.datetime.now()
            
            LastActionTime = str(records['fields']['LastActionTime'])

            #Recuperation de l'heure et minutes de Lastactiontime
            LastActionTimeHour = int(LastActionTime[11:13])
            LastActionTimeMinute = int(LastActionTime[14:16])
            
            if (now.hour - LastActionTimeHour) < 1 and (now.minute - LastActionTimeMinute) < 10:
                #difference between now and last action time
                difference = (now.hour - LastActionTimeHour) * 60 + (now.minute - LastActionTimeMinute)
                table2.update(recordId, {'Crashed': 'Depuis ' +str(difference)+ ' minutes'})
                print("Difference: " + str(difference))
                print("PussyDestroyer is not needed")
                checker()
            else:
                table2.update(recordId, {'Crashed': 'PussyDestroyer IS ON THE WAY'})
                print("PussyDestroyer IS ON THE WAY")
                PussyDestroyer()
    time.sleep(60)

checker()