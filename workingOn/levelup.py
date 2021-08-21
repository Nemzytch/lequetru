import pydirectinput 
#Test Values
yuumiLevel = 7
spellLevel = 4


#Level up fuction
# MaxE = ["Z","E","A","E","A","E","R","E","A","E","A","R","A","A","Z","Z","R","Z","Z"]
# MaxA = ["Z","A","E","A","E","A","R","E","A","E","A","R","E","E","Z","Z","R","Z","Z"]
levelUpOrder = ["Z","E","A","E","A","E","R","E","A","E","A","R","A","A","Z","Z","R","Z","Z"]
spellToUp = levelUpOrder[yuumiLevel]
desiredSpellLevel = levelUpOrder[0:yuumiLevel+1].count(spellToUp)

if spellLevel < desiredSpellLevel:
    print('you need to level up your ' + spellToUp + ' spell to level '+ str(desiredSpellLevel))
    pydirectinput.keyDown('ctrl')
    pydirectinput.press(spellToUp)
    pydirectinput.keyUp('ctrl')
else: 
    print('you are already at the max level for your ' + spellToUp + ' spell')
    
    
    
# enum = {
    
    
print(enumerate(levelUpOrder))

    


