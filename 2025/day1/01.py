# circle dial 
# left from 0 -> ... -> 99 -> 0
# right from 99 -> 0 -> ..... -> 99

import pathlib

data = pathlib.Path("2025/day1/01.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")
instruction = [(i[0], int(i[1:])) for i in lines]

current1 = 50
current2 = 50
count1 = 0
count2 = 0


for direction, amount in instruction:
    # part 1
    if direction == "R":
        # to higher num
        current1 = (current1 + amount) % 100
    elif direction == "L":
        # to lower num
        current1 %= 100
        current1 = (current1 - amount) % 100

    if current1 == 0:
        count1 += 1


    # part 2
    for i in range(amount):
        if direction == "R":
            # to higher num
            current2 = (current2 + 1) % 100
        elif direction == "L":
            # to lower num
            current2 = (current2 - 1) % 100
        
        if current2 == 0:
            count2 += 1

# Final Password 
# Part 1 : number of times dial left pointing at 0 after any rotation
print("The final password is " + str(count1))
# Part 2 : number of time the dial point at 0 during/after the rotation
print("The final password is " + str(count2))
