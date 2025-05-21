import random

"3.  Word Frequency Counter"
"Ask the user for a sentence or paragraph, then count how often each word appears."
"Store the frequencies in a dictionary."

def word_frequency():
    phrase = input("Enter the phrase: ")
    print(f"The phrase looks like this: {phrase}.")
    words = phrase.split()
    my_list = []
    my_dict = {}
    for word in words:
        print(word)
        my_list.append(word)

    print(my_list)

    for elements in my_list:
        frequency = my_list.count(elements)
        print(f"The frequency of {elements} in our phrase is {frequency}.")
        my_dict[elements] = frequency

    print(my_dict)

word_frequency()

