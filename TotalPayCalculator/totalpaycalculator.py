print ()
print ("-Employee Weekly Pay-")
print ()

wage = float(input("Please input the hourly wage of the employee : "))
print ()

reg = int(input (  "Please input number of regular hours worked  : "))
print ()

ovr = int(input (  "Please input number of overtime hours worked : "))
print ()

weekly = (reg * wage) + ((ovr * wage) * 1.5)

print ("The total weekly pay of this employee is:","$"+str(weekly))
