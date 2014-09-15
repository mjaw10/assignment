#This program will calculate the volume of a rectangutar swimming pool

print("This program will calculate the volume of water you need to fill your swimming pool")
length = float(input("Please enter the length of your pool: "))
width = float(input("Please enter the width of your pool: "))
deep_depth = float(input("Please enter the depth at the deep end of your pool: "))
shallow_depth = float(input("Please enter the depth at the shallow end of your pool: "))
volume1 = width * length * shallow_depth
depth = deep_depth - shallow_depth
volume2 = (depth * width * length) / 2
total_volume = volume1 + volume2
print("The volume of water needed to fill the pool is {0}m³".format(total_volume))
