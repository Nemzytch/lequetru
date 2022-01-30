from subprocess import run
from time import sleep
import subprocess


# Path and name to the script you are trying to start
file_path = "Main.py" 
restart_timer = 2

subprocess.call(["git", "reset", "--hard", "HEAD"])
subprocess.call(["git", "pull"])
print('Updating')

def start_script():
    try:
        # Make sure 'python' command is available
        subprocess.run("python "+file_path, check=True) 
    except:
        # Script crashed, lets restart it!
        handle_crash()

def handle_crash():
    sleep(restart_timer)  # Restarts the script after 2 seconds
    start_script()

start_script()