import requests
import os
from requests.adapters import HTTPAdapter
import urllib3
from base64 import b64encode 
import json
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class lobby():
    username = 'riot'
    champion = 350 
    host = '127.0.0.1'
    protocol = 'https'
    gamedirs = [r'C:\Riot Games\League of Legends',r'D:\Games\League of Legends',r'D:\Riot Games\League of Legends',]
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
    os.system('cls' if os.name == 'nt' else 'clear')
    Riot_adapter = HTTPAdapter(max_retries=1)   
    session = requests.Session()
    session.mount('https://127.0.0.1:2999/liveclientdata/allgamedata', Riot_adapter)

    print('status check')
    try:
        session.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify = False)
        print("Avant Chargement")
    except ConnectionError as ce:
        print("you aren't in game")

    print(' connecting to port '+str(lobby.port)+' with the password' +str(lobby.password)+ ' we will lock champ #'+ str(lobby.champion))


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
idtoken = request('get', '/lol-login/v1/session').json()['idToken']    
    
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
    print(TransacHistory)



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



def Refund():
    accid = request('get', '/lol-login/v1/session').json()['accountId']
    StoreUrl = request('get', '/lol-store/v1/getStoreUrl').json()
    transactions = getrequest('https://euw.store.leagueoflegends.com/storefront/v3/history/purchase').json()['transactions']
    for champs in transactions:
        if champs['itemId'] in [150,350,235,64,157,238,32,1,22,36,86,10,11,20,78,13,27,15,16,19,44,17,18,23,266,14]:
            if champs['refundable'] == True:
                TransacID = champs['transactionId']
                print(TransacID)
                PostRequest( str(StoreUrl)+'/storefront/v3/refund', data=({"accountId":accid ,"transactionId":TransacID ,"inventoryType":"CHAMPION","language":"en_GB"})) 

Refund()
class Player():
    loot = []
    lootChamps = []
    lootChests = []
    loot_chest_generic = []
    loot_chest_champion_mastery = []
    skin_list = []

def openChest(ID,repeat,data):
    chestUrl = f'/lol-loot/v1/recipes/CHEST_{str(ID)}_OPEN/craft'
    chestData = [f"CHEST_{str(ID)}"]
    if data!=None:
        chestData = data
    repeat = repeat = f"repeat={str(repeat)}"
    request ('post', chestUrl,query=repeat, data=chestData)
    
def championDisenchant(ID):
    champUrl = '/lol-loot/v1/recipes/CHAMPION_RENTAL_disenchant/craft'
    champID =  [f"CHAMPION_RENTAL_{str(ID)}"]
    request ('post', champUrl, data=champID)
    champUrl = '/lol-loot/v1/recipes/CHAMPION_disenchant/craft'
    champID =  [f"CHAMPION_{str(ID)}"]
    request ('post', champUrl, data=champID)
    

def keyCraft(keyNumber):
    keyUrl = "/lol-loot/v1/recipes/MATERIAL_key_fragment_forge/craft"
    data = ["MATERIAL_key_fragment"]
    fullKeys =f"repeat={str(keyNumber//3)}"
    request ('post', keyUrl,query=fullKeys, data=data)

def mythicForge(numberCurrency):
    url ="/lol-loot/v1/recipes/CURRENCY_mythic_forge_13/craft"
    fullKeys =f"repeat={str(numberCurrency//10)}"
    for _ in range (numberCurrency%10):
        request('post', url,query=fullKeys, data=["CURRENCY_mythic"])
    

def PlayerLootMap():
    Player.loot =request('get', '/lol-loot/v1/player-loot-map').json()
    with open('loot.json', 'w') as outfile:
        json.dump(Player.loot, outfile)


def setLoot():        
    
    #craft first keys/mythic capsules / champions capsule
    for items in Player.loot:
        _ = Player.loot[items]
        if _["lootId"] == "MATERIAL_key_fragment":
            keyCraft(_["count"])
        if _["lootId"] == "CURRENCY_mythic":
            mythicForge(_["count"])
        if _["displayCategories"] == "CHEST": 
            if _["storeItemId"] == 128:
                # print(_['count'])
                print(_["storeItemId"])
                openChest(_['storeItemId'],_['count'],None)
            if _["storeItemId"] == 145:
                # print(_['count'])
                print(_["storeItemId"])
                openChest(_['storeItemId'],_['count'],None)
            if _["storeItemId"] == 186:
                # print(_['count'])
                print(_["storeItemId"])
                openChest(_['storeItemId'],_['count'],None)
            else:
                #try to open it anyway
                openChest(_['storeItemId'],_['count'],None)
                print("chest found in wrong format "+str(_["storeItemId"]))
    Player.loot =request('get', '/lol-loot/v1/player-loot-map').json()  
    
    
    for items in Player.loot:
        _ = Player.loot[items]
        # print(_['displayCategories'])
        if _["displayCategories"] == "CHAMPION":
            print(_['count'])
            Player.lootChamps.append(_["storeItemId"])

        if _["displayCategories"] == "CHEST" and _["storeItemId"] ==1:
            Player.loot_chest_generic.append([_["storeItemId"],_['count']])
            
        if _["displayCategories"] == "CHEST" and _["storeItemId"] ==-1:
            Player.loot_chest_champion_mastery.append([_["storeItemId"],_['count']])
    

        if _["displayCategories"] == "SKIN":
            # print(_['itemDesc'])
            skin_name = _['itemDesc']
            #remove special caracters from skin name
            skin_name = re.sub(r'[^\w]', ' ', skin_name)
            skin_link = _["splashPath"]
            #download the skin image and save it as "skin_name.png" in the subdirectory "skins"
            r = request("get",skin_link)
            with open(f'skins/{str(skin_name)}.png', 'wb') as f:
                f.write(r.content)
            # print(f"skins/{skin_name}.png")
            Player.skin_list.append([skin_name])
            

    for chests in Player.loot_chest_generic:
        openChest("generic",chests[1],["CHEST_generic","MATERIAL_key"])
    for chests in Player.loot_chest_champion_mastery:
        openChest("champion_mastery",chests[1],["CHEST_champion_mastery","MATERIAL_key"])
    
    Player.loot =request('get', '/lol-loot/v1/player-loot-map').json()
    for champ in Player.lootChamps:
        championDisenchant(champ)
    print(Player.lootChamps,Player.loot_chest_generic,Player.loot_chest_champion_mastery)
    print(Player.skin_list)

PlayerLootMap()
setLoot()
            # openChest(_["storeItemId"],_['count'],None)
            # openChest("generic",_['count'],["CHEST_generic","MATERIAL_key"])
            # openChest("champion_mastery",_['count'],["CHEST_champion_mastery","MATERIAL_key"])