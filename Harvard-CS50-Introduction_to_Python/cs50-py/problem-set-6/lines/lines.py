
# description: count lines of code in a python file, omitting blank lines and comments

import sys
import re

def main():
    print(count_lines())






















def count_lines():

    if len(sys.argv) != 2:
        sys.exit("Invalid number of arguments")

    filename = sys.argv[1]

    if not filename.endswith('.py'):
        sys.exit("Invalid file type")

    counter = 0
    empty_line = re.compile(r'^\s*$')
    comment = re.compile(r'^\s*#')

    try:
        with open(filename) as file:    #default mode is read
            for line in file:           #line is a default defined in python for the lines in a program
                if not empty_line.match(line) and not comment.match(line):
                    counter += 1

            return counter

    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main()
