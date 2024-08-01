def main():

    out_var = input("Greeting: ")
    print(value(out_var))


























def value(greeting):

    greeting = greeting.lower().strip()

    if greeting.startswith("hello"): #match can't handle functions directly
            return 0
    elif greeting.startswith("h") and not greeting.startswith("hello") :
            return 20
    else:
            return 100


if __name__ == "__main__":
    main()





















