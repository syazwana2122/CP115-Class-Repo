grade = float(input())

total_sum = 0
valid_count = 0

while grade != -1:
    if grade < 0 or grade > 100:
        grade = float(input())
        continue

    total_sum += grade
    valid_count += 1
    grade = float(input())

average = total_sum / valid_count


print(valid_count)
print(f"{average:.2f}")
