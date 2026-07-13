import string
import random

letter = string.ascii_letters
num = string.digits
special = string.punctuation

data = [letter,num,special]

def genrate_password(length):
    password = []
    try :
        for i in range(0,length+1):
            ran = random.choice(data)
            i = random.choice(ran)
            password.append(i)
    except:
        return "there is something wrong"
    return "".join(password)

        
