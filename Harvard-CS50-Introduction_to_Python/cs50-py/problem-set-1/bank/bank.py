def main():
    output_var = input("Greeting: ")

    greeting = output_var.lower().strip()

    if greeting.startswith("hello"): #match can't handle functions directly
            print("$0")
    elif greeting.startswith("h") and not greeting.startswith("hello") :
            print("$20")
    else:
            print("$100")

#solution with regular expressions also possible












main ()
