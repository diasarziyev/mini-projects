from data import people
import random
x=0
random_person2=random.choice(people)
should_continue=True
while should_continue==True:
    random_person1=random_person2
    random_person2=random.choice(people)
    if random_person1==random_person2:
        random_person2=random.choice(people)
    A=random_person1["follower_count"]
    B=random_person2["follower_count"]
    a=random_person1["name"]
    b=random_person2["name"]
    print(a) 
    print(b)
    choice=input("Who has more followers: A or B?: ").lower()
    if (choice=="a" and A>B) or (choice=="b" and A<B):
        print("Let's gooo")
        x+=1
        print(x)
    else:
        print(f"You lost bruv ;( Yo score: {x}")
        should_continue=False
