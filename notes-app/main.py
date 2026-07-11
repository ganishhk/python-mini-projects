def data_entry ():
    while True:
        data = input("enter your notes here and if you want to delte or read just write : ").lower()
        return data

def add_note(char):
    with open("notes_app.txt","a") as file:
        file.write(char +"\n")
    return "notes save"

def show_notes():
    with open("notes_app.txt","r") as file:
        file_data = file.read()
        return file_data
    
import os

def delete_notes():
    if os.path.exists("notes_app.txt"):
        os.remove("notes_app.txt")
        return "delete complete "
    else:
        return "file not found"
    
def search_notes(char):
    if char == "read":
        return show_notes() 
    elif char == "delete":
        return delete_notes() 
    else:
        return add_note(char) 
    

while True:
    saved_data = data_entry()

    if saved_data == "stop":
            break
    
    result = search_notes(saved_data)
    print(result)
