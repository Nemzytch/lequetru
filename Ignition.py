from importlib.resources import path
import subprocess
import os
import time
import mouse 
import win32gui

os.startfile("C:\\Riot Games\\League of Legends\\LeagueClient.exe")
print("Starting League of Legends..")
time.sleep(30)

file_path = "C:\\Users\\Administrator\\Desktop\\lequetru\\start.py"
directory = "C:\\Users\\Administrator\\Desktop\\lequetru"
subprocess.Popen(["start", "cmd", "/k", file_path], shell = True, cwd = directory)
time.sleep(2)

xpos = 0
ypos = 500
width = 400
length = 500

def enumHandler(hwnd, lParam):
    #thetitle = win32gui.GetWindowText(hwnd)
    if win32gui.IsWindowVisible(hwnd):
        if '.exe' in win32gui.GetWindowText(hwnd):
            win32gui.MoveWindow(hwnd, xpos, ypos, width, length, True)


win32gui.EnumWindows(enumHandler, None)

