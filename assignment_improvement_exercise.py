#john bain
#variable improvement exercise
#05-09-12

import math

r = float(input("please enter the radius of the circle: "))

c = 2 * math.pi * r
c = round(c,2)

a = math.pi * r**2
a = round(a,2)

print("The circumference of this circle is {0}.".format(c))
print("The area of this circle is {0}.".format(a))
