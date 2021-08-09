import requests
import urllib3
import json
from base64 import b64encode
from time import sleep
from colorama import Fore, Back, Style
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class lobby():
    print(' select your port ')
    port = 49930
    print('select your passowrd')
    password = '_wwNN3bfIyAUTE1S6HUH4w'
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
        r = fn(url, verify=False, headers=headers)
    else:
        r = fn(url, verify=False, headers=headers, json=data)

    return r



userpass = b64encode(bytes('%s:%s' % (lobby.username, lobby.password), 'utf-8')).decode('ascii')
headers = { 'Authorization': 'Basic %s' % userpass }
print(headers['Authorization'])

# Create Request session
s = requests.session()



while True:
    sleep(1)
    r = request('get', '/lol-login/v1/session')

    if r.status_code != 200:
        print(r.status_code)
        continue

    # Login completed, now we can get data
    if r.json()['state'] == 'SUCCEEDED':
        break
    else:
        print(r.json()['state'])

summonerId = r.json()['summonerId']


# Main worker loop


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



        actorCellId = -1

        for member in cs['myTeam']:
            if member['summonerId'] == summonerId:
                actorCellId = member['cellId']

        if actorCellId == -1:
            continue

        for action in cs['actions'][0]:
            if action['actorCellId'] != actorCellId:
                continue
            #pick yuumi
            if action['championId'] == 0:
                url = '/lol-champ-select/v1/session/actions/%d' % action['id']
                data = {'championId': 350}

                # Pick champion
                r = request('patch', url, '', data)
                print(r.status_code, r.text)

                # Lock champion
                if action['completed'] == False:
                    r = request('post', url+'/complete', '', data)
                    print(r.status_code, r.text)

    elif phase == 'InProgress':
        print('in progress')
    else:
            sleep(3)



    sleep(0.5)

