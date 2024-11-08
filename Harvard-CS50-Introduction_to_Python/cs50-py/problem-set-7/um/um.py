
# description: count the appereances of um (as an own word)

import re

def main():
    print(count(input("Text: ")))























def count(s):
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)           # \b...\b searches its input as an own word // # findall saves every finding in matches automatically

    counter = 0

    for match in matches:
        counter += 1

    return counter


if __name__ == "__main__":
    main()
