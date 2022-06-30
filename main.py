import logging
import os
import re
import sys
import cv2
import time
import json
import math
from cv2 import phase
import mouse 
import socket
import random
import urllib3
import datetime
import win32api
import win32con
import requests
import pyautogui
import numpy as nm
import pydirectinput
from time import sleep
from logging import info
from PIL import ImageGrab
from pyairtable import Table
from base64 import b64encode 
from cv2 import validateDisparity
from pyairtable.formulas import match
from colorama import Fore, Back, Style
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError
from requests.packages.urllib3.util.retry import Retry
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import subprocess
import pyperclip
import psutil
import capture
import mss
from PIL import Image
from PIL import ImageGrab
from mss import mss
import mouse
import ctypes
import inGameChecks
import shop_actions
import clientConnect
import tableActions

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



#__________ SCREEN ELEMENT __________________
user32 = ctypes.windll.user32
screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)
height = 768
width = 1024
top =int((screenHeight-height)/2)
left = int((screenWidth-width)/2)
mon = {'top': top, 'left':left, 'width':width, 'height':height}
sct = mss()
sct_img = sct.grab(mon)



#___________ UI ELEMENTS ____________________
adcHp75Pixel =[1005+left,447+top]
adcHp50Pixel = [991+left,447+top]
ePosition = [481+left,724+top]

gamedirs = [r'C:\Games\Garena\32787\LeagueClient',r'D:\Games\League of Legends',r'C:\Riot Games\League of Legends']
os.system("")
lastMessageChampSelect = datetime.datetime.now() - datetime.timedelta(minutes=4)


OneMinute= 900
saved_time = datetime.datetime.now()
Action = "Waiting"

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

PhaseNumber = 0
Lastphase = "Nothing"

def restart():
    subprocess.call(["git", "reset", "--hard", "HEAD"])
    subprocess.call(["git", "pull"])
    logging.info("Restarting")
    print("argv was",sys.argv)
    print("sys.executable was", sys.executable)
    print("restart now")

    os.execv(sys.executable, ['python'] + sys.argv)

def PussyDestroyer():
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
    time.sleep(3)
    os.startfile("C:\\Riot Games\\League of Legends\\LeagueClient.exe")
    print("Starting League of Legends..")
    time.sleep(25)
    restart()
def Pause():
    for records in table2.all():
        if records['fields']['PcName'] == Pc_Name:
            recordId = records['id']
            if "Status" in records['fields']:
                print("Play")

            else:
                print("Pause :(")
                time.sleep(10)
                Pause()
def ConfigSetup():
    #Change permissions to be safe
    for f in os.listdir("C:\Riot Games\League of Legends\Config"):
        os.chmod(os.path.join("C:\Riot Games\League of Legends\Config", f), 0o777)
    #replace file in Our "Config" with file in LOL "Config"
    for filename in os.listdir("Config"):
        src = os.path.join("Config", filename)
        dst = os.path.join("C:\Riot Games\League of Legends\Config", filename)
        os.replace(src, dst) 
        
    print('Config Set')
            
def fetchDatas():
    response = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify = False).text
    # with open("data.json", "w") as f:
    #     f.write(response)

    return json.loads(response)

def MouseClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
    
class Personnage:
    user32 = ctypes.windll.user32
    screenWidth = user32.GetSystemMetrics(0)
    screenHeight = user32.GetSystemMetrics(1)

    height = 768
    width = 1024
    top =int((screenHeight-height)/2)
    left = int((screenWidth-width)/2)
    
    account = None
    fullApiAccess = False
    # Yuumi    
    team = None
    index = None
    yuumiState = None
    teamState = None
    WName = None
    attached = None


    YuumiLevel = None
    datas = None
    hp = None
    position = None

    Team = None
    BaseX = None
    BaseY = None
    stuff = None
    gold = None
    yuumiItems = None
    nombreItems = None
    yuumiMana = None
    resourceMax = None
    passiveCooldown = None
    
    ennemyPosition = [400,400]

    atHome = None
    ultimateCooldown = 1
    qspellCooldown = 1
    ennemy = None
    backCooldown = 1
    healCooldown = 1
    qX = 1
    qY = 1

    # Taxi     
    toplanerTimer = None
    adcDead = False
    jungleDead = None
    midDead = None
    topDead = None
    yuumiIndex = 4
    adcIndex = 3
    midIndex = 2
    jungleIndex = 1
    topIndex = 0
    carryHP =None
    # adcName = None

    adcPicture = [1005+left,447+top]
    midHp75pixel = [928+left,448+top]
    jungleHp75Pixel = [858+left,448+top]
    topHp75Pixel = [1001+left,493+top]
    redBase = [1001+left,493+top]
    blueBase = [754+left,740+top]
        
    randx = random.random()


    # GENERIC FUNCTIONS      
    def setup(self):                    
        self.updateDatas()
        i=0
        while not "gameData" in self.datas:
            time.sleep(0.2)
            self.updateDatas()
        while self.datas["gameData"]["gameTime"] < 2:
            time.sleep(0.2)
            self.updateDatas()
            print("Loading Screen")
        print("Game just started")
        try:
            for records in table2.all():
                if records['fields']['PcName'] == Pc_Name:
                    recordId = records['id']
                    Time = requests.get("http://worldtimeapi.org/api/timezone/Europe/Paris").json()['utc_datetime']
                    table2.update(recordId, {"LastActionTime": Time ,"LastAction": "InGame" })
        except:
            print("Can not update the table")
            
        with open('stuff.json',) as f:
            self.stuff = json.load(f)
        print('stuff loaded')
        i=0

        for x in self.datas["allPlayers"]:

            if x["championName"] == "Yuumi":
                print(f'Found it in the {str(i)} th index')
                self.yuumiIndex = i
                self.adcIndex = i-1
                self.midIndex = i-2
                self.jungleIndex = i-3
                self.topIndex = i-4
                print(self.adcIndex)
                team= math.ceil((i+1)/(len(self.datas["allPlayers"])/2))

                self.toplanerTimer = random.randint(900, 1300)
                #click middle of the screen
                mouse.move(self.screenWidth/2, self.screenHeight/2)
                MouseClick()
                time.sleep(0.5)
                
                pydirectinput.press('space')
                time.sleep(0.5)
                if inGameChecks.inBase() == True:
                    shop_actions.updateItemList()
                    shop_actions.updateItemList()
                list1 = [('glhf'), ('have fun'), ('good luck'), ('')]
                pydirectinput.press('enter')
                time.sleep(0.2)
                pydirectinput.write(random.choice(list1))
                time.sleep(0.2)
                pydirectinput.press('enter')

                self.passiveCooldown = time.time()

                if team ==1:
                    self.Team = 'Blue'
                    self.BaseX = self.blueBase[0]
                    self.BaseY = self.blueBase[1]
                    self.qX = 1250
                    self.qY = 100
                    print(self.Team)
                if team ==2:
                    self.team = 'Red'
                    self.BaseX = self.redBase[0]
                    self.BaseY = self.redBase[1]
                    self.qX = 450
                    self.qY = 350
                    print(self.Team)
                else:
                    print(str(i))
                break
            else:
                i=i+1
    
    def shop(self):
        shop_actions.updateItemList()

    def __init__(self):
        # try self.setup and selt.start()
        try :
            self.setup()
            self.start()
        except Exception as e:
            print(e)
            print('Error in the init')
            self.setup()
            self.start()

    def updateDatas(self):
        self.datas = fetchDatas()

    def start(self):
                        
        while self.datas["gameData"]["gameTime"] < 3600:
            
            try: 
                self.updateDatas()
                self.updatePerso()
                self.LevelUP()
            except Exception as e:
                print(e)
                print('Error in the start')
                self.updateDatas()
                self.updatePerso()
                self.LevelUP()
            # self.Surrender()
            self.randx = random.random()

            if self.randx >0.96:
                mouse.move(960,480)
                pydirectinput.press('esc')
                MouseClick()

            if self.adcDead == False and self.attached == False and self.yuumiMana < self.resourceMax:
                if inGameChecks.inBase() == True:
                    self.shop()
                self.updateDatas()
                self.updatePerso()

            if self.adcDead == False and self.attached == False:
                print('Going to adc')
                mouse.move(self.adcPicture[0],self.adcPicture[1])
                pydirectinput.press('w')
            if self.attached == True:
                print('Attached')
                inGameChecks.attached(self.yuumiState["abilities"]["Q"]["abilityLevel"])
                self.Surrender()

                if self.yuumiMana < (15*(self.resourceMax)/100):
                    print(f'you got {str(self.yuumiMana)}')
                    self.procPassive()


            if self.adcDead == True:
                if self.datas["gameData"]["gameTime"] > 600:
                    if self.jungleDead == False:
                        pyautogui.click(self.jungleHp75Pixel[0],self.jungleHp75Pixel[1]) 
                        for _ in range(3):
                            time.sleep(0.2)                   
                            pydirectinput.press('w')  
                            print('going to jungler')
                        time.sleep(3)
                        pydirectinput.press('e')
                        time.sleep(9)
                        pydirectinput.press('e')
                        mouse.move(400,400)
                        pydirectinput.press('w')

                    if self.jungleDead == True:
                        if self.midDead == False:
                            pyautogui.click(self.midHp75pixel[0],self.midHp75pixel[1])
                            for _ in range(3):
                                time.sleep(0.2)                     
                                pydirectinput.press('w')  
                                print('going to midlaner')
                            time.sleep(3)
                            pydirectinput.press('e')
                            time.sleep(9)
                            pydirectinput.press('e')
                            mouse.move(400,400)
                            pydirectinput.press('w')
                        if self.midDead == True:
                            if self.topDead == False:
                                pyautogui.click(self.topHp75Pixel[0],self.topHp75Pixel[1])
                                for _ in range(3):
                                    time.sleep(0.2)                     
                                    pydirectinput.press('w')  
                                    print('going to toplaner')
                                time.sleep(3)
                                pydirectinput.press('e')
                                time.sleep(9)
                                pydirectinput.press('e')
                                mouse.move(400,400)
                                pydirectinput.press('w')
                            if self.topDead == True:
                                print('going back to base')  

                if time.time()> (self.backCooldown+50):
                    # Action = "Going back"
                    # LastAction()
                    mouse.move(self.BaseX,self.BaseY)
                    time.sleep(0.2)
                    MouseClick()
                    pydirectinput.press('h')
                    print('going back to base')
                    time.sleep(1.5)
                    MouseClick()
                    pydirectinput.press('h')
                    time.sleep(4)
                    pydirectinput.press('b')
                    time.sleep(9)
                    self.backCooldown = time.time()
                    if inGameChecks.inBase() == True:
                        self.shop()

            time.sleep(0.5)

    def updatePosition(self):
        self.position = [self.datas.posX, self.datas.posY]


    def ctrlt(self):
        pydirectinput.keyDown('ctrl')
        pydirectinput.press(self)
        pydirectinput.keyUp('ctrl')


    def procPassive(self): 
        user32 = ctypes.windll.user32
        screenWidth = user32.GetSystemMetrics(0)
        screenHeight = user32.GetSystemMetrics(1)
        height = 768
        width = 1024
        top =int((screenHeight-height)/2)
        left = int((screenWidth-width)/2)

        mon = {'top': top, 'left':left, 'width':width, 'height':height}
        sct = mss()
        sct_img = sct.grab(mon)
        if time.time() > (self.passiveCooldown +10):
            try:
                Ennemies = capture.locate_img("ennemi.png")
                if Ennemies[0] > -40 and Ennemies[0] < 1880 and Ennemies[1] > -100 and Ennemies[1] < 980:
                    mouse.move(Ennemies[0]+40, Ennemies[1]+100)
                self.ennemyPosition = [Ennemies[0], Ennemies[1]]
                pydirectinput.press('w')
                MouseClick()
                pydirectinput.press('h')    

                mouse.move(self.adcPicture[0],self.adcPicture[1])
                time.sleep(0.2)
                time.sleep(0.1)
                pydirectinput.press('w')
                self.passiveCooldown = time.time()
            except TypeError:
                print("No ennemies found")

    def Surrender(self):  
        global OneMinute
        if self.datas["gameData"]["gameTime"] > OneMinute:
            Surrend = pyautogui.locateOnScreen("images/Surrend.png", grayscale=False,confidence=0.80, region =())
            OneMinute=OneMinute+20
            try:
                if Surrend != None:
                    pydirectinput.press('enter')
                    time.sleep(0.1)
                    pyautogui.write('/ff')
                    time.sleep(0.1)
                    pydirectinput.press('enter')
                    print('I am surrending')
            except Exception:
                print('No surrend detected')
        else:
            print('Not Time to Surrender')
                    
    def LevelUP(self):
            # MaxA = ["Z","A","E","A","E","A","R","E","A","E","A","R","E","E","Z","Z","R","Z","Z"]
        levelUpOrder = ["W","E","Q","E","Q","E","R","E","Q","E","Q","R","Q","Q","W","W","R","W","W"]
        spellToUp = levelUpOrder[self.YuumiLevel]
        desiredSpellLevel = levelUpOrder[:self.YuumiLevel+1].count(spellToUp)
        if self.yuumiState["abilities"][spellToUp]["abilityLevel"] < desiredSpellLevel:
            keyTo_Press = spellToUp
            pydirectinput.keyDown('ctrl')
            pydirectinput.press(keyTo_Press.lower())
            pydirectinput.keyUp('ctrl')

    def updatePerso(self):
        self.yuumiState = self.datas["activePlayer"]
        self.teamState = self.datas["allPlayers"]
        self.WName = self.yuumiState["abilities"]["W"]["displayName"]
        if self.WName == "Change of Plan":
            self.attached = True
        else: 
            self.attached = False
        self.YuumiLevel = self.yuumiState["level"]
        self.adcDead = self.teamState[self.adcIndex]["isDead"]
        self.jungleDead = self.teamState[self.jungleIndex]["isDead"]
        self.midDead = self.teamState[self.midIndex]["isDead"]
        self.topDead = self.teamState[self.topIndex]["isDead"]
        self.gold = self.yuumiState["currentGold"]
        self.yuumiItems = self.teamState[self.yuumiIndex]["items"]
        self.nombreItems = len(self.yuumiItems)
        self.yuumiMana = self.yuumiState["championStats"]["resourceValue"]
        self.resourceMax = self.yuumiState["championStats"]["resourceMax"]

        self.action()

    def action(self):
        return False

def Connexion():  # sourcery skip: low-code-quality
    print("entered connexxoin")
    try :
        clientConnect.stay_connected()
        #get last connected account from lastConnectedAcc.txt

        gamedirs = [r'C:\Riot Games\League of Legends',r'D:\Games\League of Legends',r'D:\Riot Games\League of Legends',] 
        lockfile = None
        while not lockfile:
            for gamedir in gamedirs:
                lockpath = r'%s\lockfile' % gamedir

                if not os.path.isfile(lockpath):
                    print("Waiting League to start")
                    time.sleep(5)
                    continue
                    
                print('Found running League of Legends, dir', gamedir, "sleeping 10 sec to make sure everything loaded")
                time.sleep(10)
                lockfile = open(r'%s\lockfile' % gamedir, 'r')
        try:
            for records in table2.all():
                if records['fields']['PcName'] == Pc_Name:
                    recordId = records['id']
                    table2.update(recordId, {"ConnectedOn": Personnage.account})
                    #LastAction update
                    Time = requests.get("http://worldtimeapi.org/api/timezone/Europe/Paris").json()['utc_datetime']
                    table2.update(recordId, {"LastActionTime": Time ,"LastAction": 'Connexion'})
        except:
            print("Error when updating the table")

                
    except:
        print("Error when connecting")
        Connexion()
    ConfigSetup()  
class lobby():
    username = 'riot'
    champion = 350 
    host = '127.0.0.1'
    protocol = 'https'
    gamedirs = [r'C:\Riot Games\League of Legends',r'D:\Games\League of Legends',r'D:\Riot Games\League of Legends',]
    lockfile = None
    Connexion()
    print('We are in lobby class waiting')
    
    while not lockfile:
        for gamedir in gamedirs:
            lockpath = r'%s\lockfile' % gamedir
            if not os.path.isfile(lockpath):
                print("waiting for League to start")
                continue
            print('Found running League of Legends, dir', gamedir)
            lockfile = open(r'%s\lockfile' % gamedir, 'r')
           

    lockdata = lockfile.read()
    lockfile.close()
    lock = lockdata.split(':')
    procname = lock[0]
    pid = lock[1]
    protocol = lock[4]
    host = '127.0.0.1'
    port = lock[2]
    username = 'riot'
    password = lock[3]
    print(port,password)

def statuscheck():
    os.system('cls' if os.name == 'nt' else 'clear')
    Riot_adapter = HTTPAdapter(max_retries=1)   
    session = requests.Session()
    session.mount('https://127.0.0.1:2999/liveclientdata/allgamedata', Riot_adapter)

    print('status check')
    try:
        session.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify = False)
        print("Avant Chargement")
        time.sleep(1)
        perso = Personnage()
    except ConnectionError as ce:
        print("you aren't in game")

    print(' connecting to port '+str(lobby.port)+' with the password' +str(lobby.password)+ ' we will lock champ #'+ str(lobby.champion))

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Helper function
    def request(method, path, query='', data=''):
        url = f'{lobby.protocol}://{lobby.host}:{lobby.port}{path}?{query}' if query else f'{lobby.protocol}://{lobby.host}:{lobby.port}{path}'

        print(f"{method.upper().ljust(7, ' ')} {url} {data}")

        fn = getattr(s, method)

        return fn(url, verify=False, headers=headers, json=data) if data else fn(url, verify=False, headers=headers)

    userpass = b64encode(bytes('%s:%s' % (lobby.username, lobby.password), 'utf-8')).decode('ascii')
    headers = { 'Authorization': 'Basic %s' % userpass }
    print(headers['Authorization'])

    s = requests.session()# Create Request session

    while True: # # Main worker loop
        
        def PhaseBlock():
            global PhaseNumber # Vaut 0 a la base 
            global Lastphase # Vaut "Nothing" a la base

            if phase != Lastphase: # si c'est pas la meme Phase que la derniere fois ca veut dire que c'est passée à autre chose

                Lastphase = phase 
                PhaseNumber = 0 
                print('reset Lastphase to phase and reset PhaseNumber to 0')

            else: # si c'est la meme Phase que la derniere fois ca veut dire que c'est pas passée à autre chose et on check si ca recommence plus de 10 fois
                
                PhaseNumber = PhaseNumber + 1 # Rajoute 1 pour chaque meme phase
                if PhaseNumber >= 10: 
                    print(f"{phase} phase time to run pussy destroyer")
                    print(PhaseNumber)
                    PussyDestroyer()
                else:
                    print(phase+ "  phase tout est ok pour l'instant")
                    print(PhaseNumber)
                    
        r = 'Not connected yet'
        try :
            accid = request('get', '/lol-login/v1/session').json()['accountId']
            r = request('get', '/lol-gameflow/v1/gameflow-phase')
            if r.status_code != 200:
                print(Back.BLACK + Fore.RED + str(r.status_code) + Style.RESET_ALL, r.text)
                continue
            print(Back.BLACK + Fore.GREEN + str(r.status_code) + Style.RESET_ALL, r.text)
        except:
            print('cant get phase yes')
            time.sleep(3)
        phase = r.json()

        def LastAction():
            global saved_time
            try:
                current_time = datetime.datetime.now()
                if (current_time - saved_time).seconds >= 15:
                    Time = requests.get("http://worldtimeapi.org/api/timezone/Europe/Paris").json()['utc_datetime']
                    SummonerName = request('get', '/lol-summoner/v1/current-summoner').json()["displayName"]
                    for records in table2.all():
                        if records['fields']['PcName'] == Pc_Name:
                            recordId = records['id']
                            table2.update(recordId, {"LastActionTime": Time ,"LastAction": phase})
                    
                    for records in table.all():
                        if records['fields']['IngameName'] == SummonerName:
                            recordId = records['id']
                            table.update(recordId, {"Unban": Time})
                    
                            saved_time = datetime.datetime.now()
            except:
                print('Error when updating the table')
                        
        def Refund():
            idtoken = request('get', '/lol-login/v1/session').json()['idToken']     
             
            def getrequest(url):
                auth = f'Bearer {idtoken}'
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': auth
                }
                return requests.get(url, headers=headers)
            
            def PostRequest(url, data):
                auth = f'Bearer {idtoken}'

                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': auth
                }
                return requests.post(url, data=json.dumps(data), headers=headers, verify=False)
            accid = request('get', '/lol-login/v1/session').json()['accountId']
            StoreUrl = request('get', '/lol-store/v1/getStoreUrl').json()
            transactions = getrequest('https://euw.store.leagueoflegends.com/storefront/v3/history/purchase').json()['transactions']
            
            for champs in transactions:
                if champs['itemId'] == 350:
                    if champs['refundable'] == True:
                        TransacID = champs['transactionId']
                        print(TransacID)
                        Refund = PostRequest( str(StoreUrl)+'/storefront/v3/refund', data=({"accountId":accid ,"transactionId":TransacID ,"inventoryType":"CHAMPION","language":"en_GB"})) 
                                       
        def Store():
            idtoken = request('get', '/lol-login/v1/session').json()['idToken']
            accid = request('get', '/lol-login/v1/session').json()['accountId']
            print(accid, "acc id is here")
            StoreUrl = request('get', '/lol-store/v1/getStoreUrl').json()
            TransacHistory = request('get', '/lol-store/v1/transaction/history').json()

            ChampionsCollection = request('get', '/lol-champions/v1/inventories/' + str(accid) + '/champions-playable-count').json()['championsOwned']
            print(ChampionsCollection)
                                        
            def PostRequest(url, data):
                auth = f'Bearer {idtoken}'

                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': auth
                }
                return requests.post(url, data=json.dumps(data), headers=headers, verify=False)
            
            champIDListCheap = [32,1,22,36,86,10,11,20,78,13,27,15,16,19]
            ChampIDListLessCheap = [44,17,18,23]

            for champID in champIDListCheap: 
                BoughtChampion = PostRequest( str(StoreUrl)+'/storefront/v3/purchase', data=({"accountId":accid,"items":[{"inventoryType":"CHAMPION","itemId":champID,"ipCost":450,"quantity":1}]}))
                print(BoughtChampion.json())
                time.sleep(1)
                
            for champID in ChampIDListLessCheap:
                BoughtChampion = PostRequest( str(StoreUrl)+'/storefront/v3/purchase', data=({"accountId":accid,"items":[{"inventoryType":"CHAMPION","itemId":champID,"ipCost":1350,"quantity":1}]}))
                print(BoughtChampion.json())
                time.sleep(1)
            BoughtChampion = PostRequest( str(StoreUrl)+'/storefront/v3/purchase', data=({"accountId":accid,"items":[{"inventoryType":"CHAMPION","itemId":350,"ipCost":6300,"quantity":1}]}))
        
        if phase == 'Not connected yet':
            print("You are not connected yet")
            PhaseBlock()
        if phase =='WaitingForStats':
            print("you are in WaitingForStats phase")
            PhaseBlock()
        if phase =='PreEndOfGame':
            PhaseBlock()
            LastAction()
            try :
                puuid = request('get', '/lol-summoner/v1/current-summoner').json()['puuid']
                ActualGameId = request('get', '/lol-match-history/v1/products/lol/'+puuid+'/matches').json()['games']['games'][0]['gameId']
                for records in table2.all():
                    if records['fields']['PcName'] == Pc_Name:
                        recordId = records['id']
                        if records['fields']['LastGameId'] != ActualGameId:
                            table2.update(recordId, {'LastGameId': ActualGameId})
                            table2.update(recordId, {"GamePlayed": int(records['fields']['GamePlayed'])+1})
                            print('GamePlayed +1')
            except: 
                print('no game')
                        
            r = request('post', '/lol-lobby/v2/play-again')
        if phase =='EndOfGame':
            PhaseBlock()
            
            #get the summoner name
            SummonerName = request('get', '/lol-summoner/v1/current-summoner').json()["displayName"]
            time.sleep(2)
            print("sending play again")
            r = request('post', '/lol-lobby/v2/play-again')
            
            puuid = request('get', '/lol-summoner/v1/current-summoner').json()['puuid']

            r = request('get', '/lol-ranked/v1/ranked-stats/'+puuid)
            tier = r.json()["queues"][0]["tier"]
            division =r.json()["queues"][0]["division"]
            leaguepoints= r.json()["queues"][0]["leaguePoints"]
            wins = r.json()["queues"][0]["wins"]
            losses= r.json()["queues"][0]["losses"]

            for records in table.all(sort=["Unban"]):
                if records['fields']['IngameName'] == SummonerName:
                    recordId = records['id']
                    table.update(recordId, {"WIN/LOSS": str(wins)+'W/'+str(losses)+'L',"Rank": str(tier) +' '+ str(division) +' '+ str(leaguepoints)+"LP"})
            
            #Iron4 0Lp stop account
            if tier == 'IRON' and division == 'IV' and leaguepoints <= 0:
                print('One more account readyyyyy')
                table.update(recordId, {"FinishedAcc": "Finish"})
                table.update(recordId,{"PcName":  Pc_Name+" STOP"})
                PussyDestroyer()
        
            time.sleep(2)

        if phase =='None':
            PhaseBlock()
            LastAction()
            ConfigSetup()
            Pause()
            while Personnage.fullApiAccess == False:
                try :
                    ChampionsCollection = request('get', '/lol-champions/v1/inventories/' + str(accid) + '/champions-playable-count').json()['championsOwned']
                
                    if ChampionsCollection < 20:
                        Store() #buy champs
                    else:
                        print('champs ok')
                    Personnage.fullApiAccess = True
                except:
                    print("can't get champs yet")
                    Personnage.fullApiAccess = False
                    time.sleep(1)
                    
            SummonerName = None
            try:
                SummonerName = request('get', '/lol-summoner/v1/current-summoner').json()["displayName"]
                Time = requests.get("http://worldtimeapi.org/api/timezone/Europe/Paris").json()['utc_datetime']
                print(SummonerName)
                
                for records in table.all():
                    if records['fields']['Account'] == Personnage.account:
                        recordId = records['id']
                        table.update(recordId, {"IngameName": SummonerName})
                        
                for records in table.all():
                    print(records)
                    if records['fields']['IngameName'] == SummonerName:
                        recordId = records['id']
                        table.update(recordId, {"Unban": Time})
                
                print('need to create lobby')
                r =request('post','/lol-lobby/v2/lobby',data={"queueId": 420})
            except:
                r = request('post', '/lol-lobby/v2/lobby',data={"queueId": 420})
                pass
            time.sleep(2)
        if phase == 'Reconnect':
            PhaseBlock()
        
        if phase =='Lobby': 
            ConfigSetup()
            PhaseBlock()
            LastAction()
            SummonerName = request('get', '/lol-summoner/v1/current-summoner').json()["displayName"]
            puuid = request('get', '/lol-summoner/v1/current-summoner').json()['puuid']

            r = request('get', '/lol-ranked/v1/ranked-stats/'+puuid)
            tier = r.json()["queues"][0]["tier"]
            division =r.json()["queues"][0]["division"]
            leaguepoints= r.json()["queues"][0]["leaguePoints"]
            wins = r.json()["queues"][0]["wins"]
            losses= r.json()["queues"][0]["losses"]

            for records in table.all(sort=["Unban"]):
                if records['fields']['IngameName'] == SummonerName:
                    print("Updating ELO")
                    recordId = records['id']
                    table.update(recordId, {"Rank": str(tier) +' '+ str(division) +' '+ str(leaguepoints)+"LP","WIN/LOSS": str(wins)+'W/'+str(losses)+'L'})
            
            if tier == 'IRON' and division == 'IV' and leaguepoints <= 0:
                print('One more account readyyyyy')
                table.update(recordId,{"PcName":  Pc_Name+" STOP","HWID":  Pc_Name+" STOP","FinishedAcc": "Finish"})
                PussyDestroyer()
                
            QueueLockout = None
            Pause()
            print('need to pick lanes')
            r = request('put', '/lol-lobby/v2/lobby/members/localMember/position-preferences', data ={"firstPreference": "UTILITY","secondPreference":"MIDDLE",})
            sleep(2)
            r = request('post', '/lol-lobby/v2/lobby/matchmaking/search')
            sleep(2)
            r = request('get', '/lol-matchmaking/v1/search')
            try : 
                errors = r.json()["errors"]
                if errors != []:
                    print(errors)
                    for error in errors:
                        print(error["penaltyTimeRemaining"])
                        if error["penaltyTimeRemaining"] > 2000:
                            QueueLockout = True
                            print('QueueLockout')
                            lockoutTime = error["penaltyTimeRemaining"]
                            for records in table.all():
                                print(records)
                                if records['fields']['IngameName'] == SummonerName:
                                    recordId = records['id']
                                    table.update(recordId, {"Unban": str(datetime.datetime.now()+datetime.timedelta(seconds=lockoutTime))})
                        #if  0 < error["penaltyTimeRemaining"] < 901: sleep = error["penaltyTimeRemaining"]
                        if 0 < error["penaltyTimeRemaining"] < 2000:
                            time.sleep(error["penaltyTimeRemaining"])
                            print("Sleeping for " + str(error["penaltyTimeRemaining"]))
            except:
                pass
            sleep(2)
            
            try:
                if QueueLockout != None:
                    
                    SummonerName = request('get', '/lol-summoner/v1/current-summoner').json()["displayName"]                   
                    time_change = datetime. timedelta(seconds=int(lockoutTime))
                    
                    for records in table.all():
                        if records['fields']['IngameName'] == SummonerName:
                            recordId = records['id']
                            table.update(recordId, {"Unban": str(datetime.datetime.now()+time_change)})
                    
                    print("Starting Pussy Destroyer")
                    sleep(2)
                    PussyDestroyer()    

                else:
                    print('No QueueLockout detected')
                    QueueLockout = None
                                  
            except:
                pass
        
            restart()
        
        if phase != 'ChampSelect':
            LastAction()

        if phase == 'ReadyCheck':
            r = request('post', '/lol-matchmaking/v1/ready-check/accept')
            time.sleep(3)

        elif phase == 'ChampSelect':
            time.sleep(3)
            LastAction()
            
            r = request('get', '/lol-champ-select/v1/session')
            if r.status_code != 200:
                continue
            cs = r.json()
            if cs["timer"]["phase"] == "PLANNING":
                print('planning')

            if cs["timer"]["phase"] == "BAN_PICK":
                global lastMessageChampSelect
                print(" you are in ban/pick")
                SummonerID = request('get', '/lol-summoner/v1/current-summoner').json()["summonerId"]
                print(SummonerID)
                cellID = -1
                
                actions = cs["actions"]
                chatRoomName = (cs["chatDetails"]["chatRoomName"]).split('@')[0] # récupérer l'identifiant de la room, seule la partie avant le @ est utile
                url = '/lol-chat/v1/conversations/'+chatRoomName+'/messages'
                messageList = ['Hello guys :D', "Hi there ! :)",'Hello team how you doing ? :D']
                data = { "body": messageList[random.randint(0,len(messageList)-1)],"type": "chat"}
                if (datetime.datetime.now() - lastMessageChampSelect).total_seconds() > 240:
                    r = request('post', url, data = data)
                    lastMessageChampSelect = datetime.datetime.now()
                

                runesPages = request('get', '/lol-perks/v1/pages').json()
                print(runesPages)
                for _ in runesPages:
                    id = _["id"]
                    if id not in [50,51,52,53,54] and _["selectedPerkIds"][0] !=8214: #si la page de rune ne fait par partie des runes de base et que sa rune principale n'est pas aery
                        request('delete', '/lol-perks/v1/pages/'+str(id))
                        data = {"autoModifiedSelections": [0],"current": True,"isActive": True,"isDeletable": True,"isEditable": True,"isValid": True,"lastModified": time.time(),"name": "Zoomies !!","order": 0,"primaryStyleId": 8200,"selectedPerkIds": [8214, 8224, 8210, 8237, 8451, 8401, 5008, 5008, 5002],"subStyleId": 8400}    
                        url = '/lol-perks/v1/pages/'
                        request('post', url, '', data)
                        time.sleep(2)
                if len(runesPages) == 5: # check si les pages de runes sont juste celles du jeu
                    data = {"autoModifiedSelections": [0],"current": True,"isActive": True,"isDeletable": True,"isEditable": True,"isValid": True,"lastModified": time.time(),"name": "Zoomies !!","order": 0,"primaryStyleId": 8200,"selectedPerkIds": [8214, 8224, 8210, 8237, 8451, 8401, 5008, 5008, 5002],"subStyleId": 8400}    
                    url = '/lol-perks/v1/pages/'
                    request('post', url, '', data)
                    time.sleep(2)
                                        
                for _ in range(0,9):
                    summonersInfo = request('get', '/lol-champ-select/v1/summoners/'+str(_)).json()
                    if SummonerID == summonersInfo["summonerId"]:
                        cellId = summonersInfo["cellId"]
                        if summonersInfo["spell1IconPath"] != "/lol-game-data/assets/DATA/Spells/Icons2D/Summoner_heal.png" or summonersInfo["spell2IconPath"] != "/lol-game-data/assets/DATA/Spells/Icons2D/SummonerIgnite.png":
                            print("wrong summoner spells")
                            url = '/lol-champ-select/v1/session/my-selection'
                            data = {"spell1Id": 7, "spell2Id": 14}
                            r = request('patch', url, '', data)
                            time.sleep(0.5)
                        else:
                            print("Correct Summoner spells")
                        
                            
                        for _ in actions : # double boucle car liste d'actions est une liste de dictionnaire
                            for _ in _ :
                                if _["actorCellId"] == cellId:
                                    if _["isInProgress"]== True:
                                        print('you are in action '+_["type"])
                                        if _['type'] == "ban":
                                            print('you are in cell '+str(cellId))
                                            url = '/lol-champ-select/v1/session/actions/%d' % _['id']
                                            data = {'championId': 12}
                                            r = request('patch', url, '', data)
                                            time.sleep(0.5)
                                            r = request('post', url+'/complete', '', data)
                                            time.sleep(0.5)


                                        if _['type'] == "pick":
                                            print('you are in cell '+str(cellId))
                                            url = '/lol-champ-select/v1/session/actions/%d' % _['id']
                                            data = {'championId': 350}
                                            r = request('patch', url, '', data)
                                            time.sleep(0.5)
                                            r = request('post', url+'/complete', '', data)
                                            time.sleep(0.5)
                                            
                                    else : 
                                        print("you finished action "+_["type"])          


        elif phase == 'InProgress':
            LastAction()
            
            print('in progress')
            statuscheck()
        else:
                sleep(1)

        sleep(0.5)
            
def main():
    statuscheck()
    return True
if __name__ == "__main__":
    main()



# https://ddragon.leagueoflegends.com/cdn/11.16.1/data/en_US/champion/Yuumi.json
# http://ddragon.leagueoflegends.com/cdn/6.8.1/img/map/map11.png
# store last attached command to who ( with positions of the pictures we know who), si self attached = true, on sait à qui on est attaché