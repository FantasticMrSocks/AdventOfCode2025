#!/usr/bin/python3

import textwrap

def find_repeats(number, div):
    if div == 0:
        print(f"number is {number} and div is 0")
    arr = textwrap.wrap(number, div)
    found = False
    if len(number) % div == 0:
        found = (len(set(arr)) == 1)
       # print(arr)
        #input()
    if found:
        print(arr)
       # input()
        return True
    elif div > 1:
        return find_repeats(number, div-1)
    else:
        return False

pairs = []
with open("input.txt") as file:
    pairs = file.read().split(",")

ids = []

for i in pairs:
    first,last = i.split("-")
    for j in range(int(first),int(last)+1):
        j = str(j)
        if len(j) > 1 and find_repeats(j, len(j)-1):
            ids.append(int(j))

ids_sum = 0

for i in ids:
    ids_sum += i

print(ids_sum)
