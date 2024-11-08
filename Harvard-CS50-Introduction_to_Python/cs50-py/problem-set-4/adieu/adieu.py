
#description: say adieu to one or multiple input-names in specific configurations


import sys

def main():
    print(say_adieu())




























def say_adieu():

    names = []

    while True:

        try:
            name = input("Name: ")
            if name.isalpha():
                names.append(name)
        except EOFError: # hit ctrl+d
            break

    if len(names) < 1:
        sys.exit("Invalid number of arguments")


    elif len(names) == 1:
        return (f"Adieu, adieu, to {names[0]}")

    elif len(names) == 2:
        return (f"Adieu, adieu, to {names[0]} and {names[1]}")


    elif len(names) > 2:
        part_list = ", ".join(names[:-1])
        return (f"Adieu, adieu, to {part_list}, and {names[-1]}")


main()
