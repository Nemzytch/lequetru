from importlib.resources import path
import subprocess
import os
import time
import mouse 

os.startfile("C:\\Riot Games\\League of Legends\\LeagueClient.exe")
print("Starting League of Legends..")
time.sleep(15)

file_path = "C:\\Users\\Administrator\\Desktop\\lequetru\\start.py"
directory = "C:\\Users\\Administrator\\Desktop\\lequetru"
subprocess.Popen(["start", "cmd", "/k", file_path], shell = True, cwd = directory)



