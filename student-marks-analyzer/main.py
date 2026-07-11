def students():
    subjects = 3
    sub = 1
    students_marks = []
    while subjects > 0:
        data  = int(input(f"Your {sub} subject marks : "))
        students_marks.append(data)
        subjects -= 1
        sub +=1
        if sub == 4 :
            sub = 1

    return students_marks 

def student_all_marks(marks):
    return f"{marks}"

def higest_marks (marks):
    return max(marks)

def lowest_marks (marks):
    return min(marks)

def total_marks (marks):
    return sum(marks)

def average_marks(marks):
    return sum(marks) / len(marks)

def student_result(marks):
    for i in marks:
        if i < 33:
            return  "student has less marks then 33 so fail"
        
    return "congrats you pass your exam"

def show_report(marks):
    return (f"""
            all subjects : {student_all_marks(marks)}
            higest : {higest_marks(marks)}
            lowest : {lowest_marks(marks)}
            total : {total_marks(marks)}
            average : {average_marks(marks)}
            result : {student_result(marks)}
            """)

student_marks = students()

print(show_report(student_marks))