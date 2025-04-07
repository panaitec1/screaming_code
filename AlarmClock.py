#AlarmClock
#Build a simple alarm clock that lets the user set a time and then plays a sound or prints a message when the time arrives.
import time
from datetime import datetime
import winsound

def alarm_clock():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    alarm_time=input("At what hour would you like to set the alarm? Hours:minutes")
    
    while(True):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if current_time == alarm_time:
            winsound.Beep(1000,1000)
            print("yes")
            break
        time.sleep(60)


alarm_clock() 

