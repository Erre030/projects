def main():
    compute_sum()   #print of result already done in function --> no return value needed
                    #print(compute_sum()) would only display one return value, but we want to show the Total after each item added, so the function has no return just print commands
                    #return --> hands back single value and ends function / function without return and with print, can print multiple values defined in function



 
























def compute_sum():

    menu ={
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0   #create variable needed later

    while True:
        try:
            item = input("Item: ").strip().lower().title()
            if item in menu:
                value = float(menu[item])
                total += value
                print(f"Total: ${total:.2f}")
        except EOFError:    #EOF (ctrl+d) --> ends input
            break
        except KeyError:    #item not in dict
            pass

    print("\n")


main()
