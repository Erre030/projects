def main():

    out_var = input("Type in arithmetric expression. Every part should be seperated by a space: " )

    try:
        x,y,z = out_var.split()

        result = interpreter(x,y,z)

        print(result)

    except:            #prohibits program from crashing with a individual error message. This way, it is harder to exploit weaknesses of the program and the output is more user friendly.
        print("invalid input")




























def interpreter(x,y,z):

    x = int(x)
    z = int(z)

    allowed_y = ("+", "-", "*", "/")

    if y in allowed_y:

        match y:
            case "+":
                res = float(x+z) # if one number is float, all numbers will be promoted to float and result will also be float
                return res
            case "-":
                res = float(x-z) # if one number is float, all numbers will be promoted to float and result will also be float
                return res
            case "*":
                res = float(x*z) # if one number is float, all numbers will be promoted to float and result will also be float
                return res
            case "/":
                if z != 0:
                    res = float(x/z) #automatically results in float value, also if only ints used
                    return res
                else:
                    print("invalid input")

    else:
        print("invalid input")



main()
