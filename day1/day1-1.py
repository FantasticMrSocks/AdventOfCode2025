#!/usr/bin/python3

sequence = []
with open("sequence.txt") as file:
    sequence = file.read().split()

#print(sequence)

dial = 50
count = 0

for i in sequence:
    if i[0] == 'R':
        dial = (dial + int(i[1:])) % 100
    else:
        dial = (dial - int(i[1:])) % 100
    if dial == 0:
        count += 1

print(count)
