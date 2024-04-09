# TODO

from cs50 import get_int

while True:  # there is no do-while loop in python
    height = get_int("Please select height between 1 and 8: ")
    if (height <= 8 and height >= 1):
        break

row = 1

for i in range(0, height, 1):  # (starting point, end, incrementation)
    for j in range(0, height, 1):
        if i+j < height - 1:
            print(" ", end="")
        if i+j >= height - 1:
            print("#", end="")
    if height == height:
        print("  ", end="")
    for k in range(0, row, 1):  # if you use row instead of height as the limit, the loop does not run through unnecessarily more times without printing
        if k <= row:
            print("#", end="")
    print()
    row = row + 1
