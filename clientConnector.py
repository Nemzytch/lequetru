import os
import requests
import time
import urllib3
from base64 import b64encode
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError
from requests.packages.urllib3.util.retry import Retry
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

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
        print(r.json())
        time.sleep(1)
        itemClick ={
  "eventName": "lol-store-item-click",
  "pageName": "champions",
  "item.itemKey": "CHAMPION-16",
  "playerEnteredRP": "0",
  "itemCoordinates": "0,0",
  "pageArrivedBy": "store-navigation",
    "item.price.BE": "450",
  "spec": "high",
  "isLowSpecModeOn": "false"
}
        postData ={"accountId":2907981474809760,"items":[{"inventoryType":"CHAMPION","itemId":16,"ipCost":450,"rpCost":"null","quantity":1}]}
        # 
        # print(buyChamp.json())
        # clickItem = request('post', '/telemetry/v1/events/lol-store-item-click', data=itemClick)
        # buyChamp = request('post', '/telemetry/v1/events/league_store_2020', data=postData)
        
        #send standard post request to this adress : "https://euw.store.leagueoflegends.com/storefront/v3/purchase?language=en_GB"
        post = request('post', 'https://euw.store.leagueoflegends.com/storefront/v3/purchase?language=en_GB', data=postData)
        
        
statuscheck()
