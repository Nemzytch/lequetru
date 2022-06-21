import keyboard



accountList = [["Linikath","!DonOtEaTtheYe11OwSnow"],
["Anerorken","!DonOtEaTtheYe11OwSnow"],
["Davesnar","!DonOtEaTtheYe11OwSnow"],
["Ilsiyalda","!DonOtEaTtheYe11OwSnow"],
["Gendympl","!DonOtEaTtheYe11OwSnow"],
["Macinone","!DonOtEaTtheYe11OwSnow"],
["Julisbober","!DonOtEaTtheYe11OwSnow"],
["Iandiandeb","!DonOtEaTtheYe11OwSnow"],
["Phiepalet","!DonOtEaTtheYe11OwSnow"],
["Ettennai","!DonOtEaTtheYe11OwSnow"],
["Unielkinay","!DonOtEaTtheYe11OwSnow"],
["Zarisseefe","!DonOtEaTtheYe11OwSnow"],
["Josendinic","!DonOtEaTtheYe11OwSnow"],
["Monayleve","!DonOtEaTtheYe11OwSnow"],
["Entacyro","!DonOtEaTtheYe11OwSnow"],
["Wydeberte","!DonOtEaTtheYe11OwSnow"],
["Gitlarsam","!DonOtEaTtheYe11OwSnow"],
["Faudrissa","!DonOtEaTtheYe11OwSnow"],
["Quidiail","!DonOtEaTtheYe11OwSnow"],
["Zianeyokat","!DonOtEaTtheYe11OwSnow"],
["Ucialeynne","!DonOtEaTtheYe11OwSnow"],
["Zeatiama","!DonOtEaTtheYe11OwSnow"],
["Gaevaria","!DonOtEaTtheYe11OwSnow"],
["Varahaeli","!DonOtEaTtheYe11OwSnow"],
["Rrhonateve","!DonOtEaTtheYe11OwSnow"],
["Belikail","!DonOtEaTtheYe11OwSnow"],
["Ulkittyl","!DonOtEaTtheYe11OwSnow"],
["Biannyea","!DonOtEaTtheYe11OwSnow"],
["Ssillait","!DonOtEaTtheYe11OwSnow"],
["Rastusae","!DonOtEaTtheYe11OwSnow"],
["Faylovie","!DonOtEaTtheYe11OwSnow"],
["Drarsong","!DonOtEaTtheYe11OwSnow"],
["Yenikoanes","!DonOtEaTtheYe11OwSnow"],
["Kachalhn","!DonOtEaTtheYe11OwSnow"],
["Winowello","!DonOtEaTtheYe11OwSnow"],
["Xoniciane","!DonOtEaTtheYe11OwSnow"],
["Phorinhita","!DonOtEaTtheYe11OwSnow"],
["Phroelbilm","!DonOtEaTtheYe11OwSnow"],
["Quarrellei"," !DonOtEaTtheYe11OwSnow"],
["Girocecis","!DonOtEaTtheYe11OwSnow"],
["Zoachesiq","!DonOtEaTtheYe11OwSnow"],
["Itaronora","!DonOtEaTtheYe11OwSnow"],
["Senaldendi","!DonOtEaTtheYe11OwSnow"],
["Pedymelhel","!DonOtEaTtheYe11OwSnow"],
["Nasminedw","!DonOtEaTtheYe11OwSnow"],
["Natordesbe","!DonOtEaTtheYe11OwSnow"],
["Hanicell2","!DonOtEaTtheYe11OwSnow"],
["Indanans","!DonOtEaTtheYe11OwSnow"],
["Rissintain","!DonOtEaTtheYe11OwSnow"]]




newPassword = "m2BKhs5k"
for accounts in accountList:
    actualPassword = accounts[1]
    accountName = accounts[0]



def connectToAccount(accountName, actualPassword):
    keyboard.write(accountName)
    keyboard.press_and_release("tab")
    keyboard.write(actualPassword)
    keyboard.press_and_release("enter")