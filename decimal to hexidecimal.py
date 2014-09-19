#Matthew Wadkin
#18/09/14
#This program will change a number from decimal to hexidecimal

DecimalValue = int(input("Enter an interger between 0 and 4095: "))
BinaryString = ""
while DecimalValue > 0:
    BinaryString = str(DecimalValue % 2) + BinaryString
    DecimalValue = DecimalValue // 2
    
no_of_bits = len(BinaryString)

if no_of_bits == 0:
    BinaryString = "000000000000" + BinaryString
elif no_of_bits == 1:
    BinaryString = "00000000000" + BinaryString
elif no_of_bits == 2:
    BinaryString = "0000000000" + BinaryString
elif no_of_bits == 3:
    BinaryString = "000000000" + BinaryString
elif no_of_bits == 4:
    BinaryString = "00000000" + BinaryString
elif no_of_bits == 5:
    BinaryString = "0000000" + BinaryString
elif no_of_bits == 6:
    BinaryString = "000000" + BinaryString
elif no_of_bits == 7:
    BinaryString = "00000" + BinaryString
elif no_of_bits == 8:
    BinaryString = "0000" + BinaryString
elif no_of_bits == 9:
    BinaryString = "000" + BinaryString
elif no_of_bits == 10:
    BinaryString = "00" + BinaryString
elif no_of_bits == 11:
    BinaryString = "0" + BinaryString
else:
    BinaryString = BinaryString

bit12 = int(BinaryString[0])
bit11 = int(BinaryString[1])
bit10 = int(BinaryString[2])
bit9 = int(BinaryString[3])
bit8 = int(BinaryString[4])
bit7 = int(BinaryString[5])
bit6 = int(BinaryString[6])
bit5 = int(BinaryString[7])
bit4 = int(BinaryString[8])
bit3 = int(BinaryString[9])
bit2 = int(BinaryString[10])
bit1 = int(BinaryString[11])

ph8_2 = bit12 * 8
ph4_2 = bit11 * 4
ph2_2 = bit10 * 2
ph1_2 = bit9 * 1

ph8_1 = bit8 * 8
ph4_1 = bit7 * 4
ph2_1 = bit6 * 2
ph1_1 = bit5 * 1

ph8 = bit4 * 8
ph4 = bit3 * 4
ph2 = bit2 * 2
ph1 = bit1 * 1

decimal_no_2 = ph8_2 + ph4_2 + ph2_2 + ph1_2
decimal_no_1 = ph8_1 + ph4_1 + ph2_1 + ph1_1
decimal_no = ph8 + ph4 + ph2 + ph1

if decimal_no_2 == 0:
    hex2 = 0
elif decimal_no_2 == 1:
    hex2 = 1
elif decimal_no_2 == 2:
    hex2 = 2
elif decimal_no_2 == 3:
    hex2 = 3
elif decimal_no_2 == 4:
    hex2 = 4
elif decimal_no_2 == 5:
    hex2 = 5
elif decimal_no_2 == 6:
    hex2 = 6
elif decimal_no_2 == 7:
    hex2 = 7
elif decimal_no_2 == 8:
    hex2 = 8
elif decimal_no_2 == 9:
    hex2 = 9
elif decimal_no_2 == 10:
    hex2 = "A"
elif decimal_no_2 == 11:
    hex2 = "B"
elif decimal_no_2 == 12:
    hex2 = "C"
elif decimal_no_2 == 13:
    hex2 = "D"
elif decimal_no_2 == 14:
    hex2 = "E"
else:
    hex2 = "F"

if decimal_no_1 == 0:
    hex1 = 0
elif decimal_no_1 == 1:
    hex1 = 1
elif decimal_no_1 == 2:
    hex1 = 2
elif decimal_no_1 == 3:
    hex1 = 3
elif decimal_no_1 == 4:
    hex1 = 4
elif decimal_no_1 == 5:
    hex1 = 5
elif decimal_no_1 == 6:
    hex1 = 6
elif decimal_no_1 == 7:
    hex1 = 7
elif decimal_no_1 == 8:
    hex1 = 8
elif decimal_no_1 == 9:
    hex1 = 9
elif decimal_no_1 == 10:
    hex1 = "A"
elif decimal_no_1 == 11:
    hex1 = "B"
elif decimal_no_1 == 12:
    hex1 = "C"
elif decimal_no_1 == 13:
    hex1 = "D"
elif decimal_no_1 == 14:
    hex1 = "E"
else:
    hex1 = "F"

if decimal_no == 0:
    hex0 = 0
elif decimal_no == 1:
    hex0 = 1
elif decimal_no == 2:
    hex0 = 2
elif decimal_no == 3:
    hex0 = 3
elif decimal_no == 4:
    hex0 = 4
elif decimal_no == 5:
    hex0 = 5
elif decimal_no == 6:
    hex0 = 6
elif decimal_no == 7:
    hex0 = 7
elif decimal_no == 8:
    hex0 = 8
elif decimal_no == 9:
    hex0 = 9
elif decimal_no == 10:
    hex0 = "A"
elif decimal_no == 11:
    hex0 = "B"
elif decimal_no == 12:
    hex0 = "C"
elif decimal_no == 13:
    hex0 = "D"
elif decimal_no == 14:
    hex0 = "E"
else:
    hex0 = "F"

print("Your number in hexidecimal is {0}{1}{2}".format(hex2,hex1,hex0))
