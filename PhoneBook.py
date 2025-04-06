#Simple Contact Book
#Create a program that allows users to store contacts with names, 
#phone numbers, and emails. You can save the data in a file and allow for adding, viewing, and deleting contacts. 

import pandas as pd

def contact_book():
    
    book_data={}
    book_keys=[]
    book_values=[]
    book_phnr_email=[]

    nr_of_contacts = int(input("Please introduce the number of contacts for your phone book: "))

    while(True):

        contact_name=input("\nPlease introduce name: ")
        contact_phone_number = input("\nPlease introduce phone number for {contact_name}")
        contact_email = input("\nPlease introduce email for {contact_name}")
        contact_info = [contact_phone_number, contact_email]

        book_keys.append(contact_name)
        book_values.append(contact_info)

        for key, value in zip(book_keys, book_values):
            book_data[key] = value
    
        print(book_data)

        df = pd.DataFrame(book_data)
        df.to_excel('output.xlsx', index=False, engine='openpyxl')

        print("Data has been written to 'output.xlsx'")

        finish_input=input("No more adding? (yes/no)")

        if finish_input.lower()=="no":
            break


contact_book()


    


