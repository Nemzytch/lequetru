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

    def checkHeal(self):
        screen=pyscreeze.screenshot()
        eCast=screen.getpixel((1041,1000))
        if eCast[1] > 248:
            print('adc needs healing')
            pydirectinput.press('f')
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
            if self.gold > self.stuff["items"][A]["price"]:
                if itemInTheSlot != desiredItem:
                    print("intem in the slot "+itemInTheSlot)
                    print("desired item"+desiredItem)
                    print('Item precedent non complété')
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
                    print(' adc is alive')
                    print('i am not attached ')
                    self.baseCheck()          
                    pyautogui.click(1861,603)                    
                    pydirectinput.press('w')  
                    print('goin to adc')

            if self.attached == True:
                print('yuumi is attached')
                self.hpCheck()
                if self.carryHP<40:
                    print(' Mon adc a '+str(self.carryHP)+'%HP')
                    self.checkHeal()
                    print('sendingheal')
                    # self.manacheckR()
                    self.ultimateCast()
                    print('send R')
                    self.manacheckE()
                    print('Healed ADC')
                if self.carryHP<85:
                    print(' Mon adc a '+str(self.carryHP)+'%HP')
                    self.manacheckE()
                    print('Healed ADC')
                if self.yuumiMana < (15*(self.resourceMax)/100):
                    print('you got '+ str(self.yuumiMana))
                    self.procPassive()

                else:
                    print('HP > 85%, no need to heal ')
            

            if self.adcDead == True:
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


def statuscheck():
    roleselect = pyautogui.locateOnScreen("images/roleselect.jpg", grayscale=False,confidence=0.80)
    role1selected = pyautogui.locateOnScreen("images/role1selected.jpg", grayscale=False,confidence=0.8)
    role2selected = pyautogui.locateOnScreen("images/role2selected.jpg", grayscale=False,confidence=0.8)
    mainmenu = pyautogui.locateOnScreen("images/mainmenu.jpg", grayscale=False,confidence=0.80)
    queueselect = pyautogui.locateOnScreen("images/queueselect.jpg", grayscale=False,confidence=0.95)
    queueselected = pyautogui.locateOnScreen("images/queueselected.jpg", grayscale=True,confidence=0.99)
    lowpriority = pyautogui.locateOnScreen("images/lowpriority.jpg", grayscale=False,confidence=0.9)
    confirm= pyautogui.locateOnScreen("images/confirm.jpg", grayscale=False,confidence=0.9)
    banchamp= pyautogui.locateOnScreen("images/banchamp.jpg", grayscale=False,confidence=0.9)
    inqueue = pyautogui.locateOnScreen("images/inqueue.jpg", grayscale=False,confidence=0.8)
    choseloadout = pyautogui.locateOnScreen("images/choseloadout.jpg", grayscale=False,confidence=0.8)
    acceptqueue = pyautogui.locateOnScreen("images/acceptqueue.png", grayscale=False,confidence=0.8)
    matchfound = pyautogui.locateOnScreen("images/matchfound.png", grayscale=False,confidence=0.8)
    Riot_adapter = HTTPAdapter(max_retries=1)   
    session = requests.Session()
    session.mount('https://127.0.0.1:2999/liveclientdata/allgamedata', Riot_adapter)


    try:
        session.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify = False)
        print("Avant Chargement")
        time.sleep(1)
        # print("avant perso")
        perso = Personnage()
        # print("après perso")
    except ConnectionError as ce:
        print("you aren't in game")

    if acceptqueue != None:
        print('matchfound')
        acceptqueue = pyautogui.locateOnScreen("images/acceptqueue.png", grayscale=False,confidence=0.8)
        print('accepting the queue')
        pyautogui.click(acceptqueue[0],acceptqueue[1])
        time.sleep(5)
        statuscheck()

    if choseloadout!= None:
        print('champion picked, waiting game to start')

    DeclareUrChamp = pyautogui.locateOnScreen("images/DeclareUrChamp.png", grayscale=False,confidence=0.90)
    if DeclareUrChamp != None:

        print('Time to declare your champion')
        
        SearchChamp = pyautogui.locateOnScreen("images/search.png", grayscale=False,confidence=0.90)
        if SearchChamp != None:

            pyautogui.click(SearchChamp[0],SearchChamp[1])
            print("I am going to search Yuumi")
            pyautogui.write('Yuumi', interval=0.25)
            Yuumy = pyautogui.locateOnScreen("images/FaceDeYuumi.png", grayscale=False,confidence=0.90)

            if Yuumy[0] != None:
                pyautogui.click(Yuumy[0],Yuumy[1])
    
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
            time.sleep(3)
            if Bannissement != None:
                pyautogui.click(Bannissement[0],Bannissement[1])
            else: 
                print("cant find ban button")

    Lockin = pyautogui.locateOnScreen("images/Lockin.jpg", grayscale=False,confidence=0.70)
    if Lockin != None:
        pyautogui.click(Lockin[0],Lockin[1])
        print("Champion Lock Nigga !")
    Fleche = pyautogui.locateOnScreen("images/Fleche.jpg", grayscale=False,confidence=0.70)
    if Fleche != None:
        if Fleche[0] != -1:
            pyautogui.click(Fleche[0], Fleche[1])

            print('Yesss')

    PlayAgain = pyautogui.locateOnScreen("images/PlayAgain.jpg", grayscale=False,confidence=0.70)
    if PlayAgain != None:
        if PlayAgain[0] != -1:
            pyautogui.click(PlayAgain[0], PlayAgain[1])

            print('Go Another game')

    elif mainmenu !=None:
        print('main menu ')
        pyautogui.click(mainmenu[0], mainmenu[1])
    elif lowpriority !=None:
        print('you are in lowpriority queue, be patient')
    elif inqueue !=None:
        print('you are in queue')
    elif role2selected !=None:
        print('selected 2nd role, launch queue')
        findmatch = pyautogui.locateOnScreen("images/findmatch.jpg", grayscale=False,confidence=0.80)
        if findmatch!=None:
            pyautogui.click(findmatch[0],findmatch[1])
        else:
            print('Cant start queue yet')
    elif role1selected !=None:
        print('selected first role, need 2nd')
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
        time.sleep(3)
        mid = pyautogui.locateOnScreen("images/mid.jpg", grayscale=False,confidence=0.80)
        pyautogui.click(mid[0],mid[1])
    elif roleselect !=None:
        print('need to select 1st role')
        pyautogui.click(roleselect[0],roleselect[1])
        time.sleep(2)
        support = pyautogui.locateOnScreen("images/support.jpg", grayscale=False,confidence=0.80)
        pyautogui.click(support[0],support[1])


    elif queueselected !=None:
        print('queue selected, starting queue')
        pyautogui.click(confirm[0],confirm[1])

    elif queueselect !=None:
        print('selecting queue')
        pyautogui.click(queueselect[0], queueselect[1])

    
    else:
        print('i dont know where you at')
    statuscheck()


def main():
    statuscheck()
    return True

if __name__ == "__main__":
    main()







