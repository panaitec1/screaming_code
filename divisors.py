import random
import string
import tkinter
#import tkinter as tk
from tkinter import *
from tkcalendar import *
import math
from random import randint

#Write a program that asks the user to enter a number and prints the sum of the divisors of
#that number. The sum of the divisors of a number is an important function in number theory.

def the_divisors():
    print("Enter your number: ")
    my_num = int(input())
    sum_of_div = 0
    for i in range(2, my_num+1):
        divisor = my_num % i
        if divisor == 0:
            sum_of_div = sum_of_div + i

    print("The sum of the divisors is", sum_of_div)

the_divisors()


