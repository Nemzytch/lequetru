import subprocess
import os
import time

file_path = "start.py" 

time.sleep(10)
os.startfile("C:\\Riot Games\\League of Legends\\LeagueClient.exe")
print("Starting League of Legends..")
time.sleep(100)


subprocess.Popen(["start", "cmd", "/k", file_path], shell = True)