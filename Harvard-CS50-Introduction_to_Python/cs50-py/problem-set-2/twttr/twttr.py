def main():
    out_var = input("Input: ")

    print(generate_text(out_var))


























def generate_text(string):

    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    text = ""

    for letter in string:   #iterate over every char in the string
        if letter not in vowels:
            text += letter

    return text

main()
