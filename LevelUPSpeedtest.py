
import pydirectinput
import timeit
import time

time.sleep(3)

eLevel = 4
rLevel = 2
qLevel = 3
wLevel = 4
YuumiLevel =10
abilityLevel = 2

def LevelUP():
    global YuumiLevel
    global abilityLevel
        # MaxA = ["Z","A","E","A","E","A","R","E","A","E","A","R","E","E","Z","Z","R","Z","Z"]
    levelUpOrder = ["W","E","Q","E","Q","E","R","E","Q","E","Q","R","Q","Q","W","W","R","W","W"]
    spellToUp = levelUpOrder[YuumiLevel]
    desiredSpellLevel = levelUpOrder[:YuumiLevel+1].count(spellToUp)
    if abilityLevel < desiredSpellLevel:
        keyTo_Press = spellToUp
        pydirectinput.keyDown('ctrl')
        pydirectinput.press(keyTo_Press.lower())
        pydirectinput.keyUp('ctrl')

def LevelUPZ():
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('r')
        pydirectinput.press('q')
        pydirectinput.press('w')
        pydirectinput.press('e')
        pydirectinput.keyUp('ctrl')  
        
        
# def switchCase(case):

#     switcher{
#         5 >= yuumiState['abilities']['r']['abilityLevel'] : {pydirectinput.keyDown('ctrl'),pydirectinput.presS('r'),pydirectinput.keyUp('ctrl')}
#         5 >= yuumiState['abilities']['q']['abilityLevel'] : {pydirectinput.keyDown('ctrl'),pydirectinput.presS('q'),pydirectinput.keyUp('ctrl')}
#         5 >= yuumiState['abilities']['w']['abilityLevel'] : {pydirectinput.keyDown('ctrl'),pydirectinput.presS('w'),pydirectinput.keyUp('ctrl')}
#         5 >= yuumiState['abilities']['e']['abilityLevel'] : {pydirectinput.keyDown('ctrl'),pydirectinput.presS('e'),pydirectinput.keyUp('ctrl')}
#     }
#     switcher.get(True)

    
print(timeit.timeit(LevelUP, number=5),"seconds for Nemzy")
print(timeit.timeit(LevelUPZ, number=5), "seconds for Turtle")