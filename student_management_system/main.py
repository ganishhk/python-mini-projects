import user_input 
import student_data

def manage_data(op):
    d = op
    if d == "add":
        data_of_students = user_input.user_data()
        a,b,c = data_of_students
        return student_data.add_student(a,b,c)
    elif d == "view":
        return student_data.view_student()
    elif d == "search":
        a = input("enter student name so we can search student data : ")
        return student_data.view_student(a)
    elif d == "update":
        data = input("what you want to update name,age or course : ").lower()
        return student_data.update_student(data)
    elif d == "delete":
        a = input("enter student name so we can delete student data : ")
        return student_data.delete_student(a)

def loop():
    while True:
        operation = user_input.user_operation()
        if operation == "exit":
            break
        else:
         print(manage_data(operation))
loop()

