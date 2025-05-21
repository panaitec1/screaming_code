import random

"3. Dice Rolling Simulator"
"Simulate rolling a dice multiple times."
"Record and count the frequency of each outcome."
"Display results in a readable format."

def rolling_dice():
    dice_faces = [1,2,3,4,5,6]
    while(True):
        number_of_rolls = int(input("How many times do you want to roll the dice?"))
        result = []
        for roll in range(0,number_of_rolls):
            result.append((random.choice(dice_faces)))
        print(result)

        for elements in dice_faces:
            frequency = result.count(elements)
            print(f"The frequency of {elements} element is {frequency}.")

        to_stop = input("Roll again? y/n").lower()
        if to_stop == "n":
            break


rolling_dice()
