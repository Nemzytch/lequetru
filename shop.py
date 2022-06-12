import contextlib
import json


GOLDS = 1700


itemList = ["Shard of True Ice", "Imperial Mandate", "Ardent Censer", "Staff of Flowing Water", "Dark Seal", "Chemtech Putrifier", "Redemption"]
itemListIDs = ["3853","4005","3504","6616","1082","3011","3107"]
#find the items in items.json



CompleteItemList = []
with open('items.json') as f:
    items = json.load(f)
    data = items['data']
    
    # #find the item in the itemList
    # for item in itemList:
    #     for key, value in data.items():
    #         if value['name'] == item:
    #             print(key)
    #             break
    
    for item in itemListIDs:
        print(data[item]["name"], data[item]["gold"]["total"])
        CompleteItemList.append(data[item]["name"])
        CompleteItemList.append(data[item]["gold"]["total"])
        
        # get the components of the item
        with contextlib.suppress(Exception):
            components = data[item]["from"]
            print(components)
            for component in components:
                print(data[component]["name"], data[component]["gold"]["total"])
                #get the components of the component
                with contextlib.suppress(Exception):
                    subcomponents = data[component]["from"]
                    for subcomponent in subcomponents:
                        print(data[subcomponent]["name"],  data[subcomponent]["gold"]["total"])
                        
                        
print(CompleteItemList)
                        
                        
                        
# buy as much item from the shop as possible, if cant buy item, buy component of the item, if cant buy component, buy component of the component, etc.



                