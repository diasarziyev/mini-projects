import random
x=random.randint(1,100)
def hard():
    global number
    i=5
    while i!=0:
        number=int(input("pick a number: "))
        if number==x:
            print("You are right!")
            quit()
        elif number>x:
            i=i-1
            print("too high")
            print(f"You have {i} attempts remaining")
        elif number<x:
            i=i-1
            print("too low")
            print(f"You have {i} attempts remaining")
        if i==0:
            print(f"You lose, the number was {x}")
def easy():
    i=10
    while i!=0:
        number=int(input("pick a number: "))
        if number==x:
            print("You are right!")
            quit()
        elif number>x:
            i=i-1
            print("too high")
            print(f"You have {i} attempts remaining")
        elif number<x:
            i=i-1
            print("too low")
            print(f"You have {i} attempts remaining")
        if i==0:
            print(f"You lose, the number was {x}")
difficulty=input("Choose difficulty: ").lower()
if difficulty=="hard":
    hard()
elif difficulty=="easy":
    easy()
else:
    print("Error, try again")
    quit()