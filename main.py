import os
import time
import json
import math
import random
import win32api
import win32con
import requests
import pyautogui
import pyscreeze
import numpy as nm
import pydirectinput
from time import sleep
from PIL import ImageGrab
from random import randrange
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError
from requests.packages.urllib3.util.retry import Retry
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
import urllib3
import json
from base64 import b64encode
from time import sleep
from colorama import Fore, Back, Style
import TimerMsg

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #  

gamedirs = [r'C:\Games\Garena\32787\LeagueClient',
            r'D:\Games\League of Legends']
os.system("")

def fetchDatas():
    response = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify = False).text
    return json.loads(response)

class Personnage:
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
        self.toplanerTimer = random.randint(900, 1300)
        print('will go to toplaner at '+ str(self.toplanerTimer))
        self.cameraLock()
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
        # if gameTime > self.toplanerTimer:
        #     self.adcIndex = i-4
        self.passiveCooldown = time.time()
        TimerMsg.RiotEventListener.MainMsg()

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
        while self.datas["gameData"]["gameTime"] < 3600:
            self.updateDatas()
            self.updatePerso()
            self.LevelUP()
            self.randx = random.random()
            print(self.randx)
            if self.randx >0.80:
                pyautogui.moveTo(960,480)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
                time.sleep(0.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
                pydirectinput.press('space')   

            if self.adcDead == False:
                if self.attached == False:
                    if self.yuumiMana < self.resourceMax:
                        self.baseCheck()
                        self.updateDatas()
                        self.updatePerso()     

            if self.adcDead == False:
                if self.attached == False:
                    print('going to adc')
                    pyautogui.click(1861,603)                    
                    pydirectinput.press('w')  
                    print('goin to adc')

            if self.attached == True:
                print('yuumi is attached')
                self.hpCheck()
                if self.carryHP<50:
                    print(' Mon adc a '+str(self.carryHP)+'%HP')
                    if time.time()> (self.healCooldown+240):
                        pydirectinput.press('f')
                        self.healCooldown = time.time()
                    self.ultimateCast()
                    print('send R')
                    ennemy = pyautogui.locateOnScreen("images/1.png", grayscale=False,confidence=0.90)
                    if ennemy!=None:
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
                    else:
                        TimerMsg.RiotEventListener.MainMsg()
                            

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
                    pyautogui.moveTo(self.BaseX,self.BaseY)
                    print('adc is not alive')
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0,0)
                    time.sleep(0.2)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0,0)
                    print('going back to base')
                    time.sleep(5)
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
                pyautogui.moveTo(ennemy[0]+40,ennemy[1]+70)
                print('hello')
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
                pyautogui.moveTo(Ennemies[0]+40, Ennemies[1]+100)
                pydirectinput.press('w')
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
                time.sleep(0.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)      
                pyautogui.moveTo(1861,603)
                time.sleep(0.3)
                pydirectinput.press('w')
                # pydirectinput.press('y')
                self.passiveCooldown = time.time()
            except TypeError:
                print("No ennemies found")

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

class lobby():
    username = 'riot'
    champion = 350
    host = '127.0.0.1'
    protocol = 'https'
    gamedirs = [r'C:\Riot Games\League of Legends',
            r'D:\Games\League of Legends']
    lockfile = None
    print('Waiting for League of Legends to start ..')
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
        r = request('get', '/lol-gameflow/v1/gameflow-phase')

        if r.status_code != 200:
            print(Back.BLACK + Fore.RED + str(r.status_code) + Style.RESET_ALL, r.text)
            continue
        print(Back.BLACK + Fore.GREEN + str(r.status_code) + Style.RESET_ALL, r.text)

        phase = r.json()


        if phase =='PreEndOfGame':
            okPreEndOfGame = pyautogui.locateOnScreen("images/okPreEndOfGame.png")
            pyautogui.click(900,500)
            if okPreEndOfGame !=None:
                pyautogui.click(okPreEndOfGame[0],okPreEndOfGame[1])
            

        
        if phase =='EndOfGame':
            time.sleep(2)
            print('thanking the mates and going next')
            playAgain = pyautogui.locateOnScreen("images/playagian.JPG", confidence=0.90)
            pyautogui.click(playAgain)

        if phase =='None':
            print('need to create lobby')
            r =request('post','/lol-lobby/v2/lobby',data={"queueId": 420})

        if phase =='Lobby':
            print('need to pick lanes')
            r = request('put', '/lol-lobby/v2/lobby/members/localMember/position-preferences', data ={"firstPreference": "UTILITY","secondPreference":"MIDDLE",})
            sleep(2)
            r = request('post', '/lol-lobby/v2/lobby/matchmaking/search')
        if phase != 'ChampSelect':
            championIdx = 0

        # Auto accept match
        if phase == 'ReadyCheck':
            r = request('post', '/lol-matchmaking/v1/ready-check/accept') 

        # Pick/lock champion
        elif phase == 'ChampSelect':
            r = request('get', '/lol-champ-select/v1/session')
            if r.status_code != 200:
                continue

            cs = r.json()
            if cs["timer"]["phase"] == "PLANNING":
                print('Looking to prepick yuumi')
                SearchChamp = pyautogui.locateOnScreen("images/search.png", grayscale=False,confidence=0.90)
                if SearchChamp != None:
                    pyautogui.click(SearchChamp[0],SearchChamp[1])
                    print("I am going to search Yuumi")
                    pyautogui.write('Yuumi', interval=0.25)
                    Yuumy = pyautogui.locateOnScreen("images/FaceDeYuumi.png", grayscale=False,confidence=0.90)
                    if Yuumy[0] != None:
                        pyautogui.click(Yuumy[0],Yuumy[1])

            banchamp= pyautogui.locateOnScreen("images/banchamp.jpg", grayscale=False,confidence=0.9)
            PhaseDeBan = pyautogui.locateOnScreen("images/PhaseDeBan.png", grayscale=False,confidence=0.90)
            if PhaseDeBan != None:
                print("Time to ban some champs")
                SearchChamp = pyautogui.locateOnScreen("images/search.png", grayscale=False,confidence=0.90)
                pyautogui.click(SearchChamp[0],SearchChamp[1])
                pyautogui.write('Alistar', interval=0.25)
                Alistar = pyautogui.locateOnScreen("images/FaceDeAlistar.png", grayscale=False,confidence=0.90)
                Bannissement = pyautogui.locateOnScreen("images/Bannissement.jpg", grayscale=False,confidence=0.70)

                if Alistar != None:
                    pyautogui.click(Alistar[0],Alistar[1])
                    sleep(3)
                    if Bannissement != None:
                        pyautogui.click(Bannissement[0],Bannissement[1])
                    else: 
                        print("cant find ban button")

            Lockin = pyautogui.locateOnScreen("images/Lockin.jpg", grayscale=False,confidence=0.70)
            if Lockin != None:
                pyautogui.click(Lockin[0],Lockin[1])
                print("Champion Lock bro!")

        elif phase == 'InProgress':
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





