import os
import sys
import tableActions

def restart():
    if tableActions.check_crash(tableActions.check_time())== True:
        tableActions.just_restarted()
        print("Restarting PC")
        os.system("shutdown -r -t 0")
        sys.exit()
    else:
        print("PC is not crashed")
        
restart()