import pyautogui
import keyboard
import random


# take a screenshot of the screen and save it in the screenshots folder with a name generated randomly

def screenshot():
    pyautogui.screenshot('screenshots/' + str(random.randint(1, 1000000)) + '.png')


#bind the screenshot function to the F12 key   

keyboard.add_hotkey('f12', screenshot)

keyboard.wait('esc')


