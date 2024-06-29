import re

def main():

    out_var = input("camelCase: ")

    camel = snake_case(out_var)

    print (f"snake_case: {camel}")





















def snake_case(string):

    low_list = []
    parts_list = re.split(r"(?=[A-Z])",string) #positive lookahead: reg. ex., which splits before upper-case

    for part in parts_list:
        low = part.lower()
        low_list.append(low)

    camel = "_".join(low_list)
    return camel

main()
