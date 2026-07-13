from input import user_data
from genrator import genrate_password

def genrator(length):
    return genrate_password(length)


data = user_data()
print(genrator(data))