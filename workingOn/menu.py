# Import the necessary packages
from consolemenu import *
from consolemenu.items import *

# Create the menu

QueueType=None
menu = ConsoleMenu("Welcome to YuumiBot V1.04", "Chose your queue type")
selection_menu = SelectionMenu(["item1", "item2", "item3"])

menu_items = [("BotBeginner",300),("BotIntermediate",400),("NormalDraft",100),("Ranked Solo/Duo",420),("Ranked 5V5",420)]

for items in menu_items:
    menu.append_item(MenuItem(items[0]))

menu.show()





# A FunctionItem runs a Python function when selected
# function_item = FunctionItem("Call a Python function", input, ["Enter an input"])

# # A CommandItem runs a console command
# command_item = CommandItem("Run a console command",  "touch hello.txt")

# # A SelectionMenu constructs a menu from a list of strings
# selection_menu = SelectionMenu(["item1", "item2", "item3"])

# # A SubmenuItem lets you add a menu (the selection_menu above, for example)
# # as a submenu of another menu
# submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu