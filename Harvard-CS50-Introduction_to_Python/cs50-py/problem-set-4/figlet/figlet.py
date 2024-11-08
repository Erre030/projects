
#description: render an input to 3d-font if valid amount of sys.argvs and specific parameters are provided.



#pip install pyfiglet

from pyfiglet import Figlet
import random
import sys

    #check/handle argv conditions/constraints first --> progress with "actual" program if valid
    #define exit cases first to make program more efficient/faster and more secure

def main():
    transform_text()



















#try/except blocks could also be used for function

def transform_text():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("Invalid number of arguments")

    figlet = Figlet()

    if len(sys.argv) == 1:      #render input with random font from library pyfiglet
        text = input("Input: ")
        valid_fonts = figlet.getFonts()
        random_font = random.choice(valid_fonts)
        figlet.setFont(font=random_font)
        print(figlet.renderText(text))

    elif len(sys.argv) == 3:    #render input with specific font from library pyfiglet

        valid_fonts = figlet.getFonts()

        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid parameter. Use -f or --font")

        if sys.argv[2] not in valid_fonts:
            sys.exit("Invalid font")

        else:
            text = input("Input: ")     #input needs to come after exit cases, would create endless loop when checking results otherwise
            font = sys.argv[2]
            figlet.setFont(font=font)
            print(figlet.renderText(text))


main()
