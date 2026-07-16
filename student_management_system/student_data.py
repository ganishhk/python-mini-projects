import csv
import os
file_name = "student.csv"
def add_student(a,b,c):
    with open (file_name , "a" , newline="") as file:
        writer = csv.writer(file)
        if os.path.getsize(file_name) == 0:
            writer.writerow(["name","age","course"])
        writer.writerow([a,b,c])
            
    return "student added"

def view_student():
    with open (file_name, "r") as file :
        reader = csv.reader(file)
        next(reader)
        allstudents = []
        for row in reader:
            allstudents.append(row)
        return allstudents
    
def search_Student(a):
    with open(file_name , "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == a:
                return row[0]
            
def update_student(a):
    name = input("enter name so we can find your data : ")
    with open(file_name , "r") as file:
        reader = csv.reader(file)
        next(reader)
        new_data = []
        for row in reader:
            if a == "name":
                if row[0] == name:
                    update = input("enter your updated name : ")
                    row[0] = update
                    new_data.append(row)
            elif a == "age":
                if row[0] == name:
                    update = input("enter your updated age : ")
                    row[1] = update
                    new_data.append(row)
            elif a == "course":
                if row[0] == name:
                    update = input("enter your updated course : ")
                    row[2] = update
                    new_data.append(row)

        with open (file_name , "w" , newline="") as file:
         writer = csv.writer(file)
         writer.writerow(["name","age","course"])
         writer.writerow(new_data)

    return "update succesful"

def delete_student(a):
    with open(file_name , "r") as file:
        reader = csv.reader(file)
        next(reader)
        new_data = []
        for row in reader:
            if row[0] != a:
                new_data.append(row)

    with open (file_name , "w" , newline="") as file:
         writer = csv.writer(file)
         writer.writerow(["name","age","course"])
         writer.writerow(new_data)
    return "student data is removed"


    
                        
