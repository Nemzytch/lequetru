from importlib.resources import path
import subprocess
import os
import time
import mouse 
import win32gui
import ctypes


#__________ SCREEN ELEMENT __________________
user32 = ctypes.windll.user32
screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)

os.startfile("C:\\Riot Games\\League of Legends\\LeagueClient.exe")
print("Starting League of Legends..")
time.sleep(15)

file_path = "C:\\Users\\Administrator\\Desktop\\lequetru\\start.py"
directory = "C:\\Users\\Administrator\\Desktop\\lequetru"
subprocess.Popen(["start", "cmd", "/k", file_path], shell = True, cwd = directory)
time.sleep(3)

xpos = 0
ypos = 400
width = (screenWidth - 1024) / 2
length = 400

def enumHandler(hwnd, lParam):
    #thetitle = win32gui.GetWindowText(hwnd)
    if win32gui.IsWindowVisible(hwnd):
        if 'cmd.exe' in win32gui.GetWindowText(hwnd):
            win32gui.MoveWindow(hwnd, xpos, ypos, width, length, True)


win32gui.EnumWindows(enumHandler, None)

