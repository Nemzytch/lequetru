import json
from enum import Enum
import random
import time
import pydirectinput
import keyboard
 

LAST_TIMER_MSG = 0

f = open('msg.json',)
JsonMsg = json.load(f)
f.close()

### STATIC VAR ########
TIMER_EARLY_GAME = 600
TIMER_MID_GAME = 1200
TIMER_LATE_GAME = 1800

class DeathEvent(Enum): 
    Adc="Adc"
    Me="Me"
    Other="Other"
    Ace="Ace"
    Penta="Penta"
    Special="Special"

class GameEvent(Enum): 
    Inib="Inib"
    Tower="Tower"
    Nashor="Nashor"
    Drake="Drake"
    Special="Special"

class Classic(Enum): 
    End = "End"
    Begin = "Begin"
    Motivation = "Motivation"
class SpellYuumi(Enum): 
    Qspell = "Qspell"
    Wspell = "Wspell"
    Espell = "Espell"
    Rspell = "Rspell"
    Pspell = "Pspell"


JsonPath1 = None
JsonPath2 = None
JsonPath3 = None
text = ""

## Tool Def ################## 
def RandForMsgAndSetString(ListSort,InputValue):
    index=0
    ListIndex = []
    for msg in ListSort :
        index = index + msg["PowerRand"]
        ListIndex.append(index)

    _randomIndex = random.randint(0, index)
    indexChoise = 0
    msgChoise = 0
    for idx,msg in enumerate(ListIndex) : 
        if  _randomIndex <= msg:
            indexChoise = idx
            break
    for idx,msg in enumerate(ListSort) :
        if idx ==indexChoise :
            msgChoise = msg
            break
    if msgChoise !=0:
        SetTextToDisplay(msgChoise,InputValue)
        return True
    else:
        print("ErreurRand")
        return False


def SetLastTime(msg):
    msg["DernierEnvoie"] = time.time()

def SetTextToDisplay(msg,InputValue):
    global text
    StringToDisplay = msg["Content"]
    if msg["NeedValueInput"] == 1:

        listText = StringToDisplay.split('#')
        StringToDisplay = listText[0] + InputValue + listText[1]
    if msg["All"] == True:
        StringToDisplay = "/all " + StringToDisplay 
    text = StringToDisplay



    ## SUB list Def################## 
def SubListBasedOnDeltaTime(ListSort):
    ListSortDeltaTime = []  
    for msg in ListSort:
        if time.time() -msg["DernierEnvoie"]>= msg["TimerDernierEnvoie"] :
            ListSortDeltaTime.append(msg)
    if len(ListSortDeltaTime) == 0:
        print("plus de msg SubListBasedOnDeltaTime")
    return ListSortDeltaTime

def SubListCheckIfInputValue(ListSort,ValueInput):
    ListSortWithoutInputValue = []
    if ValueInput == 0 or "" :
        for msg in ListSort:
            if msg["NeedValueInput"] == 0:
                ListSortWithoutInputValue.append(msg)
        return  ListSortWithoutInputValue 
    else :
        return  ListSort      

def SubListSortByAttribute(Attribute,ListSort) :
    ListSortAttribute = []  
    for msg in ListSort :
        if Attribute == msg["Attribute"]:
            ListSortAttribute.append(msg)  
    if len(ListSortAttribute) == 0:
        print("No msg with this attribute "+Attribute)    
    return ListSortAttribute

def SubListBasedOnTimer(TimerGame,ListMsg):
    ListSort = []
    if TimerGame < TIMER_EARLY_GAME :
        for msg in ListMsg :
            if  msg["EarlyGame"] == True:
                ListSort.append(msg)
    elif TimerGame >= TIMER_EARLY_GAME and TimerGame < TIMER_MID_GAME :
        for msg in ListMsg :
            if  msg["MidGame"] == True:
                ListSort.append(msg)
    else :
        for msg in ListMsg :
            if  msg["LateGame"] == True:
                ListSort.append(msg)
    if len(ListSort) == 0:
        print("plus de msg SubListBasedOnTimer ERREUR")
    return ListSort

    ##PRINT MSG ###############
def WriteMsg(text):
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    keyboard.write(text)
    keyboard.press_and_release('enter')


    ## Main Def ################## 
def Msg(Event,IsAlly,ProbaEvent,TimerGame,ValueInput,Attribute) : 
    global text
    global LAST_TIMER_MSG
    if LAST_TIMER_MSG < TimerGame -300 :
        if checkTypeOfEvent(Event,IsAlly) :
            if random.randint(0, 100)<= ProbaEvent :
                ListMsg = ReadJson()
                print(ListMsg)
                ListSort = SubListBasedOnTimer(TimerGame,ListMsg) 
                ListSort = SubListSortByAttribute(Attribute,ListSort)
                ListSort = SubListCheckIfInputValue(ListSort,ValueInput)
                ListSort = SubListBasedOnDeltaTime(ListSort)
                RandForMsgAndSetString(ListSort,ValueInput)
                WriteMsg(text)
                LAST_TIMER_MSG = TimerGame
                print(text)
            else :
                print("BadLuck")
        else :
            print("ErrorMsg")
    else : print("Msg resament envoyer")

    ## Path JSON ##################

def GetEnum(Event):
    global JsonPath3
    JsonPath3 = Event.value

def checkTypeOfEvent(Event,IsAlly):
    global JsonPath2
    global JsonPath1
    if IsAlly :
        JsonPath2 = "Ally"
    else :
        JsonPath2 = "Ennemy"

    if type(Event) == DeathEvent :
        JsonPath1 = "DeathEvent"
        GetEnum(Event)
        return True
    elif type(Event) == GameEvent :
        JsonPath1 = "GameEvent"
        GetEnum(Event)
        return True
    elif type(Event) == Classic :
        JsonPath1 = "Classic"
        GetEnum(Event)
        JsonPath2 = "Ally"
        return True
    elif type(Event) == SpellYuumi :
        JsonPath1 = "SpellYuumi"
        GetEnum(Event)
        JsonPath2 = "Ally"
        return True
    else :
        print ("Erreur d'event")
        return False
    
    ##################  

    ## Read JSON ##################
def ReadJson() :
    ListMsg = JsonMsg[JsonPath1][JsonPath2][JsonPath3]
    return ListMsg


def Send_Msg():
    Msg(GameEvent.Drake,True,100,2,"","")

#keyboard.add_hotkey("j",Send_Msg)
#keyboard.wait()




