
#description : transform 12-hour time into 24-hour time using regexs.

import re

def main():
    print(convert(input("Hours: ")))























def convert(s):

    if not re.search(r"^(1[0-2]|[1-9]):?([0-5][0-9])?\s(AM|PM)\s(?:to\s)?(1[0-2]|[1-9]):?([0-5][0-9])?\s(AM|PM)$", s):
        raise ValueError

    else:
        matches = re.search(r"^((?:1[0-2]|[1-9]):?(?:[0-5][0-9])?)\s(AM|PM)\s(?:to\s)?((?:1[0-2]|[1-9]):?(?:[0-5][0-9])?)\s(AM|PM)$", s)  #-->exclude groups for matches also if they are encompassed by another group

        #matches.group(1) --> hour start
        #matches.group(2) --> (AM|PM)
        #matches.group(3) --> hour end
        #matches.group(4) --> (AM|PM)




    #start-times

    if matches.group(1) and matches.group(2) == "AM":       #for inputs like: 9:00 AM
        if (":") in matches.group(1):
            hour, min = matches.group(1).split(":")
            hour = int(hour)

            if hour == 12:                  #edge case 12:00 AM --> 00:00
                hour = 0

            start = (f"{hour:02}:{min}")

        else:                                               #for inputs like 9 AM
            hour = matches.group(1)
            hour = int(hour)

            if hour == 12:
                hour = 0

            start = (f"{hour:02}:00")                           #pad int with preceding 0's so it is at least two digits wide (required format for output)

    elif matches.group(1) and matches.group(2) == "PM":     #for inputs like: 9:00 PM

        if (":") in matches.group(1):
            hour, min = matches.group(1).split(":")
            hour = int(hour)

            if hour == 12:                  #edge case 12:00 PM --> 12:00
                hour = 0

            hour = hour + 12
            start = (f"{hour:02}:{min}")

        else:
            hour = matches.group(1)                         #for inputs like: 9 PM
            hour = int(hour)

            if hour == 12:
                hour = 0

            hour = hour + 12
            start = (f"{hour:02}:00")

    #end-times --> same mechanics and descriptions like for start-times

    if matches.group(3) and matches.group(4) == "AM":
        if (":") in matches.group(3):
            hour, min = matches.group(3).split(":")
            hour = int(hour)

            if hour == 12:
                hour = 0

            end = (f"{hour:02}:{min}")

        else:
            hour = matches.group(3)

            if hour == 12:
                hour = 0

            hour = int(hour)
            end = (f"{hour:02}:00")

    elif matches.group(3) and matches.group(4) == "PM":
        if (":") in matches.group(3):
            hour, min = matches.group(3).split(":")
            hour = int(hour)

            if hour == 12:
                hour = 0

            hour = hour + 12
            end = (f"{hour:02}:{min}")

        else:
            hour = matches.group(3)
            hour = int(hour)

            if hour == 12:
                hour = 0

            hour = hour + 12
            end = (f"{hour:02}:00")



    shift = (f"{start} to {end}")

    return shift





if __name__ == "__main__":
    main()

