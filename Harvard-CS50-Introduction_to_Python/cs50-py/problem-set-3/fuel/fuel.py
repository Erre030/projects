def main():
    print(fuel_level())




























def fuel_level():   #errors could be catched and concealed with "pass" to make the program more secure in some cases
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = map(int,fraction.split('/'))   #maps resulting strings to ints
            fuel = (numerator / denominator)*100
            if fuel > 100:
                raise ValueError    #displays except message configured for ValueError
        except ValueError:
            print("Please type in a valid fraction")
        except ArithmeticError:     #encompasses OverflowError, ZeroDivisionError, FloatingPointError
            print("Divisor can't be 0")
        else:
            break


    if fuel <= 1:
        return ("E")
    elif fuel >= 99:
        return ("F")
    else:
        return (f"{round(fuel)}%")


main()
