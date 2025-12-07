#!/usr/bin/python3

sequence = []
with open("sequence.txt") as file:
    sequence = file.read().split()

#print(sequence)

dial = 50
count = 0

for i in sequence:
    print(f"starting dial is {dial}")
    print(f"i = {i}")

    change = int(i[1:])
    if i[0] == 'L':
        change = 0 - change
    print(f"change = {change}")

    dial += change
    print(f"dial + change = {dial}")

    print(f"count = {count}")

    if dial <= 0 and dial != change:
       count += 1
    count += abs(int(dial/100))

    print(f"adding {abs(int(dial/100))} to count")
    print(f"now count = {count}")

    dial %= 100

    print(f"using dial %= 100 to set dial to {dial}")

    #input()

print(count)
