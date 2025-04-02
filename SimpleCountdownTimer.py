#SimpleCountdonwTimer
#Create a countdown timer that takes user input for the time and counts down to zero, printing a message when the time is up.
import time

def my_timer(minutes):
    time_left = minutes * 60
    while time_left>0:
        minutes_left = time_left//60
        seconds_left = time_left%60
        print(f"Time remaining: {minutes_left} minutes {seconds_left} seconds")
        time.sleep(1) #wait for 1 seconds
        time_left-=1
    print("Time's up! You're ready to go!")
    
        
user_input = int(input("Please introduce the time you need for your task in minutes: "))
my_timer(user_input)