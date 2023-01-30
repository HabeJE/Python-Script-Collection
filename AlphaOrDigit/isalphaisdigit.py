#alpha digit

line = "did not quit yet"
sumTotal   = 0
sumDigits  = 0
sumAlphas  = 0
sumNeither = 0

alphaLines   = ""
digitLines   = ""
neitherLines = ""

while line != "":
    print ()
    line = input ("Enter a line or just <Enter> to quit: ")

    if line == "":
        break

    sumTotal += 1
    print (" " * 38, end = "is ")

    if line.isdigit():
        sumDigits += 1
        print ("Digits #", sumDigits)
        alphaLines = alphaLines + line + "\n"

    elif line.isalpha ():
        sumAlphas += 1
        print ("Alpha #", sumAlphas)
        digitLines = digitLines + line + "\n"

    else:
        sumNeither += 1
        print ("Neither #", sumNeither)
        neitherLines = neitherLines + line + "\n"

print ()
print ("Here are the alpha, digit and neither lines you entered...")
print ()
print (alphaLines)
print (digitLines)
print (neitherLines)

print ("Totals:", sumDigits, "Digits, ", sumAlphas, "Alphas, ",\
       sumNeither, "Neithers. ", \
       "That's", sumTotal, "lines in all")

print ()
print ("All done.")
