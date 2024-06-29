def main():
    input_transform()





























#"main" function which calls subfunctions

def input_transform():
    while True:
        out_var = input("Date: ")
        try:
            if "/" in out_var:
                numeric_input(out_var)
                break
            elif "," in out_var:
                alpha_input(out_var)
                break
        except:
            pass

#---------------------------------
#subfunctions, which handle input in specific way, given by "main"-function


#input type: 9/8/1636
    #seperate input into parts (day,month,year) (clean variables)
    #conditions for day (1-31), month (1-12) and year (max. four digits)
    #if valid day, month, year add preceding 0's if needed and return wanted output format


def numeric_input(date):
    try:
        month, day, year = date.strip(" ").split("/")
        month = int(month)
        day = int(day)
        if month >= 1 and month <= 12:
            if day >= 1 and day <= 31:
                if len(year) <= 4:      #only works with str (restricted to 4 numbers to avoid abuse/too long input)
                    if len(str(month)) == 1:    #only works with str
                        month = (f"0{month}")
                    if len(str(day)) == 1:  #only works with str
                        day = (f"0{day}")
                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError

        print(f"{year}-{month}-{day}")

    except ValueError:
        input_transform()


#input type: September 8, 1636
    #seperate input into parts (day,month,year) (clean variables)
    # conditions for day (1-31), month (1-12) & in dict and year (max. four digits)
    #if valid day, month, year add preceding 0's if needed and return wanted output format
    #raise errors if datenot valid and call input_transform again --> reprompt


def alpha_input(date):

    months = {
        "January" : 1,
        "February" : 2,
        "March" : 3,
        "April" : 4,
        "May" : 5,
        "June" : 6,
        "July" : 7,
        "August" : 8,
        "September" : 9,
        "October" : 10,
        "November" : 11,
        "December" : 12
    }


    try:
        month, day, year = date.strip(" ").split(" ")
        if month in months:
            month = months[month]
        day = day.strip(",")
        year = year.strip(" ")

        month = int(month)
        day = int(day)
        if month >= 1 and month <= 12:
            if day >= 1 and day <= 31:
                if len(year) <= 4:  #only works with str
                    if len(str(month)) == 1:    #only works with str
                        month = (f"0{month}")
                    if len(str(day)) == 1:  #only works with str
                        day = (f"0{day}")
                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError

        print(f"{year}-{month}-{day}")

    except ValueError:
        input_transform()


main()


#if for the subfunctions return instead of print would be used, for faulty date inputs, the subfunction would return no value (declared as "None" by default).
#Since the subfunctions keep calling the "main"-function until a valid date is entered, for every faulty date input there will be a "None" output,
#preceding the valid date input, which ends the program and displays all of the return values.

#if a function returns no value it always returns "None" (also if the function prints something).
#But the "None" is only printed to the console by default, if:
    #1.it is preceding to the final answer/console output which terminates the program
    #2.it comes after the "answer" of the function but there are still commands left/program is not terminated

#not if it comes after the final answer/console output which terminated the program



#possible additional refinements for security
    #avoid/handle float inputs for year, month, day
    #avoid/negative inputs for year
