
# description: put in exactly two cmd-arguments, where the second one is the number of bitcoins.
            # Show the current bitcoin price in "$" by using the coindesk-api for the amount of bitcoin presented in the cmd-line.


import requests
import sys

def main():
    calculate_bitcoin()






















def calculate_bitcoin():

    if len(sys.argv) < 2:
        sys.exit("Missing or extra command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many extra command-line arguments")

    try:
        bitcoin_amount = float(sys.argv[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")


    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    data = response.json()          #transform json data into python dictionaries to be able to use/extract values
    price = data["bpi"]["USD"]["rate_float"]    #access nested dictionaries like lists (begin with the "biggest" one) --> "bpi" accesses the dictionary "bpi" and its data, ...
    final_price = bitcoin_amount * price

    print(f"${final_price:,.4f}")   # (:,.4f) --> "," is sign used to split thousands (only "," can be used). 4f is used to show four decimal places



if __name__ == "__main__":
    main()
