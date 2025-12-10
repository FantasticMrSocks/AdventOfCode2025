#!/usr/bin/python3

banks = []
with open("input.txt") as file:
    banks = file.read().split()

joltage = 0

for bank in banks:
    digits = ["0","0","0","0","0","0","0","0","0","0","0","0"]
    index = 0
    for j in range(0,12):
        for i in range(index,len(bank)-(11-j)):
           # print(f"range is {index} to {len(bank)-(11-j)}")
           # print(f"index = {i}")
           # print(f"bank[i] = {bank[i]}")
           # print(f"digit = {digits[j]}")
           # print(f"is bank[i] bigger than digit? {int(bank[i]) > int(digits[j])}")
           # input()
            if int(bank[i]) > int(digits[j]):
                digits[j] = bank[i]
                index = i+1
   # print(f"adding {int(''.join(digits))} to joltage")
    joltage += int(''.join(digits))
   # print(f"joltage is now {joltage}")
   # input()

print(joltage)
