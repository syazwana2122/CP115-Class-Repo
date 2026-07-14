hours = float(input())
if hours <= 2:
    charges = 0
else:
    if hours <= 5:
        charges = hours - 2 * 2
    else:
        charges = 3 * 2 + hours - 5
parkingFee = charges * hours
print(parkingFee)
