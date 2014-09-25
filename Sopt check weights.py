weight = int(input("Please enter a weight in grams: "))
no_of_100g = weight//100
weight = weight%100
no_of_50g = weight//50
weight = weight%50
no_of_10g = weight//10
weight = weight%10
no_of_5g = weight//5
weight = weight%5
no_of_2g = weight//2
weight = weight%2
no_of_1g = weight//1
print("The amount of weights you need are:")
print("{0} 100g weights".format(no_of_100g))
print("{0} 50g weights".format(no_of_50g))
print("{0} 10g weights".format(no_of_10g))
print("{0} 5g weights".format(no_of_5g))
print("{0} 2g weights".format(no_of_2g))
print("{0} 1g weights".format(no_of_1g))
