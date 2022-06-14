import json
import os

GOLDS = 1550

# with open('items.json') as f:
#     items = json.load(f)
#     data = items['data']
#     f.close()

# itemListIDs = ["3850","3364","1082","4005","3504","6616","3011","3107"]

# def getItemList(itemListIDs):
#     itemList = []
#     currentItem = []
#     for item in itemListIDs:
#         if "from" in data[item]:
#             currentItem.append([data[item]["name"],data[item]["gold"]["total"],[]])
#             for key in data[item]["from"]:
#                 #add the sub item to the current item
#                 currentItem[-1][2].append([data[key]["name"],data[key]["gold"]["total"]])
#             print(currentItem,"curent item")
#             itemList.append(currentItem)
#             currentItem = []

#         else :
#             itemList.append([data[item]["name"],data[item]["gold"]["total"],[]])
#     return itemList

# print(getItemList(itemListIDs))

itemList = [["Spellthief's Edge", 400, []], ['Oracle Lens', 0, []], ['Dark Seal', 350, []], ['Imperial Mandate', 2500, [['Kindlegem', 800], ['Bandleglass Mirror', 950]]], ['Ardent Censer', 2300, [['Amplifying Tome', 435], ['Forbidden Idol', 800], ['Amplifying Tome', 435]]], ['Staff of Flowing Water', 2300, [['Amplifying Tome', 435], ['Forbidden Idol', 800], ['Amplifying Tome', 435]]], ['Chemtech Putrifier', 2300, [['Oblivion Orb', 800], ['Bandleglass Mirror', 950]]], ['Redemption', 2300, [['Kindlegem', 800], ['Forbidden Idol', 800]]]]

buyList = []

def canBuy(GOLDS,itemList):
    global buyList
    #try to buy the first item in the list if not enough money, try components of the item if not enough money, break
    if GOLDS < itemList[0][1]:
        print("Not enough gold for full item")
        if len(itemList[0][2]) > 0:
            print("Trying to buy components")
            for component in itemList[0][2]:
                if GOLDS >= component[1]:
                    print("Adding " + component[0] + " to buy list")
                    buyList.append(component[0])
                    GOLDS -= component[1]
                    canBuy(GOLDS,itemList)
    else:
        print("Adding " +str(itemList[0][0]) + " to buy list")
        GOLDS -= itemList[0][1]
        buyList.append(itemList[0][0])
        itemList.pop(0)
        print(GOLDS)
        if GOLDS > 400:
            canBuy(GOLDS,itemList)
        

print(canBuy(GOLDS,itemList))

print(buyList)