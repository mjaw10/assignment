binary_no = input("Enter a 4 bit binary number: ")
bit4 = int(binary_no[0])
bit3 = int(binary_no[1])
bit2 = int(binary_no[2])
bit1 = int(binary_no[3])
ph8 = bit4 * 8
ph4 = bit3 * 4
ph2 = bit2 * 2
ph1 = bit1 * 1
decimal_no = ph8 + ph4 + ph2 + ph1
if decimal_no == 0:
    print("Your number in hexidecimal is 0")
elif decimal_no == 1:
    print("Your number in hexidecimal is 1")
elif decimal_no == 2:
    print("Your number in hexidecimal is 2")
elif decimal_no == 3:
    print("Your number in hexidecimal is 3")
elif decimal_no == 4:
    print("Your number in hexidecimal is 4")
elif decimal_no == 5:
    print("Your number in hexidecimal is 5")
elif decimal_no == 6:
    print("Your number in hexidecimal is 6")
elif decimal_no == 7:
    print("Your number in hexidecimal is 7")
elif decimal_no == 8:
    print("Your number in hexidecimal is 8")
elif decimal_no == 9:
    print("Your number in hexidecimal is 9")
elif decimal_no == 10:
    print("Your number in hexidecimal is A")
elif decimal_no == 11:
    print("Your number in hexidecimal is B")
elif decimal_no == 12:
    print("Your number in hexidecimal is C")
elif decimal_no == 13:
    print("Your number in hexidecimal is D")
elif decimal_no == 14:
    print("Your number in hexidecimal is E")
else:
    print("Your number in hexidecimal is F")



