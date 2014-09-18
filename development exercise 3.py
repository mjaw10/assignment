#Matthew Wadkin
#18/09/14
#This program will convert your height from inches to centermeters and your weight from stone to kg

height_inch = float(input("Please enter you height in inches: "))
weight_stone = float(input("Please enter your weight in stone: "))
height_cm = height_inch * 2.54
weight_kg = weight_stone * 6.364
print("Your height in cm is {0} and your weight in kg is {1}".format(height_cm,weight_kg))
