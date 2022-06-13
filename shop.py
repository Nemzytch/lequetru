import contextlib
import json
from platform import machine
import pydirectinput
import time
import pyautogui
import keyboard

golds =2501
LASTSHOP = time.time()
itemInInventory = ["Shard of True Ice"]
time.sleep(3)
with open('items.json') as f:
    items = json.load(f)
    data = items['data']

def canBuy(GOLDS,itemInInventory):
    # itemList = ["Shard of True Ice", "Imperial Mandate", "Ardent Censer", "Staff of Flowing Water", "Dark Seal", "Chemtech Putrifier", "Redemption"]
    itemListIDs = ["3853","4005","3504","6616","1082","3011","3107"]
    #find the items in items.json
    global data
    buyList = []
    with open('items.json') as f:
        items = json.load(f)
        data = items['data']
        for item in itemListIDs:
            if data[item]["gold"]["total"] < GOLDS and not data[item]["name"] in itemInInventory:
                buyList.append(data[item]["name"])
                GOLDS -= data[item]["gold"]["total"]
            elif "from" in data[item]:
                for key in data[item]["from"]:
                    if data[key]["gold"]["total"] < GOLDS and not data[key]["name"] in itemInInventory:
                        buyList.append(data[key]["name"])
                        GOLDS -= data[key]["gold"]["total"]
                    elif "from" in data[key]:
                        for key2 in data[key]["from"]:
                            if data[key2]["gold"]["total"] < GOLDS and not data[key2]["name"] in itemInInventory:
                                buyList.append(data[key2]["name"])
                                GOLDS -= data[key2]["gold"]["total"]

    return buyList




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
    pydirectinput.press('p')
    time.sleep(0.2)
    
if canBuy(golds,itemInInventory) != []:
    
    print("can buy:", canBuy(golds,itemInInventory), f"You have {str(golds)} golds left")
    cycle(canBuy(golds,itemInInventory))
    
    
# keyboard.add_hotkey('c', lambda: cycle(canBuy(golds,itemInInventory)))
# keyboard.wait()