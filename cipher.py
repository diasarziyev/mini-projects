alphabet=['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
x=0
def encrypt(original_text, shift_amount):
    t=""
    for letter in original_text:
        if letter not in alphabet:
            t+=letter
        else:
            x=alphabet.index(letter)+shift_amount
            x=x%len(alphabet)
            t+=alphabet[x]
    print(t)
def decrypt(original_text, shift_amount):
    t=""
    for letter in original_text:
        if letter not in alphabet:
            t+=letter
        else:
            x=alphabet.index(letter)-shift_amount
            x=x%len(alphabet)
            t+=alphabet[x]
    print(t)

def cipher():
    if direction=="encode":
        encrypt(text, shift)
    elif direction=="decode":
        decrypt(text, shift)
    else:
        print("sorry, what?")
        quit()
should_continue=True
while should_continue:
    direction=input("Type 'encode' to encrypt, and 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    cipher()
    res=input("Type 'yes', if you want to go again. If not, type 'no'.\n").lower()
    if res=="no":
        should_continue=False
        print("Thank you.")
