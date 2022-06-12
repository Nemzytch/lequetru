from timeit import timeit

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
import threading
import win32con

import keyboard
import mouse
# import pyautogui
    
    
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

def locate_img(imgPath):
    global offset
    image_to_find = cv2.imread(imgPath)
    sct_img = sct.grab(mon)
    
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    match = cv2.matchTemplate(img_bgr, image_to_find, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)
    
    if max_val > 0.95:
        x = max_loc[0]
        y = max_loc[1]
        print(f"found in {x+offset[0]},{y+offset[1]}")
        return [x+offset[0],y+offset[1]]


# def MouseClick():
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
#     time.sleep(0.01)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

# def RightClick():
#     win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0,0)
#     time.sleep(0.01)
#     win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0,0)


#Right click with mouse librairy
    
    


#get the mouse position

#block user mouse input
def blockMouse():
    while True:
        mouse.wait()
        
image = "ennemi.png"
ennemiOnScreen = False
ennemiPos= []
def mainFunc():
    global ennemiPos
    global ennemiOnScreen
    threading.Thread(target=locateEnnemi).start()
    if ennemiOnScreen == True:
        mousePosition = mouse.get_position()
        mouse.move(ennemiPos[0]+40,ennemiPos[1]+70)
        mouse.click(button='left')
        time.sleep(0.028)
        mouse.move(mousePosition[0],mousePosition[1])
        mouse.click(button='right')
        time.sleep(0.1)
    
    

keyboard.add_hotkey('c',mainFunc)
#loop to detect imgs

def locateEnnemi():
    global ennemiOnScreen
    global ennemiPos
    # while True:
    # for _ in range(2):
    ennemi =locate_img(image)
    if ennemi != None:
        ennemiPos = ennemi
        ennemiOnScreen = True
        print(ennemi)
    else:
        ennemiOnScreen = False
        print("no ennemi")
        
            




keyboard.wait()
# pyautogui.screenshot('screenshot.png',region=(left,top,width,height))

# image = 'ennemi.png'
# ennemi =locate_img(image)
# print(ennemi)

