"""
Ch 6 Menu and functions: Passing x and y with return to the math functions
"""

def main ():
    choice      = "start, no choice yet"
    operation   = "start, no operation yet"
    answer      = "start, no answer yet"

    Menu = """
    a   add
    s   subtract
    m   multiply
    d   divide
    e   enter new values
    q   quit
    """

    print ("\n")
    print ("My Python Calculator")
    print ()

    x = int (input ("Enter a non-zero x value: "))
    y = int (input ("Enter a non-zero y value: "))

    while True:
        print (Menu)
        choice = input ("What is your choice: ")

        if choice == "a":
            operation = "Addition"
            answer = addit (x, y)

        elif choice == "s":
            operation = "Subtraction"
            answer = subtractit (x, y)

        elif choice == "m":
            answer = multiplyit (x, y)
            operation = "Multiplication"

        elif choice == "d":

            if y == 0:
                operation = "Divide by 0"
                answer = "Error, can't divide by 0."

            else:
                operation = "Dividing"
                answer = divideit (x,y)

        elif choice == "e":
            operation = "Entering new values"
            answer = enterNew ()
            x = answer [0]
            y = answer [1]

        elif choice == "q":
            operation = "Quitting."
            answer = "Game over."
            break

        else:
            operation = "an invalid choice"
            answer = "request to pick a menu choice."

        print ("Operation is", operation, "of", x, "and", y, "giving", answer)

    print ()
    print ("Goodbye.", operation, answer)

def addit (x, y):
    temp = x + y
    return temp

def subtractit (x, y):
    temp = x - y
    return temp

def multiplyit (x, y):
    return x * y

def divideit (x, y):
    return x / y

def enterNew():
    x = int (input ("Enter an x value : "))
    y = int (input ("Enter a y value  : "))
    return x, y

main ()
    
