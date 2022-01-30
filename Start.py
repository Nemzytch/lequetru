from subprocess import *
from time import sleep
import subprocess
import os
import sys
import time



# Path and name to the script you are trying to start
file_path = "Main.py" 
restart_timer = 2

subprocess.call(["git", "reset", "--hard", "HEAD"])
subprocess.call(["git", "pull"])
print('Updating')

def start_script():
    try:
        # Make sure 'python' command is available
        os.system("start /B start cmd.exe @cmd /k python Main.py")
        # Popen(['python', 'Main.py'])
        # # os.system('cmd /k "python main.py"')
        time.sleep(1)
        sys.exit()
    except:
        # Script crashed, lets restart it!
        handle_crash()
os.system("taskkill /f /im cmd.exe")
def handle_crash():
    sleep(restart_timer)  # Restarts the script after 2 seconds
    start_script()

start_script()