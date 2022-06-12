import pymem
from pymem import Pymem

#Offsets
LocalPlayerOffset = 0x30E11FC        # This is always required to read other objects in games.
HealthOffset = 0x0D9C                # Object to read and use for script.

LOL = Pymem('League of Legends.exe') # Read process by name.

def read_object(LOL):
    Local = LOL.read_uint(LOL.base_address + LocalPlayerOffset)  # You can find tutorials of this in YT and in UC I think. How to find offs, use with base_adress etc.
    return LOL.read_float(Local + HealthOffset)                  #Reading and return the value (in this case is float 0.0+)

print(read_object(LOL)) # and that's all!

#Or even re-write objects:

def write_object(LOL):
    Local = LOL.read_uint(LOL.base_address + LocalPlayerOffset)
    LOL.write_float(Local + HealthOffset, 9999.0)

write_object(LOL)

#Obviulsy you will not change any value if you want to maintain it safe..