a = int(input())

overtake_round = 0
current_round = 0

while a != -1:
    b = int(input())
    current_round += 1

    if b > a and overtake_round == 0:
        overtake_round = current_round

    a = int(input())

print(overtake_round)
