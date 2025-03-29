#RockPaperScissors
import random
def RPS():
    print("Welcome to the RockPaperScissors game.\n")
    my_choice = ["Rock", "Paper", "Scissors"]
    my_input_r=0
    my_input_p=0
    my_input_s=0
    computers_choice = set(my_choice)
    #user input
    my_input = input("What's your choice? Rock paper or scissors?\n")
    if my_input == "rock":
        my_input_r = my_choice[0].lower()
        print(f"You chose {my_input_r}.")
    elif my_input == "paper":
        my_input_p = my_choice[1].lower()
        print(f"You chose {my_input_p}.")
    elif my_input == "scissors":
        my_input_s = my_choice[2].lower()
        print(f"You chose {my_input_s}.")
    #PC input
    pc_input = (random.choice(list(computers_choice))).lower()
    print(f"The pc chose {pc_input}.")
    #comparing logic
    while True:
        if pc_input==my_input_r:
            print("It's a draw!")
            break
        elif pc_input == my_input_p:
            print("It's a draw!")
            break
        elif pc_input == my_input_s:
            print("It's a draw!")
            break
        if my_input != pc_input:
            if my_input_r and pc_input == "scissors":
                print("You won!")
                break
            if my_input_r and pc_input == "paper":
                print("You lost!")
                break
            if my_input_p and pc_input == "rock":
                print("You won!")
                break
            if my_input_p and pc_input == "scissors":
                print("You lost!")
                break
            if my_input_s and pc_input == "paper":
                print("You won!")
                break
            if my_input_s and pc_input == "rock":
                print("You lost!")
                break
    
RPS()
