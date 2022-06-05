from ast import If
import os
import re
import sys
from tkinter import N 
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
import keyboard
import requests
import pyautogui
import pyscreeze
import pytesseract
import pytesseract
import numpy as nm
import pydirectinput
from time import sleep
from logging import info
from PIL import ImageGrab
from random import randrange
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

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

gamedirs = [r'C:\Games\Garena\32787\LeagueClient',
            r'D:\Games\League of Legends']
os.system("")
lastMessageChampSelect = datetime.datetime.now() - datetime.timedelta(minutes=4)

#NuberGamesToPlay
NumberGamesToPlay = random.randint(10, 15)
print(NumberGamesToPlay)
#surrend
OneMinute= 900
#Number Dudge Singed
NumberSinged= 0
# saved time
saved_time = datetime.datetime.now()
Action = "Waiting"

#Account Status Check
API_KEY= "key181wgNDrYM2bms"
BASE_ID = "appHnr7cu8j1HlMC2"
table = Table(API_KEY, 'appHnr7cu8j1HlMC2', 'YUUMI')
table2 = Table(API_KEY, 'appHnr7cu8j1HlMC2', 'ADMIN')

PhaseNumber = 0
Lastphase = "Nothing"





def restart():
    subprocess.call(["git", "reset", "--hard", "HEAD"])
    subprocess.call(["git", "pull"])
    print('Updating')
    print("argv was",sys.argv)
    print("sys.executable was", sys.executable)
    print("restart now")

    os.execv(sys.executable, ['python'] + sys.argv)

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
    time.sleep(3)
    os.startfile("C:\\Riot Games\\League of Legends\\LeagueClient.exe")
    print("Starting League of Legends..")
    time.sleep(25)
    restart()
def Pause():

    for records in table2.all():
        if records['fields']['PcName'] == socket.gethostname():
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
    return json.loads(response)

def MouseClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

class Personnage:
    
    account = None
    
    # Yuumi    
    team = None
    index = None
    yuumiState = None
    teamState = None
    WName = None
    attached = None

    #spell levels
    QLevel = None
    WLevel = None
    ELevel = None
    RLevel = None

    YuumiLevel = None
    datas = None
    hp = None
    position = None
    yuumiIndex = None
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
    adcDead = None
    jungleDead = None
    midDead = None
    topDead = None
    adcIndex = None
    midIndex = None
    jungleIndex = None
    topIndex = None
    carryHP =None
    adcName = None

    adcPicture = [1870,600]
    midPicture = [1770,600]
    junglePicture = [1670,600]
    topPicture = [1570,600]

    randx = random.random()



    # GENERIC FUNCTIONS      
    def setup(self):                    
        self.updateDatas()
        i=0
        while not "gameData" in self.datas:
            time.sleep(0.2)
            self.updateDatas()
        while self.datas["gameData"]["gameTime"] < 1:
            time.sleep(0.2)
            self.updateDatas()
            print("Loading Screen")
        print("Game just started")
        for records in table2.all():
            if records['fields']['PcName'] == socket.gethostname():
                recordId = records['id']
                now = datetime.datetime.now()
                table2.update(recordId, {"LastAction": "InGame"})
                table2.update(recordId, {"LastActionTime": now.strftime("%H:%M %m-%d-%Y") })

        f = open('stuff.json',)
        self.stuff = json.load(f)
        f.close()
        print('stuff loaded')
        i=0
        
        for x in self.datas["allPlayers"]:
                
            if x["championName"] == "Yuumi":
                print('Found it in the '+str(i)+" th index")
                self.yuumiIndex = i
                self.adcIndex = i-1
                self.midIndex = i-2
                self.jungleIndex = i-3
                self.topIndex = i-4
                print(self.adcIndex)
                team= math.ceil((i+1)/(len(self.datas["allPlayers"])/2))

                #Start of the game 
                self.toplanerTimer = random.randint(900, 1300)
                print('will go to toplaner at '+ str(self.toplanerTimer))
                # self.cameraLock()
                pydirectinput.press('space')
                time.sleep(0.5)
                pydirectinput.press('p')
                time.sleep(0.2)
                pydirectinput.keyDown('ctrl')
                time.sleep(0.1)
                pydirectinput.press('l')
                pydirectinput.keyUp('ctrl')
                pyautogui.write('spellt', interval=0.15)
                time.sleep(0.2)
                pydirectinput.press('enter')
                pydirectinput.keyDown('ctrl')
                pydirectinput.press('l')
                pydirectinput.keyUp('ctrl')
                time.sleep(0.1)
                pyautogui.write('oracle', interval=0.15)
                time.sleep(0.2)
                pydirectinput.press('enter')
                pydirectinput.press('p')
                time.sleep(0.2)
                list1 = [('glhf'), ('have fun'), ('good luck'), ('')]
                pydirectinput.press('enter')
                time.sleep(0.2)
                pydirectinput.write(random.choice(list1))
                time.sleep(0.2)
                pydirectinput.press('enter')
                

                self.passiveCooldown = time.time()
                
                if team ==1:
                    self.Team = 'Blue'
                    self.BaseX = 1539
                    self.BaseY = 1042
                    self.qX = 1250
                    self.qY = 100
                    print(self.Team)
                if team ==2:
                    self.team = 'Red'
                    self.BaseX = 1888
                    self.BaseY = 691
                    self.qX = 450
                    self.qY = 350
                    print(self.Team)
                else:
                    print(str(i))
                break
            else:
                i=i+1

    def manacheckE(self):
    # if Mana < 0.15*(MaxMana)+40:
    #     print('not enough mana to cast E')
    # else:
    #     pressE()
    #     print(' can cast E')
    # time.sleep(5)
        screen=pyscreeze.screenshot()
        eCast=screen.getpixel((920,1012))
        if eCast[1] > 250:
            print('adc needs healing')
            pydirectinput.press('e')
            # doubleCheck = screen.
        else:
            print('cant heal yet')
        
    def cameraLock(self):
        camera = pyautogui.locateOnScreen("images/camera.png", grayscale=False,confidence=0.90)
        if camera!=None:
            pyautogui.click(camera[0],camera[1])
        else:
            print('Cant start queue yet')

    def shop(self):
        A = self.nombreItems -1
        desiredItem = self.stuff["items"][A-1]["displayName"]
        itemInTheSlot = self.yuumiItems[A-1]["displayName"]
        if self.nombreItems<7:
            if self.nombreItems <4:
                if self.gold > 950:
                    pydirectinput.press('p')
                    time.sleep(0.2)
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.press('l')
                    pydirectinput.keyUp('ctrl')
                    pyautogui.write(("Bandleglass Mirror").lower(), interval=0.15)
                    time.sleep(0.2)
                    pydirectinput.press('enter')
                    pydirectinput.press('p')

            if self.nombreItems ==4:
                if self.gold > 1550:
                    if self.yuumiItems[2]["displayName"] != ["Moonstone Renewer"]:
                        pydirectinput.press('p')
                        time.sleep(0.2)
                        pydirectinput.keyDown('ctrl')
                        pydirectinput.press('l')
                        pydirectinput.keyUp('ctrl')
                        pyautogui.write(("Moonstone Renewer").lower(), interval=0.15)
                        time.sleep(0.2)
                        pydirectinput.press('enter')
                        pydirectinput.press('p')


            if self.gold > self.stuff["items"][A]["price"]:
                if itemInTheSlot != desiredItem:
                    print("intem in the slot "+itemInTheSlot)
                    print("desired item"+desiredItem)
                    print('Item precedent not completed')
                    pydirectinput.press('p')
                    time.sleep(0.2)
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.press('l')
                    pydirectinput.keyUp('ctrl')
                    pyautogui.write((desiredItem).lower(), interval=0.15)
                    time.sleep(0.2)
                    pydirectinput.press('enter')
                    pydirectinput.press('p')
                    print(self.stuff["items"][A-1]["displayName"]+" was bought")
                else:
                    
                    print(self.stuff["items"][A-1]["displayName"])
                    print(self.stuff["items"][A]["displayName"])
                    print('On achete bien le prochain item')
                    pydirectinput.press('p')
                    time.sleep(0.2)
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.press('l')
                    pydirectinput.keyUp('ctrl')
                    pyautogui.write((self.stuff["items"][A]["displayName"]).lower(), interval=0.15)
                    time.sleep(0.2)
                    pydirectinput.press('enter')
                    pydirectinput.press('p')
                    print(self.stuff["items"][A]["displayName"]+" was bought")
            else:
                print('sorry no money to buy'+ (self.stuff["items"][A]["displayName"]).lower())
        else:
            print('nothing to buy, you are full stuff buddy')


    def __init__(self):
        self.setup()
        self.start()

    def updateDatas(self):
        self.datas = fetchDatas()

    def start(self):
        
        def LastAction():
            # nouveau last action : last action since ....
            
            global saved_time
            current_time = datetime.datetime.now()
            if (current_time - saved_time).seconds >= 10:
                for records in table2.all():
                    if records['fields']['PcName'] == socket.gethostname():
                        recordId = records['id']
                        now = datetime.datetime.now()
                        table2.update(recordId, {"LastAction": Action})
                        table2.update(recordId, {"LastActionTime": now.strftime("%H:%M %m-%d-%Y") })
                        saved_time = datetime.datetime.now()
                        
        while self.datas["gameData"]["gameTime"] < 3600:
            self.updateDatas()
            self.updatePerso()
            self.LevelUP()
            self.Surrender()
            self.randx = random.random()
            print(self.randx)
            
            if self.randx >0.80:
                pyautogui.moveTo(960,480)
                MouseClick()
                pydirectinput.press('space')   

            if self.adcDead == False:
                if self.attached == False:
                    if self.yuumiMana < self.resourceMax:
                        self.baseCheck()
                        self.updateDatas()
                        self.updatePerso()
                        self.Surrender()     

            if self.adcDead == False:
                if self.attached == False:
                    print('going to adc')
                    pyautogui.click(1861,603)                    
                    pydirectinput.press('w')  
                    print('goin to adc')
                    #LastAction
                    Action = "Going to adc"
                    LastAction()

            if self.attached == True:
                print('yuumi is attached')
                self.hpCheck()
                if self.carryHP<50:
                    print(' Mon adc a '+str(self.carryHP)+'%HP')
                    if time.time()> (self.healCooldown+240):
                        if self.datas["gameData"]["gameTime"] > 90:
                            pydirectinput.press('f')
                            #LastAction
                            Action = "Healing"
                            LastAction()
                            self.healCooldown = time.time()
                    pyautogui.moveTo(self.ennemyPosition[0],self.ennemyPosition[1])
                    self.ultimateCast()
                    print('send R')
                    ennemy = pyautogui.locateOnScreen("images/1.png", grayscale=False,confidence=0.90)
                    if ennemy!=None:
                        if ennemy[0]+40 >0 and ennemy[0]+40<1920:
                            if ennemy[1]+100 >0 and ennemy[1]+100<1080:
                                pyautogui.moveTo(ennemy[0]+40,ennemy[1]+100)
                                pydirectinput.press('d')
                    self.manacheckE()
                    print('Healed ADC')
                if self.carryHP<85:
                    print(' Mon adc a '+str(self.carryHP)+'%HP')
                    self.manacheckE()
                    print('Healed ADC')

                if self.carryHP>85:
                    if time.time() > (self.qspellCooldown+25):
                        ennemy = pyautogui.locateOnScreen("images/1.png", grayscale=False,confidence=0.90)
                        if ennemy!=None:
                            self.qSpell()
                            self.qspellCooldown = time.time()

                if self.yuumiMana < (15*(self.resourceMax)/100):
                    print('you got '+ str(self.yuumiMana))
                    self.procPassive()

                else:
                    print('HP > 85%, no need to heal ')
            

            if self.adcDead == True:
                if self.datas["gameData"]["gameTime"] > 600:
                    if self.jungleDead == False:
                        pyautogui.click(self.junglePicture[0],self.junglePicture[1]) 
                        time.sleep(0.2)                   
                        pydirectinput.press('w')  
                        print('going to jungler')
                        time.sleep(5)
                        pydirectinput.press('e')
                        time.sleep(9)
                        pydirectinput.press('e')
                        pyautogui.moveTo(400,400)
                        pydirectinput.press('w')

                    if self.jungleDead == True:
                        if self.midDead == False:
                            pyautogui.click(self.midPicture[0],self.midPicture[1])
                            time.sleep(0.2)                     
                            pydirectinput.press('w')  
                            print('going to midlaner')
                            time.sleep(5)
                            pydirectinput.press('e')
                            time.sleep(9)
                            pydirectinput.press('e')
                            pyautogui.moveTo(400,400)
                            pydirectinput.press('w')
                        if self.midDead == True:
                            if self.topDead == False:
                                pyautogui.click(self.topPicture[0],self.topPicture[1])
                                time.sleep(0.2)                     
                                pydirectinput.press('w')  
                                print('going to toplaner')
                                time.sleep(5)
                                pydirectinput.press('e')
                                time.sleep(9)
                                pydirectinput.press('e')
                                pyautogui.moveTo(400,400)
                                pydirectinput.press('w')
                            if self.topDead == True:
                                print('going back to base')  
            
                if time.time()> (self.backCooldown+50):
                    #LastAction
                    Action = "Going back"
                    LastAction()
                    pyautogui.moveTo(self.BaseX,self.BaseY)
                    print('adc is not alive')
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
                    self.shop()
                    self.backCooldown = time.time()

            # sleep(randrange([0.3, 0.7]))
            time.sleep(0.5)


    # UPDATES            

    def updatePosition(self):
        self.position = [self.datas.posX, self.datas.posY]

    def hpCheck(self):
        screen=pyscreeze.screenshot()
        i=0
        x = None
        y = 635
        if self.adcDead == False:
            x = 1835
        if self.adcDead == True:
            if self.jungleDead== False:
                print('check jungle hp')  
                x = 1738
            if self.jungleDead== True: 
                if self.midDead == False:
                    print('check mid hp') 
                    x = 1641
                if self.midDead == True:
                    print('check top hp') 
                    x = 1544

        for i in range(69):
            rgb_values=screen.getpixel((x,y))
            if rgb_values[1] == 19:
                #doublecheck the pixel color
                bgr_values=screen.getpixel((x,y))
                if bgr_values[1] == 19:
                    x = x+1
                    self.carryHP = i*1.42
                    break
            if rgb_values[1] != 19:
                x = x+1
        else:
            self.carryHP = 100
        
    
    def ctrlq(self): 
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('q')
        pydirectinput.keyUp('ctrl')
    def ctrlw(self): 
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('w')
        pydirectinput.keyUp('ctrl')
    def ctrle(self):    
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('e')
        pydirectinput.keyUp('ctrl')
    def ctrlr(self): 
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('r')
        pydirectinput.keyUp('ctrl')
        


    def baseCheck(self):
        ManaPrecedent = self.yuumiMana
        print("You got "+ str(ManaPrecedent)+ " mana")
        time.sleep(3)

        response = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify = False).text
        datas = json.loads(response)

        ManaActuel = datas["activePlayer"]["championStats"]["resourceValue"]
        print(ManaActuel)
        RegenMana = datas["activePlayer"]["championStats"]["resourceRegenRate"]
        print(RegenMana)

        if ManaActuel > 4*(RegenMana)+ManaPrecedent:
            #open shop()
            print('At Home')
            self.shop()
            time.sleep(3)

        else:
            print('Not at Home')


    def qSpell(self):

        x =0
        ennemy = pyautogui.locateOnScreen("images/1.png", confidence=0.95)
        for pos in pyautogui.locateAllOnScreen('images/minions.png'):
            x = x+1
            self.qX = pos[0]
            self.qY = pos[1]
            if pos[0] < self.qX:
                self.qX = pos[0]
            if pos[1] < self.qY:
                self.qY = pos[1]
            if pos[0] == None:
                print('no minions')
                self.qX = ennemy[0]
                self.qY = ennemy[1]
        
        if self.qX != None:
            offsetx = self.qX -100
            offsety = self.qY -40
            pyautogui.moveTo(offsetx, offsety)
            pydirectinput.press('q') 
            try:
                ennemy = pyautogui.locateOnScreen("images/1.png", confidence=0.95)
                time.sleep(0.3)
                if ennemy[0]+40 >0 and ennemy[0]+40<1920:
                    if ennemy[1]+70 >0 and ennemy[1]+100<1080:
                        pyautogui.moveTo(ennemy[0]+40,ennemy[1]+70)
            except TypeError:
                print('failed q spell')

    def ultimateCast(self):
        if time.time() > (self.ultimateCooldown +70):
            try:
                Ennemies = pyautogui.locateOnScreen(r"images/1.png", grayscale=False,confidence=0.95)
                pyautogui.moveTo(Ennemies[0]+40, Ennemies[1]+100)
                time.sleep(0.2)
                pydirectinput.press('r')
                self.ultimateCooldown = time.time()
            except TypeError:
                print("No ennemies found")
                pyautogui.moveTo(self.BaseX,self.BaseY)
                pydirectinput.press('r')
                self.ultimateCooldown = time.time()


    def procPassive(self) : 
        if time.time() > (self.passiveCooldown +10):
            try:
                Ennemies = pyautogui.locateOnScreen(r"images/1.png", grayscale=False,confidence=0.95)
                # pydirectinput.press('y')
                if Ennemies[0]+40 >0 and Ennemies[0]+40<1920:
                    if Ennemies[1]+100 >0 and Ennemies[1]+100<1080:
                        pyautogui.moveTo(Ennemies[0]+40, Ennemies[1]+100)
                self.ennemyPosition = [Ennemies[0], Ennemies[1]]
                pydirectinput.press('w')
                MouseClick()
                pydirectinput.press('h')      
                pyautogui.moveTo(1861,603)
                time.sleep(0.3)
                pydirectinput.press('w')
                # pydirectinput.press('y')
                self.passiveCooldown = time.time()
            except TypeError:
                print("No ennemies found")

    def Surrender(self):
        
        global OneMinute
        if self.datas["gameData"]["gameTime"] > OneMinute:
            Surrend = pyautogui.locateOnScreen("images/Surrend.png", grayscale=False,confidence=0.80)
            OneMinute=OneMinute+20
            print(OneMinute)
            try:
                if Surrend != None:
                    pydirectinput.press('enter')
                    time.sleep(0.1)
                    pyautogui.write('/ff')
                    time.sleep(0.1)
                    pydirectinput.press('enter')
                    print('I am surrending')
            except :
                print('No surrend detected')
        else:
            print('Not Time to Surrender')
                    
    def LevelUP(self):
        if self.YuumiLevel == 1:
            if self.ELevel < 1:
                self.ctrle()
                print('level up E')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 2:
            if self.QLevel < 1:
                self.ctrlq()
                print('level up Q')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 3:
            if self.ELevel < 2:
                self.ctrle()
                print('level up E')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 4:
            if self.WLevel < 2:
                self.ctrlw()
                print('level up W')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 5:
            if self.ELevel < 3:
                self.ctrle()
                print('level up E')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 6:
            if self.RLevel < 1:
                self.ctrlr()
                print('level up R')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 7:
            if self.ELevel < 4:
                self.ctrle()
                print('level up E')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 8:
            if self.WLevel < 3:
                self.ctrlw()
                print('level up W')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 9:
            if self.ELevel < 5:
                self.ctrle()
                print('level up E')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 10:
            if self.WLevel < 4:
                self.ctrlw()
                print('level up W')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 11:
            if self.RLevel < 2:
                self.ctrlr()
                print('level up R')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 12:
            if self.WLevel < 5:
                self.ctrlw()
                print('level up W')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 13:
            if self.QLevel < 2:
                self.ctrlq()
                print('level up Q')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 14:
            if self.QLevel < 3:
                self.ctrlq()
                print('level up Q')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 15:
            if self.QLevel < 4:
                self.ctrlq()
                print('level up Q')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 16:
            if self.RLevel < 3:
                self.ctrlr()
                print('level up R')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 17:
            if self.QLevel < 5:
                self.ctrlq()
                print('level up Q')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 18:
            if self.QLevel < 6:
                self.ctrlq()
                print('level up Q')
            else:
                print('Nothing To Level Up')
        print("Yuumi is level  "+str(self.YuumiLevel))

    def updatePerso(self):
        self.yuumiState = self.datas["activePlayer"]
        self.teamState = self.datas["allPlayers"]
        self.WName = self.yuumiState["abilities"]["W"]["displayName"]
        if self.WName == "Change of Plan":
            self.attached = True
        else: 
            self.attached = False
        self.QLevel = self.yuumiState["abilities"]["Q"]["abilityLevel"]
        self.WLevel = self.yuumiState["abilities"]["W"]["abilityLevel"]
        self.ELevel = self.yuumiState["abilities"]["E"]["abilityLevel"]
        self.RLevel = self.yuumiState["abilities"]["R"]["abilityLevel"]
        self.YuumiLevel = self.yuumiState["level"]
        self.adcName = self.teamState[self.adcIndex]["championName"]
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


def Connexion():
    
    PcName = socket.gethostname()
    print(PcName)
        
    table = Table(API_KEY, 'appHnr7cu8j1HlMC2', 'YUUMI') 
    Connexion_image = pyautogui.locateOnScreen("images/Connexion.png", grayscale=False,confidence=0.90)
    TermsOfServices = pyautogui.locateOnScreen("images/TermsOfServices.png", grayscale=False,confidence=0.90)
    try:
        if Connexion_image!=None:
            
            formula = match({"PcName": PcName[:3]})
            Personnage.account = table.first(formula=formula, sort=["Unban"])['fields']['Account']
            password = table.first(formula=formula, sort=["Unban"])['fields']['Password']
            
            #LogDesired
            pyautogui.moveTo(Connexion_image[0],Connexion_image[1]+80)
            time.sleep(0.1)
            MouseClick()
            pyautogui.typewrite(Personnage.account, interval=0.10)
            time.sleep(0.1)
            print('Log Write')
                
            #PwdDesired
            pyautogui.moveTo(Connexion_image[0],Connexion_image[1]+140)
            time.sleep(0.1)
            MouseClick()
            # pyautogui.typewrite(password, interval=0.10)
            pyperclip.copy(password)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.1)
            print('Pwd Write')
            for records in table.all():
                if records['fields']['Account'] == Personnage.account:
                    recordId = records['id']
                    table.update(recordId, {"Unban": str(datetime.datetime.now())})
            
            if TermsOfServices != None:
                pyautogui.moveTo(TermsOfServices[0],TermsOfServices[1])
                time.sleep(1)
                pyautogui.scroll(-100000)
                time.sleep(1)
                pyautogui.click(TermsOfServices[0],TermsOfServices[1]+600)
                
            #Press connexion button
            pyautogui.moveTo(Connexion_image[0]+60,Connexion_image[1]+520)
            time.sleep(0.1)
            MouseClick()
            time.sleep(6)
            
            #Press Play button
            pyautogui.moveTo(Connexion_image[0],Connexion_image[1]+650)
            time.sleep(0.1)
            MouseClick()
            time.sleep(0.1)
            
            for records in table2.all():
                if records['fields']['PcName'] == socket.gethostname():
                    recordId = records['id']
                    table2.update(recordId, {"ConnectedOn": Personnage.account})
                    #LastAction update
                    now = datetime.datetime.now()
                    table2.update(recordId, {"LastAction": 'Connexion'})
                    table2.update(recordId, {"LastActionTime": now.strftime("%H:%M %m-%d-%Y") })
            
            time.sleep(20)
        else:
            print('No connexion detected, waiting 1 seconds')
            time.sleep(10)
            
    except:
        print('No more accounts')
        time.sleep(10)
        Connexion()
               
def PopUpClose():
    try:
        Exclamation = pyautogui.locateOnScreen("images/Exclamation.png", grayscale=False,confidence=0.90)
        GG = pyautogui.locateOnScreen('images/GG.png', grayscale=False,confidence=0.90)
        ok = pyautogui.locateOnScreen('images/ok.jpg', grayscale=False,confidence=0.90)
        list1 =list(pyautogui.locateAllOnScreen('images/CroixM.png', grayscale=False,confidence=0.90))
        list2 =list(pyautogui.locateAllOnScreen('images/CroixM.png',region=(list1[0][0]-1200,list1[0][1], list1[0][0],list1[0][1]+450),grayscale=False,confidence=0.90))

        if Exclamation != None:
            pyautogui.moveTo(Exclamation[0],Exclamation[1])
            pyautogui.click(Exclamation[0],Exclamation[1])
            
        if GG != None:
            pyautogui.moveTo(GG)
            pyautogui.click(GG)

        if ok != None:
            pyautogui.moveTo(ok)
            pyautogui.click(ok)
    
        pyautogui.moveTo(list2[1])
        time.sleep(0.1)
        MouseClick()
        time.sleep(0.1)
        print('PopUp Close')
        time.sleep(0.5)
            
    except:
        print('No PopUp')
        time.sleep(0.2)
    
def SignOutt():
    CroixM = pyautogui.locateOnScreen("images/CroixM.png", grayscale=False,confidence=0.90)
    
    if CroixM!=None:
        pyautogui.moveTo(CroixM[0]+5,CroixM[1]+5)
        time.sleep(0.1)
        MouseClick()
        time.sleep(3)
        pyautogui.moveTo(CroixM[0]-600,CroixM[1]+400)
        time.sleep(0.1)
        MouseClick()
        time.sleep(0.1)
        print('SignOut')
        time.sleep(10)
        restart()
    else:
        print('No CroixM')
        
        
class lobby():
    username = 'riot'
    champion = 350 
    host = '127.0.0.1'
    protocol = 'https'
    gamedirs = [
        r'C:\Riot Games\League of Legends',
        r'D:\Games\League of Legends',
        r'D:\Riot Games\League of Legends',
    ]
    lockfile = None
    print('Waiting for League of Legends to start ..')
    print('Trying to connect')
    Connexion()
    while not lockfile:
        for gamedir in gamedirs:
            lockpath = r'%s\lockfile' % gamedir

            if not os.path.isfile(lockpath):
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
        if not query:
            url = '%s://%s:%s%s' % (lobby.protocol, lobby.host, lobby.port, path)
        else:
            url = '%s://%s:%s%s?%s' % (lobby.protocol, lobby.host, lobby.port, path, query)

        print('%s %s %s' % (method.upper().ljust(7, ' '), url, data))

        fn = getattr(s, method)

        if not data:
            r = fn(url, verify=False, headers=headers)
        else:
            r = fn(url, verify=False, headers=headers, json=data)

        return r



    userpass = b64encode(bytes('%s:%s' % (lobby.username, lobby.password), 'utf-8')).decode('ascii')
    headers = { 'Authorization': 'Basic %s' % userpass }
    print(headers['Authorization'])

    # Create Request session
    s = requests.session()



    # # Main worker loop
    while True:
        accid = request('get', '/lol-login/v1/session').json()['accountId']
        r = request('get', '/lol-gameflow/v1/gameflow-phase')
        if r.status_code != 200:
            print(Back.BLACK + Fore.RED + str(r.status_code) + Style.RESET_ALL, r.text)
            continue
        print(Back.BLACK + Fore.GREEN + str(r.status_code) + Style.RESET_ALL, r.text)

        phase = r.json()
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
                    
                    print(phase+ " phase time to run pussy destroyer")
                    print(PhaseNumber)
                    PussyDestroyer()
                else :
                    print(phase+ "  phase tout est ok pour l'instant")
                    print(PhaseNumber)


        def LastAction():
            global saved_time
            current_time = datetime.datetime.now()
            if (current_time - saved_time).seconds >= 10:
                for records in table2.all():
                    if records['fields']['PcName'] == socket.gethostname():
                        recordId = records['id']
                        now = datetime.datetime.now() - datetime.timedelta(hours=2)
                        table2.update(recordId, {"LastAction": phase})
                        table2.update(recordId, {"LastActionTime": now.strftime("%H:%M %m-%d-%Y")})
                        saved_time = datetime.datetime.now()
                        
        def Refund():
            idtoken = request('get', '/lol-login/v1/session').json()['idToken']     
             
            def getrequest(url):
                        
                auth = 'Bearer %s' % idtoken
        
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': auth
                }
                
                r = requests.get(url, headers=headers)
                return r
            
            def PostRequest(url, data):
                auth = 'Bearer %s' % idtoken

                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': auth
                }
                r = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
                return r
            
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
            StoreUrl = request('get', '/lol-store/v1/getStoreUrl').json()
            TransacHistory = request('get', '/lol-store/v1/transaction/history').json()

            ChampionsCollection = request('get', '/lol-champions/v1/inventories/' + str(accid) + '/champions-playable-count').json()['championsOwned']
            print(ChampionsCollection)
                                        
            def PostRequest(url, data):
                auth = 'Bearer %s' % idtoken
            
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': auth
                }
                r = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
                return r
    
            champsCheap = ["Amumu","Annie","Ashe,","Dr. Mundo","Garen","Kayle","Master Yi","Nunu","Poppy","Ryze","Singed","Sivir","Soraka","Warwick"]
            champIDListCheap = [32,1,22,36,86,10,11,20,78,13,27,15,16,19]

            champsLessCheap = ["Taric","Teemo","Tristana","Tryndamere","Twisted Fate"]
            ChampIDListLessCheap = [44,17,18,23]
            Yuumi = "350"

            for champID in champIDListCheap: 
                BoughtChampion = PostRequest( str(StoreUrl)+'/storefront/v3/purchase', data=({"accountId":accid,"items":[{"inventoryType":"CHAMPION","itemId":champID,"ipCost":450,"quantity":1}]}))
                print(BoughtChampion.json())
                time.sleep(1)
                
            for champID in ChampIDListLessCheap:
                BoughtChampion = PostRequest( str(StoreUrl)+'/storefront/v3/purchase', data=({"accountId":accid,"items":[{"inventoryType":"CHAMPION","itemId":champID,"ipCost":1350,"quantity":1}]}))
                print(BoughtChampion.json())
                time.sleep(1)
            BoughtChampion = PostRequest( str(StoreUrl)+'/storefront/v3/purchase', data=({"accountId":accid,"items":[{"inventoryType":"CHAMPION","itemId":350,"ipCost":6300,"quantity":1}]}))
        
        if phase =='WaitingForStats':
            print("you are in WaitingForStats phase")
            PhaseBlock()
        if phase =='PreEndOfGame':
            PhaseBlock()
            
            LastAction()
            
            okPreEndOfGame = pyautogui.locateOnScreen("images/okPreEndOfGame.png")
            pyautogui.click(900,500)
            if okPreEndOfGame !=None:
                pyautogui.click(okPreEndOfGame[0],okPreEndOfGame[1])
            try:
                os.system('taskkill /f /im "SystemSettings.exe"')
            except:
                print('no SystemSettings.exe')
            r = request('post', '/lol-lobby/v2/play-again')
        if phase =='EndOfGame':
            #LastAction()
            
            global NumberGamesToPlay
            #get the summoner name
            SummonerName = request('get', '/lol-summoner/v1/current-summoner').json()["displayName"]
            time.sleep(2)
            print("sending play again")
            r = request('post', '/lol-lobby/v2/play-again')
            
            
            try:
                OKEND2 = pyautogui.locateOnScreen("images/ok.JPG", confidence=0.90)
                pyautogui.click(OKEND2)                
                OKEND = pyautogui.locateOnScreen("images/OKEND.JPG", confidence=0.90)
                pyautogui.click(OKEND)
                IUnderstand = pyautogui.locateOnScreen("images/IUnderstand.JPG", confidence=0.70)
                pyautogui.click(IUnderstand)
                IAgree = pyautogui.locateOnScreen("images/IAgree.JPG", grayscale=False,confidence=0.90)
                if IAgree != None:
                    print('I Agree')
                    pyautogui.click(IAgree[0]+80,IAgree[1]-20)
                    pyautogui.write('I Agree', interval=0.25)
            except:
                print('Nice')
                
            print('thanking the mates and going next')
            

            NumberGamesToPlay =NumberGamesToPlay -1
            print(NumberGamesToPlay,'avec le -1')
            
            for records in table.all():
                if records['fields']['IngameName'] == SummonerName:
                    recordId = records['id']
                    table.update(recordId, {"GamesToPlay": str(NumberGamesToPlay)})
            
            for records in table2.all():
                if records['fields']['PcName'] == socket.gethostname():
                    recordId = records['id']
                    #add 1 to the number of games played
                    table2.update(recordId, {"GamePlayed": int(records['fields']['GamePlayed'])+1})
                    print('GamePlayed +1')
                    
            
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
                    table.update(recordId, {"Rank": str(tier) +' '+ str(division) +' '+ str(leaguepoints)+"LP"})
                    table.update(recordId, {"WIN/LOSS": str(wins)+'W/'+str(losses)+'L'})
            
            #Iron4 0Lp stop account
            if tier == 'IRON' and division == 'IV' and leaguepoints <= 0:
                print('One more account readyyyyy')
                table.update(recordId, {"FinishedAcc": "Finish"})
                table.update(recordId,{"PcName":  socket.gethostname()+" STOP"})
                PussyDestroyer()
                
            
            time.sleep(2)

        if phase =='None':
            PhaseBlock()
            LastAction()
            ConfigSetup()
            
            ChampionsCollection = request('get', '/lol-champions/v1/inventories/' + str(accid) + '/champions-playable-count').json()['championsOwned']
            
            if ChampionsCollection < 20:
                Store() #buy champs
            else:
                print('champs ok')
                
            time.sleep(3)
            SummonerName = None
            try:
                SummonerName = request('get', '/lol-summoner/v1/current-summoner').json()["displayName"]
                
                for records in table.all():
                    if records['fields']['Account'] == Personnage.account:
                        recordId = records['id']
                        table.update(recordId, {"IngameName": SummonerName})
                        
                for records in table.all():
                    if records['fields']['IngameName'] == SummonerName:
                        recordId = records['id']
                        table.update(recordId, {"Unban": str(datetime.datetime.now())})
                
                print('need to create lobby')
                r =request('post','/lol-lobby/v2/lobby',data={"queueId": 420})
            except:
                print("no summoner name, account already logged out")
                print("we send the magical pussy destroyer")
                PussyDestroyer()

        if phase =='Lobby': 
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
                    table.update(recordId, {"Rank": str(tier) +' '+ str(division) +' '+ str(leaguepoints)+"LP"})
                    table.update(recordId, {"WIN/LOSS": str(wins)+'W/'+str(losses)+'L'})
            
            #Iron4 0Lp stop account
            if tier == 'IRON' and division == 'IV' and leaguepoints <= 0:
                print('One more account readyyyyy')
                table.update(recordId, {"FinishedAcc": "Finish"})
                table.update(recordId,{"PcName":  socket.gethostname()+" STOP"})
                PussyDestroyer()
            QueueLockout = None
            AtemptToJoin = pyautogui.locateOnScreen("images/AtemptToJoin.png", confidence=0.90)
            OKEND = pyautogui.locateOnScreen("images/OKEND.JPG", confidence=0.90)
            IUnderstand = pyautogui.locateOnScreen("images/IUnderstand.JPG", confidence=0.70)
            GG = pyautogui.locateOnScreen('images/GG.png', grayscale=False,confidence=0.90)
            
            Pause()
            
            print('need to pick lanes')
            r = request('put', '/lol-lobby/v2/lobby/members/localMember/position-preferences', data ={"firstPreference": "UTILITY","secondPreference":"MIDDLE",})
            sleep(2)
            r = request('post', '/lol-lobby/v2/lobby/matchmaking/search')
            sleep(2)
            r = request('get', '/lol-matchmaking/v1/search')
            # print(r.json())
            errors = r.json()["errors"]
            if errors != []:
                print(errors)
                for error in errors:
                    print(error["penaltyTimeRemaining"])
                    if error["penaltyTimeRemaining"] > 901:
                        QueueLockout = True
                        print('QueueLockout')
                        lockoutTime = error["penaltyTimeRemaining"]
                        

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
                
                if AtemptToJoin != None:
                    
                    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
                    SummonerName = request('get', '/lol-summoner/v1/current-summoner').json()["displayName"]
                    AtemptToJoin = pyautogui.locateOnScreen('images/AtemptToJoin.png')

                    while(True):
                        
                        cord = (AtemptToJoin[0]+120, AtemptToJoin[1]+85, AtemptToJoin[0]+210, AtemptToJoin[1]+120)
                        cap = ImageGrab.grab(bbox =(cord))

                        BanTime = pytesseract.image_to_string(
                                cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
                                lang ='eng')
                        
                        numbers = re.findall(r'\d+', BanTime)
                        
                        Seconde = 0
                        Minutes = 0
                        Hours = 0
                        Day = 0
                        
                        try:
                            Seconde = numbers[-1]
                            Minutes = numbers[-2]
                            Hours = numbers[-3]
                            Day = numbers[-4]
                        except:
                            pass
                        
                        time_change = datetime. timedelta(days=int(Day), hours=int(Hours), minutes=int(Minutes), seconds=int(Seconde))
                        
                        for records in table.all():
                            if records['fields']['IngameName'] == SummonerName:
                                recordId = records['id']
                                table.update(recordId, {"Unban": str(datetime.datetime.now()+time_change)})
                                
                                    
                        pyautogui.click(OKEND)
                        time.sleep(1)
                        pyautogui.click(OKEND)
                        time.sleep(1)
                        pyautogui.click(OKEND)
                        time.sleep(1)
                        SignOutt()
                else:
                    print('No AtemptToJoin detected')
            except:
                pass
        
            restart()
        
        if phase != 'ChampSelect':
            LastAction()

        if phase == 'ReadyCheck':
            
            r = request('post', '/lol-matchmaking/v1/ready-check/accept') 

        elif phase == 'ChampSelect':
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
                
                #message 2 minute cooldown
                if (datetime.datetime.now() - lastMessageChampSelect).total_seconds() > 240:
                    r = request('post', url, data = data)
                    lastMessageChampSelect = datetime.datetime.now()
                
                
                
                # print(request('get', url, '', data).json()) get the chat message
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
                                            print('annie')
                                            r = request('patch', url, '', data)
                                            time.sleep(0.5)
                                            r = request('post', url+'/complete', '', data)
                                            time.sleep(0.5)


                                        if _['type'] == "pick":
                                            print('you are in cell '+str(cellId))
                                            url = '/lol-champ-select/v1/session/actions/%d' % _['id']
                                            data = {'championId': 350}
                                            print('annie')
                                            r = request('patch', url, '', data)
                                            time.sleep(0.5)
                                            r = request('post', url+'/complete', '', data)
                                            time.sleep(0.5)
                                            
                                    else : 
                                        print("you finished action "+_["type"])          


        elif phase == 'InProgress':
            for records in table2.all():
                if records['fields']['PcName'] == socket.gethostname():
                    recordId = records['id']
                    #LastGameRun update
                    now = datetime.datetime.now()
                    table2.update(recordId, {"LastGameRun": now.strftime("%H:%M %m-%d-%Y") })
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