def main():
    output_var = input("What is the Answer to the Great Question of Life, the Universe, and Everything?"  )

    meaning_of_life = output_var.lower().strip() #make input case-insensitive

    match meaning_of_life:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")










main()
