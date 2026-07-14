yardLength = float(input())
yardWidth = float(input())
houseLength = float(input())
houseWidth = float(input())
housearea = houseWidth * houseLength
yard = yardLength * yardWidth - housearea
wage = yard * 2.0
print(wage)
