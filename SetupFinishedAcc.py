import requests
import os
from requests.adapters import HTTPAdapter
import urllib3
from base64 import b64encode 
import json
import re
import tableActions
import extraFuncs
from logger import logger
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def FinishAcc():

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

    def request(method, path, query='', data=''):
        url = f'{lobby.protocol}://{lobby.host}:{lobby.port}{path}?{query}' if query else f'{lobby.protocol}://{lobby.host}:{lobby.port}{path}'

        print(f"{method.upper().ljust(7, ' ')} {url} {data}")

        fn = getattr(s, method)

        return fn(url, verify=False, headers=headers, json=data) if data else fn(url, verify=False, headers=headers)

    userpass = b64encode(bytes('%s:%s' % (lobby.username, lobby.password), 'utf-8')).decode('ascii')
    headers = { 'Authorization': 'Basic %s' % userpass }
    print(headers['Authorization'])

    s = requests.session()
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
    
    def buyChamps():
        accid = request('get', '/lol-login/v1/session').json()['accountId']
        StoreUrl = request('get', '/lol-store/v1/getStoreUrl').json()
        ChampIDListLessCheap = [44,17,18,23,5]
            
        for champID in ChampIDListLessCheap:
            BoughtChampion = PostRequest( str(StoreUrl)+'/storefront/v3/purchase', data=({"accountId":accid,"items":[{"inventoryType":"CHAMPION","itemId":champID,"ipCost":1350,"quantity":1}]}))
            print(BoughtChampion.json())
            time.sleep(1)
            
    def Refund():
        accid = request('get', '/lol-login/v1/session').json()['accountId']
        StoreUrl = request('get', '/lol-store/v1/getStoreUrl').json()
        transactions = getrequest('https://euw.store.leagueoflegends.com/storefront/v3/history/purchase').json()['transactions']
        for champs in transactions:
            if champs['itemId'] in extraFuncs.getChampionIdList(["Senna", "Yuumi","Zed","Yasuo","Sion","Yone","LeeSin","Aatrox","BelVeth"]):
                if champs['refundable'] == True:
                    TransacID = champs['transactionId']
                    print(TransacID)
                    PostRequest( str(StoreUrl)+'/storefront/v3/refund', data=({"accountId":accid ,"transactionId":TransacID ,"inventoryType":"CHAMPION","language":"en_GB"})) 
                    
    def get_win_loss():
            puuid = request('get', '/lol-summoner/v1/current-summoner').json()['puuid']
            r = request('get', '/lol-ranked/v1/ranked-stats/'+puuid)
            wins = r.json()["queues"][0]["wins"]
            losses= r.json()["queues"][0]["losses"]
            print(str(wins)+"W/"+str(losses)+"L")
            return str(wins)+"W/"+str(losses)+"L"
        

    if tableActions.check_ingame_name(get_win_loss()) == False:
        ingame_name = request('get', '/lol-summoner/v1/current-summoner').json()["displayName"]
        tableActions.set_ingame_name(ingame_name,get_win_loss())
        print("Ingame name set to: "+ingame_name)
        
    Refund()
    
    class Player():
        loot = []
        lootChamps = []
        lootChests = []
        loot_chest_generic = []
        loot_chest_champion_mastery = []
        skin_list = []
        ingame_name = request('get', '/lol-summoner/v1/current-summoner').json()["displayName"]
        print("Player Name:", ingame_name)

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
        
    def setSkin():
        for items in Player.loot:
            _ = Player.loot[items]
            if _["displayCategories"] == "SKIN":
                skin_name = _['itemDesc']
                #remove special caracters from skin name
                skin_name = re.sub(r'[^\w]', ' ', skin_name)
                # skin_link = _["splashPath"]
                # #download the skin image and save it as "skin_name.png" in the subdirectory "skins"
                # r = request("get",skin_link)
                # with open(f'skins/{str(skin_name)}.png', 'wb') as f:
                #     f.write(r.content)
                
                Player.skin_list.append(skin_name)
                
        for chests in Player.loot_chest_generic:
            openChest("generic",chests[1],["CHEST_generic","MATERIAL_key"])
        for chests in Player.loot_chest_champion_mastery:
            openChest("champion_mastery",chests[1],["CHEST_champion_mastery","MATERIAL_key"])
        
        Player.loot =request('get', '/lol-loot/v1/player-loot-map').json()
        for champ in Player.lootChamps:
            championDisenchant(champ)
        print(Player.lootChamps,Player.loot_chest_generic,Player.loot_chest_champion_mastery)
        print(Player.skin_list)


    def lowPrioCheck():
        QueueLockout = None
        low_prio_time = "None"
        print("creating lobby")
        r =request('post','/lol-lobby/v2/lobby',data={"queueId": 420})
        time.sleep(0.5)
        print("picking roles")
        r = request('put', '/lol-lobby/v2/lobby/members/localMember/position-preferences', data ={"firstPreference": "UTILITY","secondPreference":"MIDDLE",})
        time.sleep(0.5)
        print("starting queue")
        r = request('post', '/lol-lobby/v2/lobby/matchmaking/search')
        time.sleep(0.5)
        r = request('get', '/lol-matchmaking/v1/search')
        print(r.json())
        if r.json()['isCurrentlyInQueue'] == False:
            low_prio_time = r.json()['lowPriorityData']['penaltyTimeRemaining']
            print(f"low priority time remaining {low_prio_time}")
            low_prio_time = str(low_prio_time/60)
        tableActions.set_low_priority(Player.ingame_name,low_prio_time)
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
                        print(lockoutTime)
                    #if  0 < error["penaltyTimeRemaining"] < 901: sleep = error["penaltyTimeRemaining"]
                    if 0 < error["penaltyTimeRemaining"] < 2000:
                        time.sleep(error["penaltyTimeRemaining"])
                        print("Sleeping for " + str(error["penaltyTimeRemaining"]))
        except Exception as e:
            print(e)
            pass
        return QueueLockout
    
    accid = request('get', '/lol-login/v1/session').json()['accountId']
    ChampionsCollection = request('get', '/lol-champions/v1/inventories/' + str(accid) + '/champions-playable-count').json()['championsOwned']
    if ChampionsCollection < 20:
        buyChamps()
    
    lowPrioCheck()
    for _ in range(3):
        PlayerLootMap()
        setLoot()
    setSkin()

    blue_essences = request('get', '/lol-loot/v1/player-loot-map').json()["CURRENCY_champion"]["count"]
    print(blue_essences)

    tableActions.set_blue_essence(Player.ingame_name,str(blue_essences))
    tableActions.set_skin_list(Player.ingame_name,str(Player.skin_list))