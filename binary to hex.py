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
print(decimal_no)


