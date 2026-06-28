#students grade system
student={}
verify=[]
try:
 student_total=int(input("enter number for student  : "))
except ValueError:
 print("invelid value error ")
except Exception as e:
 print(f"error{e}")
#get input from user
try:
 for i in range(student_total):
  name=input("enter your name : ")
  marks=list(map(int,input("enter your 4 subjects marks with space : ").split()))
  if len(marks)!=4:
   raise ValueError("please enter 4 subjects number")
  student[name]=marks
  print(f"all students :{student}")
except FileNotFoundError:
 print("file not found ")
except ValueError:
 print("invelid value ")
except Exception as e:
 print(f"error{e}")
# store it into a file
try:
 with open("students_grade.txt","w")as file:
  for key,value in student.items():
   file.write(f"{key}:{value}\n")
except ValueError:
 print("invelid value ")
except Exception as e:
 print(f"error{e}")
# calculate marks 
try:
 with open ("students_grade.txt","r")as file:
  def calculate(total):
   if total>=350:
    return "Grade A"
   elif total<350 and total>=280:
    return "Grade B"
   elif total<280 and total>=200:
    return "Grade C"
   else:
    return "Grade G"
  for i in file:
   a, b=i.strip().split(":",1)
   total=list(map(int,b.strip("[]").split(",")))
   combine=sum(total)
   grades=calculate(combine)
   verify.append((a,combine,grades))
except ValueError:
 print("invelid value ")
except Exception as e:
 print(f"error{e}")
#sort and average 
try:
 score=list(sorted(verify,key=lambda x:x[1], reverse=True))
 positions=list(enumerate(score,start=1))
 number=[x[1] for x in verify]
 average=sum(number)/len(verify) 
except ZeroDivisionError:
 average=0
except Exception as e:
 print(f"error{e}")
print(f"students positions {positions} \n class average:{average:.2f}")
