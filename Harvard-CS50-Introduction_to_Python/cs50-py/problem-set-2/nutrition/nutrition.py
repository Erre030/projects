def main():
    out_var = input("Item: ").strip().lower()

    print(fruit_dictionary(out_var))

























def fruit_dictionary(fruit):

    fruits = {
        "apple" : 130,
        "avocado" : 50,
        "banana" : 110,
        "cantaloupe" : 50,
        "grapefruit" : 60,
        "grapes" : 90,
        "honeydew melon" : 50,
        "kiwifruit" : 90,
        "lemon" : 15,
        "lime" : 20,
        "nectarine" : 60,
        "orange" : 80,
        "peach" : 60,
        "pear" : 100,
        "pineapple" : 50,
        "plums" : 70,
        "strawberries" : 50,
        "sweet cherries" : 100,
        "tangerine" : 50,
        "watermelon" : 80
        }

    if fruit in fruits:
        return (f"Calories: {fruits[fruit]}")   #return fruit value
    else:
        return "" #other way of ignoring invalid input instead of try/except blocks


main()
