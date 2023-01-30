print ()
print ("Area, Volume, and Weight of a Rectangular Prism")
print ()

w = int ( input ("Enter the width :   "))
l = int ( input ("Enter the length:   "))
h = int ( input ("Enter the height:   "))
print ()

a = l * w
v = l * w * h

print ("The area is", a)
print ("The volume is", v)
print ()

unitweight = float ( input ("Enter the weight of each unit:   "))
print ()

layerweight = unitweight * a
totalweight = unitweight * v

print ("One layer is", layerweight)
print ("The whole cube is", totalweight)
print ()


