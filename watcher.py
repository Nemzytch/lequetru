import os
import subprocess
import time
import psutil


for proc in psutil.process_iter():
    print(proc)
    if proc.name() == "RiotClientUxRender.exe":
        print("found riot client ux render.exe")
    if proc.name() == "RiotClientUx.exe":
        print("found riot client ux.exe")
    if proc.name() == "RiotClient.exe":
        print("found riot client.exe")
    if proc.name() == "RiotClientCrashHandler.exe":
        print("found riot client crash handler.exe")
    

    #find league of legends , or riot games in process list


#list all running process





