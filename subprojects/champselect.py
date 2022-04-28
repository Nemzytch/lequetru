from logging import info
import os
import re
import sys 
import time
import datetime
import json
import math
import random
import mouse 
import termcolor
import cv2
from cv2 import validateDisparity
import win32api
import win32con
import requests
import pyautogui
import pytesseract
import pyscreeze
import keyboard
import pytesseract
import numpy as nm
import pydirectinput
from time import sleep
from PIL import ImageGrab
from random import randrange
from pyairtable import Table 
from pyairtable.formulas import match
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


# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

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
NumberSinged= 1
print('Number For Max Dudge With Singed is', NumberSinged)

#Account Status Check
API_KEY= "key181wgNDrYM2bms"
BASE_ID = "appHnr7cu8j1HlMC2"
table = Table(API_KEY, 'appHnr7cu8j1HlMC2', 'YUUMI')

def restart():
    print("argv was",sys.argv)
    print("sys.executable was", sys.executable)
    print("restart now")

    os.execv(sys.executable, ['python'] + sys.argv)

def fetchDatas():
    response = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify = False).text
    return json.loads(response)

def MouseClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

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
            try:
                os.system('taskkill /f /im "SystemSettings.exe"')
            except:
                print('no SystemSettings.exe')
            
        if phase =='EndOfGame':
            
            global NumberGamesToPlay
            #get the summoner name
            SummonerName = request('get', '/lol-summoner/v1/current-summoner').json()["displayName"]
            
            time.sleep(2)
            
            try:
                os.system('taskkill /f /im "SystemSettings.exe"')
                PopUpClose()
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
            
            #NumberGamesToPlay -1 + Integrations
            NumberGamesToPlay =NumberGamesToPlay -1
            print(NumberGamesToPlay,'avec le -1')
            
            for records in table.all():
                if records['fields']['IngameName'] == SummonerName:
                    recordId = records['id']
                    table.update(recordId, {"GamesToPlay": str(NumberGamesToPlay)})
            
            #Thanking Mates
            playAgain = pyautogui.locateOnScreen("images/playagian.JPG", confidence=0.90)
            pyautogui.click(playAgain)
            
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
            if tier == 'IRON' and division == 'IV' and leaguepoints == 0:
                print('One more account readyyyyy')
                table.update(recordId, {"PcName": "Finish"})
                SignOutt()
                
            if NumberGamesToPlay == 0:
                print('No more game to play, bye')
                SignOutt()
                    
            time.sleep(10)

        if phase =='Lobby':   
            QueueLockout = pyautogui.locateOnScreen("images/QueueLockout.png", confidence=0.90)
            AtemptToJoin = pyautogui.locateOnScreen("images/AtemptToJoin.png", confidence=0.90)
            OKEND = pyautogui.locateOnScreen("images/OKEND.JPG", confidence=0.90)
            IUnderstand = pyautogui.locateOnScreen("images/IUnderstand.JPG", confidence=0.70)
            GG = pyautogui.locateOnScreen('images/GG.png', grayscale=False,confidence=0.90)
            #DudgeTimer = pyautogui.locateOnScreen("images/DudgeTimer.JPG", confidence=0.90)
            
            print('need to pick lanes')
            r = request('put', '/lol-lobby/v2/lobby/members/localMember/position-preferences', data ={"firstPreference": "UTILITY","secondPreference":"MIDDLE",})
            sleep(2)
            r = request('post', '/lol-lobby/v2/lobby/matchmaking/search')
            
            try:
                Alarme = pyautogui.locateOnScreen("images/Alarme.png", confidence=0.80)
                if Alarme != None:
                    print('New Account Detected, going to pick some champs')
                    Store()
                IAgree = pyautogui.locateOnScreen("images/IAgree.JPG", grayscale=False,confidence=0.90)
                if IAgree != None:
                    print('I Agree')
                    pyautogui.click(IAgree[0]+80,IAgree[1]-20)
                    pyautogui.write('I Agree', interval=0.25)
                    time.sleep(2)
                    OKEND = pyautogui.locateOnScreen("images/OKEND.JPG", confidence=0.90)
                    pyautogui.click(OKEND)
                if IUnderstand != None:
                    print('I Understand')
                    pyautogui.click(IUnderstand)
                if GG != None:
                    print('GG')
                    pyautogui.click(GG)
                if OKEND != None:
                    print('OKEND')
                    pyautogui.click(OKEND)
            except: 
                print('No I Agree')
                
            if QueueLockout or AtemptToJoin != None:
                
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
                QueueLockout = pyautogui.locateOnScreen('images/QueueLockout.png')

                while(True):
                    
                    cord = (QueueLockout[0]+145, QueueLockout[1]+80, QueueLockout[0]+230, QueueLockout[1]+105)
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
            else:
                print('No QueueLockout detected')

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
                print('planning')
                # print('Looking to prepick yuumi')
                # SearchChamp = pyautogui.locateOnScreen("images/search.png", grayscale=False,confidence=0.90)
                # if SearchChamp != None:
                #     pyautogui.click(SearchChamp[0],SearchChamp[1])
                #     print("I am going to search Yuumi")
                #     pyautogui.write('Yuumi', interval=0.25)
                #     Yuumy = pyautogui.locateOnScreen("images/FaceDeYuumi.png", grayscale=False,confidence=0.90)
                #     try:
                #         if Yuumy[0] != None:
                #             pyautogui.click(Yuumy[0],Yuumy[1])
                #     except:
                #         print('No Yuumi detected')
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