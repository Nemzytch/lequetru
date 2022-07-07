import os
import sys

#restart the pc
def restart():
    os.system("shutdown -r -t 0")
    sys.exit()

restart()