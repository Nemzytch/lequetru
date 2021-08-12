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
import pytesseract
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
import pyautogui
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #  
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
    passiveCooldown = None
    resourceMax = None
    atHome = None
    ultimateCooldown = 1
    qspellCooldown = 1
    ennemy = None
    backCooldown = 1
    healCooldown = 1

    # Taxi     
    toplanerTimer = None
    adcDead = None
    adcIndex = None
    carryHP =None
    adcName = None


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
        print("la partie viens de commencer, on setup tout les bro vive les ours etc etc")
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
                print(self.adcIndex)
                team= math.ceil((i+1)/(len(self.datas["allPlayers"])/2))

                if team ==1:
                    self.Team = 'Blue'
                    self.BaseX = 1539
                    self.BaseY = 1042
                    print(self.Team)
                if team ==2:
                    self.team = 'Red'
                    self.BaseX = 1888
                    self.BaseY = 691
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


    # def manacheckR(self):
    #     screen=pyscreeze.screenshot()
    #     eCast=screen.getpixel((953,1001))
    #     if eCast[0] > 250:
    #         print('adc needs healing')
    #         pydirectinput.press('r')
    #     else:
    #         print('cant heal yet')


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

            if self.adcDead == False:
                if self.attached == False:
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
                if self.carryHP<40:
                    print(' Mon adc a '+str(self.carryHP)+'%HP')
                    if time.time()> (self.healCooldown+240):
                        pydirectinput.press('f')
                    self.ultimateCast()
                    print('send R')
                    self.manacheckE()
                    print('Healed ADC')
                if self.carryHP<85:
                    print(' Mon adc a '+str(self.carryHP)+'%HP')
                    self.manacheckE()
                    print('Healed ADC')

                if self.carryHP>85:
                    if time.time() > (self.qspellCooldown+30):
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

                allies = pyautogui.locateOnScreen("images/1.png", grayscale=False,confidence=0.90)
                if allies!=None:
                    print('found an ally, going to him ')
                    pyautogui.moveTo(allies[0]+40,allies[1]+70)
                    pydirectinput.press('w')
                    self.manacheckE()
                    time.sleep(5)
                    self.manacheckE()
                    time.sleep(3)
                    pydirectinput.press('w')
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
            
                else:
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

            # sleep(randrange([0.3, 0.7]))
            time.sleep(0.5)


    # UPDATES            

    def updatePosition(self):
        self.position = [self.datas.posX, self.datas.posY]

    def hpCheck(self):
        screen=pyscreeze.screenshot()
        i=0
        x = 1835
        y = 635
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
        print("You got "+ str(ManaPrecedent))
        time.sleep(2)

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

        else:
            print('Not at Home')


    def qSpell(self):
        x =0
        minx = 1150
        miny = 100
        for pos in pyautogui.locateAllOnScreen('images/minions.png'):
            x = x+1
            posx = pos[0]
            posy = pos[1]
            if pos[0] < minx:
                minx = pos[0]
            if pos[1] < miny:
                miny = pos[1]
            # print(pos)
            if pos[0] == None:
                print('no minions')
            print('les coordonees du minion'+str(x)+' sont: x'+str(posx)+' y'+str(posy))
        

        print('le plus petit x vaut'+ str(minx) )
        print('le minions le plus haut se situe à '+ str(miny))

        offsetx = minx -100
        offsety = miny -40
        pydirectinput.press('y') 
        pyautogui.moveTo(offsetx, offsety)
        pydirectinput.press('q') 
        try:
            ennemy = pyautogui.locateOnScreen("images/1.png", confidence=0.95)
            time.sleep(0.3)
            pyautogui.moveTo(ennemy[0]+40,ennemy[1]+70)
            print('hello')
        except TypeError:
            print('failed q spell')
        pydirectinput.press('y')  

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
        if time.time() > (self.passiveCooldown +30):
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
        self.gold = self.yuumiState["currentGold"]
        self.yuumiItems = self.teamState[self.yuumiIndex]["items"]
        self.nombreItems = len(self.yuumiItems)
        self.yuumiMana = self.yuumiState["championStats"]["resourceValue"]
        self.resourceMax = self.yuumiState["championStats"]["resourceMax"]



#            

        self.action()

    def action(self):
        return False

class lobby():
    print(' select your port ')
    port = 58152
    print('select your passowrd')
    password = '2ehR3LwHyn8SilA0qZmv6Q'
    username = 'riot'
    champion = 350
    host = '127.0.0.1'
    protocol = 'https'

def statuscheck():
    # roleselect = pyautogui.locateOnScreen("images/roleselect.jpg", grayscale=False,confidence=0.80)
    # role1selected = pyautogui.locateOnScreen("images/role1selected.jpg", grayscale=False,confidence=0.8)
    # role2selected = pyautogui.locateOnScreen("images/role2selected.jpg", grayscale=False,confidence=0.8)
    # mainmenu = pyautogui.locateOnScreen("images/mainmenu.jpg", grayscale=False,confidence=0.80)
    # queueselect = pyautogui.locateOnScreen("images/queueselect.jpg", grayscale=False,confidence=0.95)
    # queueselected = pyautogui.locateOnScreen("images/queueselected.jpg", grayscale=True,confidence=0.99)
    # lowpriority = pyautogui.locateOnScreen("images/lowpriority.jpg", grayscale=False,confidence=0.9)
    # confirm= pyautogui.locateOnScreen("images/confirm.jpg", grayscale=False,confidence=0.9)
    # banchamp= pyautogui.locateOnScreen("images/banchamp.jpg", grayscale=False,confidence=0.9)
    # inqueue = pyautogui.locateOnScreen("images/inqueue.jpg", grayscale=False,confidence=0.8)
    # choseloadout = pyautogui.locateOnScreen("images/choseloadout.jpg", grayscale=False,confidence=0.8)
    # acceptqueue = pyautogui.locateOnScreen("images/acceptqueue.png", grayscale=False,confidence=0.8)
    # matchfound = pyautogui.locateOnScreen("images/matchfound.png", grayscale=False,confidence=0.8)
    Riot_adapter = HTTPAdapter(max_retries=1)   
    session = requests.Session()
    session.mount('https://127.0.0.1:2999/liveclientdata/allgamedata', Riot_adapter)

    print('status check')
    try:
        session.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify = False)
        print("Avant Chargement")
        time.sleep(1)
        # print("avant perso")
        perso = Personnage()
        # print("apres perso")
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



    # while True:
    #     sleep(1)
    #     r = request('get', '/lol-login/v1/session')

    #     if r.status_code != 200:
    #         print(r.status_code)
    #         continue

    #     # Login completed, now we can get data
    #     if r.json()['state'] == 'SUCCEEDED':
    #         break
    #     else:
    #         print(r.json()['state'])

    # summonerId = r.json()['summonerId']


    # # Main worker loop


    while True:
        r = request('get', '/lol-gameflow/v1/gameflow-phase')

        if r.status_code != 200:
            print(Back.BLACK + Fore.RED + str(r.status_code) + Style.RESET_ALL, r.text)
            continue
        print(Back.BLACK + Fore.GREEN + str(r.status_code) + Style.RESET_ALL, r.text)

        if phase =='PreEndOfGame':
            pyautogui.click(900,500)

        phase = r.json()
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







