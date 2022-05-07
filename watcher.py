import os
import subprocess
import time
import psutil


for proc in psutil.process_iter():
    print(proc)
    if "Riot" or "riot" in proc.name():
        print("found " + proc.name())

        

    #find league of legends , or riot games in process list


#list all running process





