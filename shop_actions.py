import contextlib
import json
from platform import machine
from timeit import timeit
import pydirectinput
import time
import keyboard
import requests
import urllib3
import capture
import mss
import ctypes
import mss
import numpy as np
import cv2
from PIL import Image
import time
from mss import mss
import time
import pyautogui
import ctypes
import win32api   


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
user32 = ctypes.windll.user32
screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)

height = 768
width = 1024
top =int((screenHeight-height)/2)
left = int((screenWidth-width)/2)
mon = {'top': top, 'left':left, 'width':width, 'height':height}

sct = mss()
sct_img = sct.grab(mon)
offset =[left,top]



itemList = [["Spellthief's Edge", 400, []], ['Oracle Lens', 0, []], ['Dark Seal', 350, []], ['Imperial Mandate', 2500, [['Kindlegem', 800], ['Bandleglass Mirror', 950]]], ['Ardent Censer', 2300, [['Amplifying Tome', 435], ['Forbidden Idol', 800], ['Amplifying Tome', 435]]], ['Staff of Flowing Water', 2300, [['Amplifying Tome', 435], ['Forbidden Idol', 800], ['Amplifying Tome', 435]]], ['Chemtech Putrifier', 2300, [['Oblivion Orb', 800], ['Bandleglass Mirror', 950]]], ['Redemption', 2300, [['Kindlegem', 800], ['Forbidden Idol', 800]]]]
    


def canBuy(GOLDS,itemList):
    buyList= []
    print("item list from canBuy FUNC: " + str(itemList))
    #try to buy the first item in the list if not enough money, try components of the item if not enough money, break
    if GOLDS < itemList[0][1]:
        print("Not enough gold for full item")
        if len(itemList[0][2]) > 0:
            print("Trying to buy components")
            for component in itemList[0][2]:
                if GOLDS >= component[1]:
                    print("Adding " + component[0] + " to buy list")
                    buyList.append(component[0])
                    #updating main item price
                    itemList[0][1] -= component[1]
                    #remove components from the components of the item
                    GOLDS -= component[1]
                    itemList[0][2].remove(component)
                    
    else:
        print("Adding " +str(itemList[0][0]) + " to buy list")
        GOLDS -= itemList[0][1]
        buyList.append(itemList[0][0])
        itemList.pop(0)
        print(GOLDS)
            
    cycle(buyList)



def cycle(buyList):
    pydirectinput.press('p')
    time.sleep(0.2)
    for items in buyList:
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('l')
        pydirectinput.keyUp('ctrl')
        pyautogui.write((items).lower(), interval=0.10)
        time.sleep(0.2)
        pydirectinput.press('enter')
        time.sleep(0.2)
        time.sleep(0.2)
    pydirectinput.press('esc')
    buyList = []
    time.sleep(0.2)

def checkShopClosed():
    if capture.locate_img("images/openShop.png") is not None:
        print("Shop is open")
        pydirectinput.press('p')

    else:
        print("Shop is closed")
    
def fetchDatas():
    response = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify = False).text
    return json.loads(response)


def inventoryItemsAndGold():
    response = fetchDatas()
    golds = response["activePlayer"]["currentGold"]
    for _ in response["allPlayers"]:
        if _["championName"] == "Yuumi":
            api_stuff = _["items"]
    return [[_["displayName"] for _ in api_stuff], golds]


def updateItemList():
    global itemList
    itemInInventory = inventoryItemsAndGold()[0]
    golds = inventoryItemsAndGold()[1]
    print(f"item in inventory: {itemInInventory}")
    for item in itemList:
        if item[0] in itemInInventory:
            print(f"{item[0]} is already in inventory")
            itemList.remove(item)
    print(f"clean List: {str(itemList)}")
    canBuy(golds,itemList)
        
