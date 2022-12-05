import random
import string
import tkinter
#import tkinter as tk
from tkinter import *
from tkcalendar import *
import os
#os help me create the gui and allows to run the apps, filedialog is gonna help us pick the apps


root = Tk()
root.title("My calendar")
root.geometry("600x400")

my_cal = Calendar(root, selectMode = "day", year = 2022, month = 12, day = 5)
my_cal.pack(pady=20)

def grab_date():
    my_label.config(text="Today's date is " + my_cal.get_date())

#creating a button
my_button = Button(root, text = "Get date", command = grab_date)
my_button.pack(pady = 20)

#creating a label
my_label = Label(root, text=" ")
my_label.pack(pady=20)

root.mainloop()

