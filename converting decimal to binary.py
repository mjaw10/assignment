DenaryValue = int(input("Enter a deary number: "))
BinaryString = ""
while DenaryValue > 0:
    BinaryString = str(DenaryValue % 2) + BinaryString
    DenaryValue = DenaryValue // 2
print("The binary equivilant is {0}".format(BinaryString))
