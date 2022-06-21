import datetime
import pytz


# print datetime from paris

now = datetime.datetime.now(pytz.timezone('Europe/Paris'))
print(now.strftime("%H:%M %m-%d-%Y"))
