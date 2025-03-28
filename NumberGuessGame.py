#Number Guessing game
import random
def guess():
    my_list=[]
    #do the list
    for i in range(101):
       my_list.append(i)
    #generate random number
    random_nr=random.choice(my_list)
    print(f"The random number is {random_nr}.")
    #prompt the user to guess the number
    
    print("You have 3 attempts to guess the number!")
    for i in range(3):
        nr_pick=int(input("Guess the number: "))
        if i<3:
            if nr_pick>100:
                print("The number you gave is exceeding the limit.")
            elif nr_pick>random_nr:
                print("The number you gave is too high.")
            elif nr_pick<random_nr:
                print("The number you gave is too low.")
            i+=1
            if nr_pick==random_nr:
                print("Congrats! You guessed the number!")
            else:
                print("Sorry! You didn't guess the number.")
        
    
guess()