def add(n1, n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

for pick in operations:
    n1=float(input("What's the first number?: "))
    print(
        "+\n",
        "-\n",
        "*\n",
        "/\n"
    )
    pick=input("Pick an operation: ")
    if pick=="*":
        operations["*"]
    elif pick=="+":
        operations["+"]
    elif pick=="-":
        operations["-"]
    elif pick=="/":
        operations["/"]
    n2=float(input("What's the next number?: "))
    r1=operations[pick](n1,n2)
    print(operations[pick](n1,n2))
    con=input("Type 'y' if you want to continue, and 'n' if you want to try again").lower()
    while con=="y":
        pick=input("Pick an operation: ")
        if pick=="*":
            operations["*"]
        elif pick=="+":
            operations["+"]
        elif pick=="-":
            operations["-"]
        elif pick=="/":
            operations["/"]
        n3=float(input("What's the next number?: "))
        print(operations[pick](r1,n3))
        con=input("Type 'y' if you want to continue, and 'n' if you want to try again").lower()
        if con=="n":
            quit()