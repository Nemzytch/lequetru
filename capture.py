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
import mouse
    

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

ennemi_image = 'ennemi.png'
def locate_img(imgPath):
    global offset
    image_to_find = cv2.imread(imgPath)
    sct = mss()
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




def find_ennemi():
    ennemi = locate_img(ennemi_image)
    if ennemi != None:
        mouse.move(ennemi[0],ennemi[1])
    return ennemi
