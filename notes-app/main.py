import os

while True:
    data = input("ENTER YOUR NOTE : ")
    data_clean = data.strip().lower()
    file_name = "new_notes.txt"

    if data_clean == "exit" :
        break

    elif data_clean == "read":
         with open(file_name , "r") as file:
            content = file.read()
            print(content)

    elif data_clean == "delete":
        if os.path.exists(file_name):
            os.remove(file_name)
            print("file deleted")
        else:
            print("file not found")

    elif data_clean == "clear":
        with open(file_name , "w") as file:
          pass
          print("File Data Cleared")

    else:
        with open(file_name , "a") as file:
          file.write(data+"\n")
        print("Your note has been saved!")