import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")






















def is_valid(s):

    start_valid = letter_start(s)
    length_valid = length(s)
    num = numbers(s)
    signs_valid = extra_signs(s)

    if start_valid + length_valid + num + signs_valid != 0:
        return False
    else:
        return True


#---subfunctions of is_valid()

def letter_start(s):    #check if start with two letters
    if re.match(r"^[A-Z]{2}",s):
        return 0
    else:
        return 1


def length(s):  #check if legth is 2-6
    if len(s) >= 2 and len(s) <=6:
        return 0
    else:
        return 1


def numbers(s):     #numbers allowed only sequentially without interruption at end & sequence does not start with 0
    if re.match(r"^[A-Z]+\d+$", s):
        if re.match(r"^[A-Z]+0", s):
            return 1
        else:
            return 0
    elif re.match(r"^[A-Z]*$", s):
        return 0
    else:
        return 1


def extra_signs(s):     #exclude forbidden signs
    forbidden_signs = [" ",".","?","!"]
    for sign in s:
        if sign in forbidden_signs:
            return 1

    return 0

main()
