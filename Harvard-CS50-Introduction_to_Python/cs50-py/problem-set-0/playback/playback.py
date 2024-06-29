def main():
    input_var = input("Please provide input: ")
    words = input_var.split()
    playback_str = "...".join(words) #join parts together using specific seperators
    print(playback_str)


main()
