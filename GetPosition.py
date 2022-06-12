from DataFunc import *
from keyboard import is_pressed
from time import sleep
import os
import time

def getPos():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    view_proj_matrix, width, height = find_view_proj_matrix(LOL)
    champions = [read_object(LOL, pointer) for pointer in champion_pointers]
    
    x, y = None, None
    for i in champions:
        x, y = world_to_screen(view_proj_matrix, width, height, i.x, i.z, i.y)
        print('{} in Screen Position: x= {} ; y= {}'.format(i.name, x, y))
    
    return x, y

while not is_pressed('k'):
    before =time.time()
    getPos()
    after = time.time()
    print(f'Time: {after - before}')
    sleep(0.01)
    
