

#removed loops and try/except to be able to test program better/easier in comparison to fuel.py from problem-set-3

# Error automatically ends program, if it is not catched by try/except

def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    print(gauge(percent))


def convert(fraction):
    if not isinstance(fraction, str):
        raise TypeError("input must be str")

    numerator, denominator = map(int,fraction.split('/'))   #maps resulting strings to ints, throws ValueError if not possible

    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise ValueError("Please provide a valid fraction")

    elif denominator == 0:
        raise ZeroDivisionError("Divisor can't be 0")

    fuel = round((numerator / denominator)*100)

    if fuel > 100 or fuel < 0:
        raise ValueError("Please provide a valid fraction")

    return fuel


def gauge(percentage):
    if not isinstance(percentage,int):
        raise ValueError("input not int")

    if percentage <= 1:
        return ("E")

    elif percentage >= 99:
        return ("F")

    else:
        return (f"{percentage}%")



if __name__ == "__main__":
    main()
