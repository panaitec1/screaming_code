import tkinter as tk
from tkinter import filedialog, Text
import os
from unicodedata import numeric
#os help me create the gui and allows to run the apps, filedialog is gonna help us pick the apps

#determine the number of numerical digits in a string

def digits_number():
    my_string = input()
    print("The string in which we have to identify the digits is:", my_string)
    numerical_digit = 0
    for i in my_string:
        if i.isdigit():
            numerical_digit+=1

    print("There are",numerical_digit,"in",my_string)


digits_number()