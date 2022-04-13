import imp
from subprocess import run
from time import sleep
import subprocess
import os
import time

# Path and name to the script you are trying to start
file_path = "Main.py" 
restart_timer = 10

subprocess.call(["git", "reset", "--hard", "HEAD"])
subprocess.call(["git", "pull"])
print('Updating')

def start_script():
    try:
        # Make sure 'python' command is available
        run("python "+file_path, check=True)
    except:
        # Script crashed, lets restart it!
        try:
            os.system('taskkill /f /im "LeagueClient.exe"')
            os.system('taskkill /f /im "League of Legends.exe"')
            
            time.sleep(10)
            
            os.startfile("C:\Riot Games\League of Legends\LeagueClient.exe")
            handle_crash()
        except:
            print("Could not restart script")
    

def handle_crash():
    sleep(restart_timer)  # Restarts the script after 10 seconds
    start_script()

start_script()