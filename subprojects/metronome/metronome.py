import requests
import time 
import os
import json
import random
import numpy
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError
from requests.packages.urllib3.util.retry import Retry
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3
from base64 import b64encode
from time import sleep
from colorama import Fore, Back, Style
import math
import playsound
import vlc
from urllib.request import urlopen
from mutagen.mp3 import MP3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

gamedirs = [r'C:\Games\Garena\32787\LeagueClient',
            r'D:\Games\League of Legends']
os.system("")

def fetchDatas():
    response = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify = False).text
    return json.loads(response)

class lobby():
    username = 'riot'
    host = '127.0.0.1'
    protocol = 'https'
    gamedirs = [r'C:\Riot Games\League of Legends',
            r'D:\Games\League of Legends']
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

    def updateDatas(self):
        self.datas = fetchDatas()

# from requests.models import PreparedRequest
# url = 'https://api.getsongbpm.com/tempo'
# params = {'api_key': 'aa3b10bd345e9d7693c329252f24ca33', 'bpm':42 }
# req = PreparedRequest()
# req.prepare_url(url, params)
# print(req.url)



# API_KEY = 'aa3b10bd345e9d7693c329252f24ca33'
# data = URL_PARAM = {'api_key': API_KEY, 'bpm':42 }
# bpmlist =requests.get("https://api.getsongbpm.com/tempo/",params = {'api_key': API_KEY, 'bpm':42 }, verify = False)
# print(bpmlist)  


# r=requests.get("https://api.getsongbpm.com/tempo/", headers={'X-API-KEY':'aa3b10bd345e9d7693c329252f24ca33','bpm':'42'}, verify=False).text
# print(r)

# import cloudscraper

# scraper = cloudscraper.create_scraper() 
# print (scraper.get("https://api.getsongbpm.com/tempo/?api_key=aa3b10bd345e9d7693c329252f24ca33&bpm=42").text) 


# ______________________________ à tester

url = "https://api.getsongbpm.com/tempo/?api_key=aa3b10bd345e9d7693c329252f24ca33&bpm=42" 
payload={} 
headers = { 'X-API-KEY': 'aa3b10bd345e9d7693c329252f24ca33' } 
response = requests.request("GET", url, headers=headers, data=payload) 
print(response.text)




# url = "https://api.getsongbpm.com/tempo/?api_key=aa3b10bd345e9d7693c329252f24ca33&bpm=42"
# file = urllib.request.urlopen(url)

# for line in file:
# 	decoded_line = line.decode("utf-8")
# 	print(decoded_line)


# url = "https://api.getsongbpm.com/tempo/?api_key=aa3b10bd345e9d7693c329252f24ca33&bpm=42"
# response = urlopen(url)
# data_json = json.loads(response.read())
# print(data_json)








class Personnage:
    BPM = 0
    LastSongTime = 0
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
            print()
            print("Loading Screen")
        print("Game just started")
        f = open('stuff.json',)
        self.stuff = json.load(f)
        f.close()
        print('stuff loaded')
        i=0
        



    def __init__(self):
        self.setup()
        self.start()

        response = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify = False).text
        datas = json.loads(response)

        ManaActuel = datas["activePlayer"]["championStats"]["resourceValue"]
        print(ManaActuel)
        RegenMana = datas["activePlayer"]["championStats"]["resourceRegenRate"]
        print(RegenMana)

    def updatePerso(self):
        self.playerState = self.datas["activePlayer"]
        self.teamState = self.datas["allPlayers"]
        self.gold = self.playerState["currentGold"]
        self.yuumiItems = self.teamState[self.yuumiIndex]["items"]
        self.action()

    def action(self):
        return False



        
        
        
        
def statuscheck():
    Riot_adapter = HTTPAdapter(max_retries=1)   
    session = requests.Session()
    session.mount('https://127.0.0.1:2999/liveclientdata/allgamedata', Riot_adapter)

    print('status check')
    try:
        session.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify = False)
        response = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify = False).text
        # print(json.loads(response))
        time.sleep(0.5)
        Personnage.BPM = (json.loads(response)["activePlayer"]["championStats"]["attackSpeed"])*60
        print(Personnage.BPM)
        Songs = [['dearmama.mp3',43]]
        for _ in Songs:
            print(_)
            if math.ceil(Personnage.BPM) == _[1]:
                print(math.ceil(Personnage.BPM), _[1])
                duration = MP3(_[0]).info.length
                playTime = time.time()
                if playTime < Personnage.LastSongTime + duration:
                    print("already playing :", _[0])
                
                else :
                    print('found matching song, song name:', _[0])
                    media_player = vlc.MediaPlayer() 
                    media = vlc.Media(_[0]) 
                    media_player.set_media(media) 
                    media_player.audio_set_volume(25) 
                    media_player.play() 
                    Personnage.LastSongTime = time.time()
                
                
            else :
                print('no matching song')
                print(math.ceil(Personnage.BPM), _[1])
                
        time.sleep(5)
        statuscheck()
        
    except ConnectionError as ce:
        print("you aren't in game")






    print(' connecting to port '+str(lobby.port)+' with the password' +str(lobby.password))

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
                
        if phase =='None':
            time.sleep(3)
            print('waiting for ANYTYHING TO HAPPEN')

        sleep(0.5)
        
          
def main():
    statuscheck()
    return True

if __name__ == "__main__":
    main()



# récupérer l'attaque speed
# convertir l'attaque speed en bpm
