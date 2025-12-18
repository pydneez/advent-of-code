# circle dial 
# left from 0 -> ... -> 99 -> 0
# right from 99 -> 0 -> ..... -> 99

import pathlib

data = pathlib.Path("2025/day1/01.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")
instruction = [(i[0], int(i[1:])) for i in lines]

current = 50
count = 0


for direction, amount in instruction:
    if direction == "R":
        # to higher num
        current = (current + amount) % 100
    elif direction == "L":
        # to lower num
        current %= 100
        current = (current - amount) % 100

    # print("The current is " + str(current))
    if current == 0:
        count += 1
        # print("The count is " + str(count))
    
# actual password is the number of times 
# that the dial left pointing at 0
# after any rotation in the sequence.
print("The final count is " + str(count))