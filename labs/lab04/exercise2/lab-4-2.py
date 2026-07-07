income = float(input())
if income >= 50000.0:
    if income >= 100000.0:
        tax = 0.02
    else:
        tax = 0.01
else:
    tax = 0.0
totalTax = tax * income
print(totalTax)
