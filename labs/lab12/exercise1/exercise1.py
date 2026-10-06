correct_password = "python123"

attempts_used = 0
login_successful = False
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    password = input()
    attempts_used += 1

    if password == correct_password:
        login_successful = "True"
        break  # Exit immediately

print(login_successful)
print(attempts_used)
