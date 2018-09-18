from datetime import datetime
from os import getcwd
import sys
import os
import time
##
odds = [ 1, 3, 5, 7, 9 , 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

right_now = datetime.today().minute

print('time right now:: ', right_now)

if right_now in odds:
    print("This minute belongs to first half of odds")
else:
    print("Not an odd minute")

##
where_am_I = getcwd()
print(where_am_I)

##
print(sys.platform , sys.version, os.getcwd(), os.getenv('JAVA_HOME'))
print(datetime.isoformat(datetime.today()))
print(time.strftime("%H:%M-%A,%p"))

