def main():
    out_var = input("What time is it?: ")

    try:    # 12 hour-time (a.m. & p.m.)
        time_value, day_time = out_var.split()

        time, day = convert12(time_value,day_time)

        meal_time12 = meal12(time,day)

        print(meal_time12)

    except: # 24 hour-time
        time_value = convert(out_var)

        meal_time  = meal(time_value)

        print(meal_time)

# to make the program more secure, checks could be included so you only get an output if you type in max two digits ##:##
# to make the program more user friendly, a specific output in addition to "None" could be generated to help the user to type in the right format














def meal12(time_value,day):
    if time_value >= 7.0 and time_value <= 8.0 and day == 0:
        return "breakfast time"
    elif time_value >= 12.0 and time_value <= 13.0 and day == 1:
        return "lunch time"
    elif time_value >= 18.0 and time_value <= 19.0 and day == 1:
        return "dinner time"


def convert12(time,day):
    h, m = time.split(":")
    hour = float(h)
    min = float(m)

    min_float = min/60

    if day == "a.m.":
        day = 0
    elif day == "p.m.":
        day = 1

    return(float(hour+min_float), day)


def convert(time):
    h, m = time.split(":")
    hour = float(h)
    min = float(m)

    min_float = min/60
    return float(hour+min_float)


def meal(time_value):
    if time_value >= 7.0 and time_value <= 8.0:
        return "breakfast time"
    elif time_value >= 12.0 and time_value <= 13.0:
        return "lunch time"
    elif time_value >= 18.0 and time_value <= 19.0:
        return "dinner time"


if __name__ == "__main__":
    main()
