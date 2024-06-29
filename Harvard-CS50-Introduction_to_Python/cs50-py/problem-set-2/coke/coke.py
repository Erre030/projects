def main():

    print(accepted_coins()) #print return value directly


























def accepted_coins():

    valid_coins = [5,10,25]
    coins = 50

    print(f"Amount Due: {coins}")       #set start value for loop and calculate its first input
    coin = int(input("Insert Coin: "))
    if coin in valid_coins:
            coins = coins - coin


    while coins > 0:
        print(f"Amount Due: {coins}")
        coin = int(input("Insert Coin: "))
        if coin in valid_coins:
            coins = coins - coin

    return (f"Change Owed: {abs(coins)}")   #absolute value


main()
