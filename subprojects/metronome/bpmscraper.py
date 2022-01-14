import webbrowser
import pyperclip
import pyautogui as pya
import time
import os
import json

# BPM_to_be_scraped = range(40,50)


# for number in BPM_to_be_scraped:
#     webbrowser.open('https://api.getsongbpm.com/tempo/?api_key=aa3b10bd345e9d7693c329252f24ca33&bpm='+str(number))
#     time.sleep(2)
#     pya.hotkey('ctrl', 'a')
#     time.sleep(0.2)
#     pya.hotkey('ctrl', 'c')
#     s = pyperclip.paste() 
#     with open(str(number)+'.json','w', encoding="utf-8") as g:
#         g.write(s)
#         print(str(number)+" file was created")
#     pya.hotkey('ctrl', 'w')

# JSON_FILES = [f for f in os.listdir('.') if f.endswith('.json')]
# for files in JSON_FILES:
#     with open(files, 'r+',encoding="utf-8") as f:
#         lines = f.readlines()
#         f.seek(0)
#         f.writelines(lines[6:])
#         f.truncate()
        
        
# # remove "song_id" from the json files
# with open('50.json', 'w') as dest_file:
#     with open('48.json', 'r') as source_file:
#         for line in source_file:
#             element = json.loads(line.strip())
#             if "tempo" in element:
#                 del element["song_id"]
#             dest_file.write(json.dumps(element))

# reparser le json pour avoir uniquement les tempos & les titres
def cleanJson():
    with open('49.json', 'r' ,encoding="utf-8") as f:
        data = json.load(f)
        for i in data["tempo"]:
            if "tempo" in i:
                print(i["tempo"])
                print(i["song_title"])
                print("\n")        
cleanJson()