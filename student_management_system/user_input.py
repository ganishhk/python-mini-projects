def user_operation():
    user_choice = input("What you want to do add,view,sreach,update,delete or exit : ").lower()    
    return user_choice

def user_data():
    student_name = str(input("enter your name : ")).lower()
    student_age = int(input("enter your age :"))
    student_course = str(input("enter your course :")).lower()
    return student_name,student_age,student_course