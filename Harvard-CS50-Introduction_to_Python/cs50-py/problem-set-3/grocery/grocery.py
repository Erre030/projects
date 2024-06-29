def main():
    sorted_dict = input_items()
    print_list(sorted_dict)



























#input items: make them upper case, add them to dict, count them, sort the dict alphabetically

def input_items():

    grocery_list = {}

    while True:
        try:
            object = input("").strip().upper()
            if object in grocery_list:
                grocery_list[object] += 1 #increase value of object by one
            else:
                grocery_list[object] = 1 #new entry in dict

        except EOFError:    #EOF (ctrl+d) --> ends input
            print("\n")
            sorted_dict = dict(sorted(grocery_list.items())) #sort dict alphabetically
            return sorted_dict


#achieve specific output of value first, key second

def print_list(dict):

    for key, value in dict.items(): #when using dict.items(), first variable are always the keys, second ones the values. For every key/value in dict ...
        print(f"{value} {key}")



main()
