print("This program will calculate the volume of a pool")
width = float(input("Please enter the width of the pool: "))
length = float(input("Please enter te length of the pool: "))
depth = float(input("Please enter the depth of your pool: "))
main_section_volume = length * width * depth
circle_radius = width/2
circle_area = 3.14 * (circle_radius ** 2)
half_circle_volume = (circle_area / 2) * depth
pool_volume = main_section_volume + half_circle_volume
print("The pool volume is {0}m³".format(pool_volume))
