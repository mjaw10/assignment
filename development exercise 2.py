#Matthew Wadkin
#18/09/14
#program to convert fahrenheit to centigrade

f_temp = float(input("Enter the temperature in degrees fahrenheit: "))
c_temp = (f_temp - 32) * (5/9)
print("The temperature in degrees centigrade is {0}".format(c_temp))
