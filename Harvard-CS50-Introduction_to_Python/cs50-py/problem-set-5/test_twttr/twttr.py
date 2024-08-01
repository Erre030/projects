
#description: get string as input and omits all uppercase and lowercase vowels in its return (twitter --> twttr)

def main():
    out_var = input("Input: ")

    print(shorten(out_var))




























def shorten(string):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    text = ""

    for letter in string:   #iterate over every char in the string
        if letter not in vowels:
            text += letter

    return text


if __name__ == "__main__":
    main()
