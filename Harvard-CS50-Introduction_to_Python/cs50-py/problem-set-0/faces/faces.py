def main():
    input_var = input("Please provide input: ")
    faces = convert(input_var)
    print(faces)










def convert(str):
    return str.replace(":)","🙂").replace(":(","🙁")


main()
