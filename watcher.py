import os
import subprocess
import time
import psutil


for proc in psutil.process_iter():
    print(proc)
    if proc.name() == "RiotClientUxRender.exe":
        print("found riot client ux render.exe")

    #find league of legends , or riot games in process list


#list all running process





