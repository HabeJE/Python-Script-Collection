def main ():
    print ()
    print (" " * 20, "Another App with Functions and a Main, Paycheck 22")

    while True:
        print ()
        name        =        input ("Enter the name or q to quit : ")

        if name == "q":
            break

        hoursWorked = float (input ("Enter hours worked          : "))
        rateOfPay   = float (input ("Enter rate of pay           : "))
        taxRate     = float (input ("Enter the tax rate          : "))
        print ()

        GP = grossPay (hoursWorked, rateOfPay)
        print ("Gross Pay is", GP)

        TA = taxAmount (GP, taxRate)
        print ("Tax Amount is", TA)

        print ()
        earnings = netPay (GP, TA)

        print (name, "Earned", earnings)
        print ()

    print ()
    print ("All done.")
    print ()

def grossPay (hoursWorked, rateOfPay):
    gPay = hoursWorked * rateOfPay
    return gPay

def taxAmount (grossPay, taxRate):
    tAmount = grossPay * taxRate
    return tAmount

def netPay (grossPay, taxAmount):
    nPay = grossPay - taxAmount
    return nPay

main ()
