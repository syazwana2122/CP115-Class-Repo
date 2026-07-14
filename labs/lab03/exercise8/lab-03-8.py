principal = float(input())
rate = float(input())
time = float(input())
interest = principal * rate / 100
print(interest)
totalAmount = principal + interest
print(totalAmount)
monthlyInterest = interest / time * 12
print(monthlyInterest)

