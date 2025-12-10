#!/usr/bin/python3

banks = []
with open("input.txt") as file:
    banks = file.read().split()

joltage = 0

for bank in banks:
    first = 0
    first_index = 0
    second = 0
    for i in range(len(bank)-1):
        #print(f"index = {i}")
        #print(f"bank[i] = {bank[i]}")
        #print(f"first = {first}")
        #print(f"is bank[i] bigger than first? {int(bank[i]) > int(first)}")
        #input()
        if int(bank[i]) > int(first):
            first = bank[i]
            first_index = i
    for i in range(first_index+1,len(bank)):
        #print(f"index = {i}")
        #print(f"bank[i] = {bank[i]}")
        #print(f"second = {second}")
        #print(f"is bank[i] bigger than second? {int(bank[i]) > int(second)}")
        #input()
        if int(bank[i]) > int(second):
            second = bank[i]
    print(f"adding {int(first+second)} to joltage")
    joltage += int(first + second)
    print(f"joltage is now {joltage}")
    input()

print(joltage)
