#To-Do List
import random
def todo_list():
    print("When you don't want to add any task press 'n'\n")
    my_list=[]
    print("Hi! Ready to tackle the day? What do we have to do today?")
    while True:
        answer = input("Input task.\n")
        if answer != "n":
            #Task = input("Input task.\n")
            my_list.append(answer)
        else:
            break
    print("Today we have to do the following:")
    index = 0
    for i in my_list:
        print(index,i)
        index+=1
        
    print("----------------------------------------------")
    task_done=input("Have you finish any of your tasks?")
    task_number=int(input("Which one?"))
    if task_done == "yes":
        print(f"Great! Let's remove task {task_number} from your list.")
        my_list.pop(task_number)
        print("Don't forget, you still have tasks left.")
        index_2=0
        for i in my_list:
            print(index_2,i)
            index_2+=1
    
todo_list()