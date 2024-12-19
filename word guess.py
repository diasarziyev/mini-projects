import random
word_list=["camel", "baboon", "aardvark"]
word=random.choice(word_list)
print(word)
underscore=""
for position in range(len(word)):
    underscore+="_"
print(underscore)
game_over=False
correct=[]
lives=6
while not game_over:
    guess=input("Guess a letter: ")
    ans=""
    for letter in word:
        if letter==guess:
            ans+=letter
            correct.append(letter)
        elif letter in correct:
            ans+=letter
        else:
            ans+="_"
    if letter in ans:
        print("You have already printed this letter")
    if guess not in word:
        lives-=1
        print("you have ", lives, " lives left")
        if lives==0:
            game_over=True
            print("You lose")
    print(ans)
    if "_" not in ans:
        game_over=True
        print("you win")