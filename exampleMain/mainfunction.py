def main ():
    print ()
    print ("An example of the main() function")
    print ()

    number = float (input ("Enter a number: "))
    print ()

    result = square (number)
    print ("The square of", number, "is", result)

    result = add10 (number)
    print (number, "plus 10 is", '%10.1f' % result)

    result = mult10 (number)
    print (number, "times 10 is", '%9.1f' % result)

    result = div10 (number)
    print (number, "divided by 10 is", result)

def square (x):
    return x * x

def add10 (y):
    return y + 10

def mult10 (z):
    answer = z * 10
    return answer

def div10 (d):
    answer = d/10
    return answer

main ()
