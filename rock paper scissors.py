import random
var=["rock", "paper", "scissors"]
x1=input().lower()
x2=random.choice(var)
print(x2)
if (x1=="rock" and x2=="paper") or (x1=="paper" and x2=="scissors") or (x1=="scissors" and x2=="rock"):
    print("You Lose")
elif (x1=="rock" and x2=="scissors") or (x1=="paper" and x2=="rock") or (x1=="scissors" and x2=="paper"):
    print("You Win")
if x1==x2:
    print("Draw")
