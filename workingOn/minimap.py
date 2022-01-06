import cv2
import numpy as np
from shapely.geometry import Polygon
from shapely.geometry import Point
import pyautogui
import time
from operator import itemgetter, attrgetter
import colorama
from colorama import Fore, Back, Style
colorama.init()

before =time.time()




championiList = ['vladimir','sivir','ashe','blitzcrank','Yuumi']

t1BotBlue = [1795,1030,'Bot T1 tower blue side']
t2BotBlue = [1700,1030,'Bot T2 tower blue side']
t3BotBlue = [1630, 1034,'Bot T3 tower blue side']
t1MidBlue = [1666,909,'Mid T1 tower blue side']
t2MidBlue = [1642,941,'Mid T2 tower blue side']
t3MidBlue = [1609,972,'Mid T3 tower blue side']
t1TopBlue = [1542,800,'Top T1 tower blue side']
t2TopBlue = [1552,896,'Top T2 tower blue side']
t3TopBlue = [1544,953,'Top T3 tower blue side']
t1BotRed = [1795,1030,'Bot T1 tower red side']
t2BotRed = [1700,1030,'Bot T2 tower']

blueBuffRedSide = [1805,885,'Blue Buff']


PointSurLaCarte = [t1BotBlue,t2BotBlue,t3BotBlue,t1MidBlue,t2MidBlue,t3MidBlue,blueBuffRedSide,t2BotRed,t3BotRed,t1TopBlue,t2TopBlue,t3TopBlue]






RedSide = Polygon([[1547, 676], [1902, 1054], [1896, 684]])



for champion in championiList :
    distances = []
    position = pyautogui.locateOnScreen('images/champions/'+champion+'.png', confidence=0.64, region=(1520,670,1905,1065), grayscale=False)
    if position != None:
        print(champion +' was found in '+str(position[0]),str(position[1]))
        champCoordinates = Point(position[0],position[1])
        distance = 500
        for spots in keyPoint:
            if champCoordinates.distance(Point(spots[0],spots[1]))<distance:
                distance = champCoordinates.distance(Point(spots[0],spots[1]))
                actualSpot = (spots[2],champCoordinates.distance(Point(spots[0],spots[1])))


        if champCoordinates.distance(RedSide) > 0 :   
            print(Back.BLACK + Fore.BLUE + champion+'is at '+actualSpot[0]+ Style.RESET_ALL)
        else:
            print(Back.BLACK + Fore.RED + champion+'is at '+actualSpot[0]+ Style.RESET_ALL)




print(time.time()-before)
print('hello')






