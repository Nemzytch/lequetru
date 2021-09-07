import pyautogui
import time
import pydirectinput



def qspell():
    qX = 1250
    qY = 100    
    x =0
    ennemy = pyautogui.locateOnScreen("images/1.png", confidence=0.95)
    for pos in pyautogui.locateAllOnScreen('images/minions.png'):
        x = x+1
        qX = pos[0]
        qY = pos[1]
        if pos[0] < qX:
            qX = pos[0]
        if pos[1] < qY:
            qY = pos[1]
        if pos[0] == None:
            print('no minions')
            qX = ennemy[0]
            qY = ennemy[1]
    
    if qX != None:
        print(qX,qY)
        offsetx = qX -100
        offsety = qY -40
        pyautogui.moveTo(offsetx, offsety)
        pydirectinput.press('q') 
        try:
            ennemy = pyautogui.locateOnScreen("images/1.png", confidence=0.95)
            time.sleep(0.3)
            pyautogui.moveTo(ennemy[0]+40,ennemy[1]+70)
            print('hello')
        except TypeError:
            print('failed q spell')
    time.sleep(0.5)
    qspell()
qspell()

