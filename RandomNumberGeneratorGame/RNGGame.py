print ()
tries = 0
import random

print ("Guessing my tries")
while True:
    print ()
    highside = int ( input ("From how many tries do you want to guess, 0 to quit: "))
    if highside == 0:
        break
    lowside = 1
    secret = random.randint (1, highside)

    while True:
        print ()
        print ("Guess my secret number between", lowside, "and", highside, end = " ")
        guess = int (input ("Guess: "))
        tries += 1

        if guess > secret:
            print ("Too high.")
            highside = guess

        if guess < secret:
            print ("Too low.")
            lowside = guess

        if guess == secret:
            print ("You got it in,", tries, "guesses.")
            break

print ()
print ("Thanks for guessing. Goodbye.")
print ()
