from datetime import datetime
import time
from random import randint


odds = [x for x in range(1, 60, 2)]

for i in range(5):

    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("This minute seems a little odd")
    else:
        print("Not an odd minute")

    time.sleep(randint(1, 60))