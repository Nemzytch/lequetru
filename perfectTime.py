#print the univeral time in the format of hh:mm:ss

import time
from datetime import datetime

#print time in new york time

Now = datetime.utcnow()

print(Now.strftime("%H:%M:%S"))