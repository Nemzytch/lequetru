import subprocess
import os
import time

file_path = "C:\\Users\\Administrator\\Desktop\\lequetru"

time.sleep(10)
os.startfile("C:\\Riot Games\\League of Legends\\LeagueClient.exe")
print("Starting League of Legends..")
time.sleep(30)


subprocess.Popen(["start", "cmd", "/k", file_path], shell = True)