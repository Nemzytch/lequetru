import requests
import urllib3
import json
from base64 import b64encode
from time import sleep
from colorama import Fore, Back, Style
import pyautogui
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class lobby():
    print(' select your port ')
    port = 58953
    print('select your passowrd')
    password = 'gAs3BsxuScBMFb1impMrgg'
    username = 'riot'
    champion = 350
    host = '127.0.0.1'
    protocol = 'https'

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
        return fn(url, verify=False, headers=headers)
    else:
        return fn(url, verify=False, headers=headers, json=data)



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

    phase = r.json()

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
    else:
            sleep(1)

    sleep(0.5)