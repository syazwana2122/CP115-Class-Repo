Minutes = int(input("Enter the number of minutes: "))

Hours = Minutes // 60
Remaining_Minutes = Minutes % 60

print("Hours:", Hours)
print("Remaining Minutes:", Remaining_Minutes)
print("Converted Time:", Hours, "hours and", Remaining_Minutes, "minutes")