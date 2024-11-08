
# description: check if input is valid IP4-address.

import re

def main():
    print(validate(input("IPv4 Address: ")))























def validate(ip):


    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if len(part) > 3:       #only maximum of three bits for each part, not e.g. 00123
             return False

        if not re.search(r"^\d+$",part):
                return False

        part_number = int(part)

        if part_number < 0 or part_number > 255:
            return False

    return True
























if __name__ == "__main__":
    main()
