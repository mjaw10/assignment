#input width
#input lengtgh
# -2m from tength + width
# code to work out how much it will cost to turf a garden wih a 1m boarder around the perimiter

width = float(input("Enter the width of your garden: ")) - 2
length = float(input("Enter the length of your garden: ")) - 2
area = width * length
cost = 10 * area
print("The area of garden you need to turf is {0}m²".format(area))
print("The cost of turfing the garden will be £{0:.2f}".format(round(cost,2)))
