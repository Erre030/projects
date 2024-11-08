#et cetera


#datatype: set() --> datatype with no duplicates (duplicates are eliminated for you/will not be added)


#-------

#global keyword: global variables are not changeable, variables inside certain functions are only accessible by those functions (scope)
    #so to define a global variable which is changeable, the keyword global is used:

    #e.g.
        #balance= 0

        #def deposit(n):
            #global balance
            #balance += n

    #-->rather use classes and define specific instance variables --> cleaner and more flexible (can be manipulated for specific instances differently without the need of using global)

#----------

#constant: define values for variables at the top of the file/class in all uppercase (hints visually that it is the constant, but it still can be changed further down the program)

#----------------


#type hints: python does dynamically type assignment in contrast to other languages, where you have to name the type of a variable specifically. We can use type hints to emulate this behaviour in python
    #e.g. def meow(n:int) -> None (input is int and return of function is none/no return) // number: int = input("Number: "), ... --> sadly python ignores the hints, but you can check them using mypy
        #program for checking if code is adhering to given type hints: mypy (pip install mypy) --> mypy program.py

#----------------

#docstrings: standard way how you shall comment your functions (using within the dosctring a convention e.g. "restructured text")
    #using: """...""" --> python recognizes those kind of comments which gives you the ability to automatically extract explanations and documentations out of your code instead of doin them manually
        #e.g.:
            #def meow(n: int) -> str:

                #"""
                # Meow n times.
                #
                #:param n: Number of times to meow
                #:type n: int
                #:raise TypeError: If n is not an int
                #:return: A string of n meows, one per line
                #:rtype: str (return type)
                # """
                #
                #return "meow\n" * n

#-------------------------------

#giving commands at the cmd-lines and "customize" them:(single "-" is used for only a letter, "--" is used for whole word to follow)
    #library: argparse --> helps to "customize" / build more advanced structure for commands on cmd-line

        #e.g.:
        #import argparse

        #parser = argparse.ArgumentParser(description="Meow like a cat")    #create instace of argument parser and describe the program
        #parser.add_argument("-n", default=1, help="number of times to meow", type=int)
            # -->add arguments/customizations/flags you want to use and specify the type the default value (used if -n not used), type: type used (will automatically be transformed to that type by library, will generate error automatically if not possible), add instructions for the command via "help"
        #args = parser.parse_args()   --> args encompasses all parsed command line arguments
            #-->as a result, we can get the information we provided above on the arguments using meow.py -h or --help

        #for _ in range(args.n):    --> contains argument typed after -n, if we would add another argument with -s, we could target this rule via args.s and so on ...
            #print("meow")


        #--> -h and --help are already configured by the library and usable (showing help message). You can use further descriptions similar as in add_argument("-n",...) to expand description at help page for specific added arguments
        #--> usage: program name [-h] [-n N] ... is also build into library and is also outputted when you run -h or --help
            # --> square brackets mean the input is optional and N specifies that input to -n must be number

#------------------------------------------------------------------

#unpacking (split input into multiple variables) --> e.g. split()
    #more possibilities:

        #variant a:
        # use "*" before element (enumerations where order is preserved , e.g. lists) to unpack automatically: (only values are unpacked)
            #e.g.:
                #def total(galleons, sickles, knuts):
                    #return (galleons * 17 + sickles) * 29 + knuts

                #coins = [100, 50, 25]

                #print(total(*coins), "Knuts")

        #variant b: use for e.g. dicts -->use: "(**coins)" instead --> will pass in values their names (galleons=100, sickles=50, knuts=25)

    #--> we could add default values in the function to also have the possibility to unpack elements which do not align with the numbers of parameters needed by the function
        #e.g.: def total(galleons=0, sickles, knuts)

#--------------------------------------------

# *args, **kwargs (can be called anything but this is convention) --> display various number of parameters for one function --> arguments (simply values), represented as tuple // keyword arguments (values with names), represented as dictionary
    #e.g.
        #def f(*args,**kwargs) --> variable number of args :  e.g. f(100,500,25) or f(100, 40) and variable number of kwargs : e.g. f(galleons=100, sickels=50, knuts=25) or f(galleons=100)

#---------------------------------------------

#map --> apply some function to every element of a sequence
    #usage: map(function you want to call, sequence you want to call it on) --> e.g. uppercase = map(str.upper, words)

#------------------------

#list comprehension: create new list on the fly, similar to map-procedure / another alternative
    #usage: uppercase = [word.upper() for word in words] --> creates new list where all words are all elements of words are stored after applying upper function to them

    #-->only include specific entries of sequence (filter specific entries):
        #e.g.
            #gryffindors = [student ["name"] for student in students if student["house"] == "Gryffindor"] --> where students is a list

#-----------------------------------

#filter: filter(function to call (which returns boolean), sequence to apply it on) --> doesn't produce a value for every element of sequence like map, rather include/exclude element based of boolean
    #-->similar to filter for specific entries using list comprehension
    #e.g.
        #def is_gryffindor(s):
            #return s["house"] == "Gryffindor"

        #gryffindors = filter(is_gryffindor, students) --> students is a dict here

#-----------------------------

#dictionary comprehensions: create new dictionary on the fly
    #usage: gryffindors = [{"name": student, "house": "Gryffindor"} for student in students] --> where students is a list
        #-->produces a list of dicts, one dict for each student --> where students is a list
    #usage: gryffindors = {student: "Gryffindor" for student in students}
        #-->produces one big dictionary with student as keys and "Gryffindot" as values

#----------------------------

#enumerate: hands back value and its index in sequence:
    #e.g.
        #students = ["Hermione", "Harry", "Ron"]

        #for i, student in enumerate(students):
            #print(i+1, student)
        #--> this returns 1 Hermione, 2 Harry, 3 Ron

#-------------------------------------------

#generators: generate values from functions bit by bit (used to deal with memory limitations)
    #return bit by bit, not all data at once as by using "return" --> use "yield"
        #"yield" returns a so called "iterator" which allows us to iterate over the created values one at a time

            #e.g.:
                #def main():
                    #n = int(input("What's n? "))
                    #for s in sheep(n):
                        #print(s)

                #def sheep(n):
                    #for i in range(n):
                        #yield "(sheep emoticon)" * i
                            # --> hand one string of sheep back at a time to get printed by main, not all strings simultaneously (fewer overall memory needed and specific values are only computed when needed)
                            #-->if using return, we would create an empty list and append the specific values of sheep to the list. So when we return, we would return the whole list at once with all its elements
                            #-->this way we keep the functionality inside a seperate function where it belongs and do not have to do everything in main(), while still be able to be memory efficient
                #if __name__ == "__main__":
                    #main()
