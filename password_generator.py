import random
import string

def my_password():
    length = int(input("Enter the length of the password:"))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    #combine and store data
    all = lower + upper + num + symbols

    #generating the password
    temp = random.sample(all,length)
    password = " ".join(temp)
    print(password)

my_password()