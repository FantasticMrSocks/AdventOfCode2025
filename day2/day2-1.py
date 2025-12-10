#!/usr/bin/python3

pairs = []
with open("input.txt") as file:
    pairs = file.read().split(",")

ids = []

for i in pairs:
    first,last = i.split("-")
    for j in range(int(first),int(last)+1):
        j = str(j)
        if len(j) % 2 == 0 and j[:int(len(j)/2)] == j[int(len(j)/2):]:
            ids.append(int(j))

ids_sum = 0

for i in ids:
    ids_sum += i

print(ids_sum)
