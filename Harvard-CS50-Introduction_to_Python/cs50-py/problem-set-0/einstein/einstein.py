def main():
    mass = int(input("Please type in a number for mass: ")) #every input from keyboard is first a string and has to be changed to int/float before doing computations
    joule_res = calc(mass)
    print(joule_res)










def calc(given_mass):
    m = 300000000
    joule = given_mass * (m*m)
    return joule


main()
