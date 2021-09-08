import json
import requests
import time
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError
from requests.packages.urllib3.util.retry import Retry
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3
from ScriptMsg import Msg 
from ScriptMsg import GameEvent
from ScriptMsg import DeathEvent
from ScriptMsg import Classic
from ScriptMsg import SpellYuumi
import keyboard
from operator import itemgetter, attrgetter


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #  

datas = "a"
datas_events = ""

OffSetEvent = {'GameStart':60,'DragonKill':30,"NashorKill":30,"InhibKill":10,"Multikill":30,"TurretKilled":15,"ChampionKill":30}

PlayersTeamDic= {}
PlayersNameDic={}

NAME_YUUMI = "Yuumi"
NAME_YUUMI_ACCOUNT = ""
TEAM_YUUMI = ""
NAME_ADC_ACCOUNT = ""


EventList = []

EventQueue = []
EventLastIndexCheck = -1

PlayerIsSetup = False

def fetchDatas():
    response = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify = False).text
    return json.loads(response)

def SetupPlayerList():
    global datas
    DatasAllPlayers = datas["allPlayers"]
    index = 0
    global PlayersTeamDic
    global PlayersNameDic

    global NAME_YUUMI_ACCOUNT
    global TEAM_YUUMI
    global NAME_ADC_ACCOUNT

    for player in datas["allPlayers"] :
        if DatasAllPlayers[index]['championName'] == NAME_YUUMI:
            NAME_YUUMI_ACCOUNT = DatasAllPlayers[index]['summonerName']
            TEAM_YUUMI = DatasAllPlayers[index]['team']
            NAME_ADC_ACCOUNT=DatasAllPlayers[index-1]['summonerName']
        PlayersTeamDic.update({DatasAllPlayers[index]['summonerName']:DatasAllPlayers[index]['team']})
        PlayersNameDic.update({DatasAllPlayers[index]['summonerName']:DatasAllPlayers[index]['championName']})
        index = index +1
    print(PlayersTeamDic)


def UpdateEvent():
    global datas_events
    datas_events = datas['events']['Events']

def UpdateData():
    global datas 
    global PlayerIsSetup
    datas = fetchDatas()
    if not PlayerIsSetup :
        PlayerIsSetup = True
        SetupPlayerList()
    UpdateEvent()

class Event:
    def __init__(self,ID,Name,KillerName,Attribute,Value):
        self.ID = ID
        self.Name = Name
        self.KillerName = KillerName
        self.Attribute = Attribute
        self.Value = Value
    def __repr__(self):
        return repr((self.ID, self.Name, self.KillerName,self.Attribute,self.Value))

def FilterDataEvent(EventJson):
    global OffSetEvent
    if EventJson['EventName'] == "GameStart" :
        return Event(EventJson['EventID'],"GameStart","","",EventJson['EventTime'] +OffSetEvent["GameStart"] )
    elif EventJson['EventName'] == "DragonKill" :
        return Event(EventJson['EventID'],"DragonKill",EventJson['KillerName'],EventJson['Stolen'],EventJson['EventTime'] +OffSetEvent["DragonKill"] )
    elif EventJson['EventName'] == "NashorKill" :
        return Event(EventJson['EventID'],"NashorKill",EventJson['KillerName'],EventJson['Stolen'],EventJson['EventTime'] +OffSetEvent["NashorKill"])
    elif EventJson['EventName'] == "InhibKill" :
        return Event(EventJson['EventID'],"InhibKill",EventJson['KillerName'],"",EventJson['EventTime'] +OffSetEvent["InhibKill"])
    elif EventJson['EventName'] == "Multikill" :
        return Event(EventJson['EventID'],"Multikill",EventJson['KillerName'],EventJson['KillStreak'],EventJson['EventTime'] +OffSetEvent["Multikill"])  
    elif EventJson['EventName'] == "TurretKilled" :
        return Event(EventJson['EventID'],"TurretKilled",EventJson['KillerName'],"",EventJson['EventTime'] +OffSetEvent["TurretKilled"])      
    elif EventJson['EventName'] == "ChampionKill" :
        return Event(EventJson['EventID'],"ChampionKill",EventJson['KillerName'],EventJson['VictimName'],EventJson['EventTime'] +OffSetEvent["ChampionKill"])  
        


def GetEvent():
    global datas_events
    _last_datas_events = []
    EventChoise = ""
    _IndexFirstForRange =20
    if len(datas_events) < 20 :
       _IndexFirstForRange = len(datas_events) 
    for event in range(len(datas_events)-_IndexFirstForRange,len(datas_events)) :
        if datas_events[event]['EventName'] in OffSetEvent :
            _last_datas_events.append(FilterDataEvent(datas_events[event]))
    for event in _last_datas_events :
        if EventChoise == "" :
            EventChoise = event
        else : 
            if EventChoise.Value < event.Value:
                EventChoise = event
    return EventChoise



def SendMsgForEvent():
    
    global PlayersTeamDic
    global PlayersNameDic

    global NAME_YUUMI_ACCOUNT
    global TEAM_YUUMI
    global datas
    global NAME_ADC_ACCOUNT
    global datas_events
    TimerGame = datas['gameData']['gameTime']
    IsAlly = True
    KillerName = ""

    if True : # SI YUUMI EST ENTRAIN DE RIEN FAIRE
        event  = GetEvent()
        if event.Value > TimerGame -60:
            if event != "" :
                if event.KillerName in PlayersTeamDic:
                    KillerName = event.KillerName
                    KillerName = PlayersNameDic[KillerName]
                    if PlayersTeamDic[event.KillerName] == TEAM_YUUMI:
                        IsAlly = False
                    else :
                        IsAlly = True
                if event.Name == "GameStart":
                    Msg(Classic.Begin,IsAlly,100,TimerGame,KillerName,event.Attribute)
                elif event.Name == "DragonKill":
                    Msg(GameEvent.Drake,IsAlly,80,TimerGame,KillerName,event.Attribute)
                elif event.Name == "NashorKilled":
                    Msg(GameEvent.Nashor,IsAlly,80,TimerGame,KillerName,event.Attribute)
                elif event.Name == "TurretKilled":
                    Msg(GameEvent.Tower,IsAlly,0,TimerGame,KillerName,event.Attribute)
                elif event.Name == "InibKill":
                    Msg(GameEvent.Inib,IsAlly,0,TimerGame,KillerName,event.Attribute) 
                elif event.Name == "Multikill":
                    if event.Attribute >3:
                        Msg(DeathEvent.Penta,IsAlly,80,TimerGame,KillerName,event.Attribute) 
                elif event.Name == "ChampionKill":
                    if event.KillerName == NAME_YUUMI_ACCOUNT:
                        Msg(DeathEvent.Me,False,70,TimerGame,"","")
                    elif event.KillerName == NAME_ADC_ACCOUNT:
                        Msg(DeathEvent.Adc,False,80,TimerGame,KillerName,"")
                    elif event.Attribute == NAME_YUUMI_ACCOUNT:
                        Msg(DeathEvent.Me,True,70,TimerGame,"","")
                    else:
                        Msg(DeathEvent.Other,IsAlly,30,TimerGame,KillerName,"")
        else :
            print("aucun event recent")


def MainMsg():
    UpdateData()
    SendMsgForEvent()

 
