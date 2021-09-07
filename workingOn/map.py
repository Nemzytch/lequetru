import pyautogui



yuumiattached = pyautogui.locateOnScreen('images/yuumiattached.png', confidence=0.85)
pyautogui.moveTo(yuumiattached[0],yuumiattached[1])

