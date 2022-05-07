# importing os module
import os
 

#replace files in Config with files in folder2

for filename in os.listdir("Config"):
    #copy file from Config to folder2
    src = os.path.join("Config", filename)
    dst = os.path.join("C:\Riot Games\League of Legends\Config", filename)
    #replace file in folder2 with file in Config
    os.replace(src, dst)