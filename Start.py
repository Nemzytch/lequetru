import imp
from subprocess import run
from time import sleep
import subprocess
import os
import time
import win32gui
import ctypes

time.sleep(1)

#__________ SCREEN ELEMENT RESIZE__________________
user32 = ctypes.windll.user32
screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)

xpos = 0
length = 400
ypos = 487
width = 345

def enumHandler(hwnd, lParam):
    #thetitle = win32gui.GetWindowText(hwnd)
    if win32gui.IsWindowVisible(hwnd):
        if 'cmd.exe' in win32gui.GetWindowText(hwnd):
            win32gui.MoveWindow(hwnd, xpos, ypos, width, length, True)


win32gui.EnumWindows(enumHandler, None)

# Path and name to the script you are trying to start
file_path = "Main.py" 
restart_timer = 2

subprocess.call(["git", "reset", "--hard", "HEAD"])
subprocess.call(["git", "pull"])
os.system('cpu.bat')

print('Updating')

def start_script():
    try:
        # Make sure 'python' command is available
        run("python "+file_path, check=True)
    except:
        handle_crash()
        # Script crashed, lets restart it!
        #try:
            #os.system('taskkill /f /im "LeagueClient.exe"')
            #os.system('taskkill /f /im "League of Legends.exe"')
            
            #time.sleep(10)
            
            #os.startfile("C:\Riot Games\League of Legends\LeagueClient.exe")
            #handle_crash()
        #except:
            #print("Could not restart script")
    

def handle_crash():
    sleep(restart_timer)  # Restarts the script after 2 seconds
    start_script()

start_script()