from cs50 import get_float

# input
while True:
    dollars = get_float("Return: ")
    if (dollars > 0):
        break

cents = dollars * 100

# quarters
quarters = int(cents / 25)
cents = (cents % 25)

# dimes
dimes = int(cents / 10)
cents = (cents % 10)

# nickels
nickels = int(cents / 5)
cents = (cents % 5)

# pennies
pennies = int(cents / 1)

# sum
coins = quarters + dimes + nickels + pennies
print(f"Number of coins: {coins}")