import random

print("What is your name?")
name = input()

rand_num = random.randint(1,8)

def answer(rand_num, name):
    if rand_num == 1:
        return( "You Suck!!")
    elif rand_num == 2:
        return( "You can't program!!")
    elif rand_num == 3:
        return( "You dont know what you are doing Do you?")
    elif rand_num == 4:
        return( "Really", (name), "really")
    elif rand_num == 5:
        return( "WOW, just WOW?")
    elif rand_num == 6:
        return( "You should just stop while your ahead?")
    elif rand_num == 7:
        return( "HAHAHA")
    elif rand_num == 8:
        return( "I have nothing to say to you")
    else:
        return( "Just nothing!!!")
    
fortune = answer(rand_num, name)
print(fortune)