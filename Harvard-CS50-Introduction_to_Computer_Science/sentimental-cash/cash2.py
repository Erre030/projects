# TODO


from cs50 import get_float


# Ask how many cents the customer is owed
while True:
    dollars = get_float("Return: ")
    if (dollars > 0):
        break

# convert to cents
cents = dollars * 100

# quarters
quarters = 0
while (cents >= 25):
    cents = cents - 25
    quarters = quarters + 1
    if (cents < 25):
        break

# dimes
dimes = 0
while (cents >= 10):
    cents = cents - 10
    dimes = dimes + 1
    if (cents < 10):
        break

# nickels
nickels = 0
while (cents >= 5):
    cents = cents - 5
    nickels = nickels + 1
    if (cents < 5):
        break

# pennies
pennies = 0
while (cents >= 1):
    cents = cents - 1
    pennies = pennies + 1
    if (cents < 1):
        break


# Sum coins
coins = quarters + dimes + nickels + pennies

# Print total number of coins to give the customer
print(f"Number of coins: {coins}")