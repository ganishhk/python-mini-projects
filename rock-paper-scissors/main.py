# rock paper scissors game
import random
def gg():
 b=["rock" ,"paper", "scissors"] 
 player_score=0
 computer_score=0
 round=5
 for i in range (1,round+1):
    print(f"round{i}")
    a=input("enter what you want to pick rock ,paper or scissors  :").lower()
    c=random.choice(b)
    print("computer choice",c)
    if a not in b:
        print("invalid data")
    elif a==c:
         print( "its a tie")
    elif (a== "rock" and c=="scissors") or\
           (a== "scissors"and c=="paper") or\
           (a== "paper"and c=="rock"):
        print("you won again ")
        player_score+=1
    else:
        print("computer won again ")
        computer_score+=1
 print("final score")
 print(f"your score :{player_score}")
 print(f"computer score :{computer_score}")

 if player_score > computer_score:
    return "you won champ"
 elif computer_score > player_score:
    return "computer is won "
 else:
    return "again tie"
print(gg())
    