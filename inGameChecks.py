from timeit import timeit
import mss
from PIL import Image
import time
from mss import mss
import time
import pyautogui
import ctypes
import win32api    
import pydirectinput
import capture
import mouse
import keyboard
# import pyautogui


user32 = ctypes.windll.user32
screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)
height = 768
width = 1024
top =int((screenHeight-height)/2)
left = int((screenWidth-width)/2)

#___________ UI ELEMENTS ____________________
adcHp75Pixel =[1005+left,447+top]
adcHp50Pixel = [991+left,447+top]
ePosition = [481+left,724+top]


mon = {'top': top, 'left':left, 'width':width, 'height':height}
sct = mss()
sct_img = sct.grab(mon)
offset =[left,top]
lastQSpell = time.time()
lastUltimate = time.time()
lastHeal = time.time()
lastIgnite = time.time()
qX = 1
qY = 1


def qSpell():
    global mon
    sct_img = sct.grab(mon)
    global qX, qY
    x =0
    global lastQSpell
    ennemy = capture.locate_img("ennemi.png")
    if ennemy != None:
        print( "we gonna try to send q spell")
        for pos in pyautogui.locateAllOnScreen('images/minions.png',region =(left,top,left+width,top+height)):
            x = x+1
            qX = pos[0]
            qY = pos[1]
            if pos[0] < qX:
                qX = pos[0]
            if pos[1] < qY:
                qY = pos[1]
            if pos[0] is None:
                print('no minions')
                qX = ennemy[0]
                qY = ennemy[1]
        if qX != None:
            offsetx = qX -100
            offsety = qY -40
            mouse.move(offsetx, offsety)
        print("fire q spell")
        pydirectinput.press('q')
        try:
            time.sleep(0.3)
            ennemy = capture.locate_img("ennemi.png")
            if ennemy[0] > -40 and ennemy[0] < 1880 and ennemy[1] > -70 and ennemy[1] < 980:
                mouse.move(ennemy[0]+40,ennemy[1]+70)
            print("q spell finished")
            lastQSpell = time.time()
        
        except TypeError:
            print('failed q spell')
    else:
        print('no ennemies found for Q spell we add 10 sec')
        lastQSpell = lastQSpell + 10

def ultimateCast():
    global mon
    sct_img = sct.grab(mon)
    global lastUltimate
    if time.time() > (lastUltimate +70):
        try:
            ennemy = capture.locate_img("ennemi.png")
            mouse.move(ennemy[0]+100,ennemy[1]+40)
            pydirectinput.press('r')
            lastUltimate = time.time()
            print('ultimate casted')
        except TypeError:
            print("No ennemies found")
    
def hpAmount():

    FullLife = sct.grab({'mon':1, 'top':adcHp75Pixel[1], 'left':adcHp75Pixel[0], 'width':1, 'height':1})
    lowlife = sct.grab({'mon':1, 'top':adcHp50Pixel[1], 'left':adcHp50Pixel[0], 'width':1, 'height':1})
    g = FullLife.pixel(0,0)
    h = lowlife.pixel(0,0)
    if g[0] == 19 and g[1] == 19 and g[2] == 19:
        adc_sub_75 = True
        if h[0] == 19 and h[1] == 19 and h[2] == 19:
            adc_sub_50 = True
        else:
            adc_sub_50 = False
    else:
        adc_sub_75 = False
        adc_sub_50 = False
    return adc_sub_75, adc_sub_50
        
def sendEcheck():
    eScreen = sct.grab({'mon':1, 'top':ePosition[1], 'left':ePosition[0], 'width':1, 'height':1})
    e = eScreen.pixel(0,0)
    if e[1] > 200:
        pydirectinput.press('e')
        print("pressed E")
    else:
        print("Need to E but can't press it")


def ignite():
    global lastIgnite
    if time.time() > (lastIgnite + 180):
        global mon
        sct_img = sct.grab(mon)
        ennemy = capture.locate_img("ennemi.png")
        if ennemy!=None:
            print("Try ignite")
            mouse.move(ennemy[0]+40,ennemy[1]+100)
            pydirectinput.press('d')
            ignitePixel = sct.grab({'mon':1, 'top':708+top, 'left':564+left, 'width':1, 'height':1})
            g = ignitePixel.pixel(0,0)
            if g[2] > 100:
                print("ignite has been used")
                lastIgnite = time.time()
    else:
        print(f"ignite is on cooldown for {str(time.time()-lastIgnite)}")
                
                
def attached():
    global lastQSpell
    global lastHeal
    adc_sub_75, adc_sub_50 = hpAmount()
    if adc_sub_75 == True:
        sendEcheck()
    if adc_sub_50 == True:
        ultimateCast()
        ignite()
        print("Pressed Heal")
        if time.time()> (lastHeal+240):
            pydirectinput.press('f')
            print("Pressed Heal")
            lastHeal = time.time()
        sendEcheck()
    if adc_sub_75 == False and time.time() > (lastQSpell + 25):
        qSpell()


def inBase():
    FullLife = sct.grab({'mon':1, 'top':759+top, 'left':665+left, 'width':1, 'height':1})
    g = FullLife.pixel(0,0)
    if g[0] and g[1] and g[2] > 31:
        
        return True
    else:
        return False
