
#comments:
# comment signle line: # , comments multi lines """..."""
#------------------------------------------------------------------------

#general:

#interactive mode: you can run code without saving it in files, just in the terminal --> type in python to choose paython as interpreter

#in documentations [] brackets often refer to something optional

# to define functions at the bottom of file : put all of your main-program into the main function, but the functions. At the EOF run main() --> this way each function is defined before executed

# scope: variable can only be used in the function it is created in --> can be changed by using global variables
#------------------------------------------------------------------------

#print function:
# input command expects str, can be specified with input to other types : e.g. (int(...)) or similar
# print ("text", variable) --> ("Hello ", David) --> output: Hello David // print ("text" + var. 0 + var. 1 + var. 2)

#sep= " " --> tells us how to seperate each input in the print function
#end= "\n" --> tells what print will do after finished at the end of the line

# you can use single quotes on outside and double quotes on inside as long as you are consistent: e.g. print('hello,"friend"') --> output: hello, "friend"
#// escape chars: print("hello, \" friend\"")
#--> more elegant(formatted string): print(f"Hello, {variable}")

#------------------------------------------------------------------------
#string properties: ( all inputs from keyboards are str at first)
    #strip things off the variable at begin and end -->e.g. strip white-spaces: variable = variable.strip()
    #capitalize --> variable = variable.capitalize() --> capitalize first letter
    #variable = variable.title() --> capitalize first letter of every word
    # first, last = name.split(" ") --> split string in variable name and safe parts in first and last (from left to right), parts are seperated by (" ")

#------------------------------------------------------------------------
#int properties:
    #mathematical operator usable: +,-,*,/,%) --> % takes remainder after division
    #beware when using operator to not concatenate strings/perform operation on strings, but on ints--> typecast used values:  int(x) + int(y)
    #no size-bound on ints

#------------------------------------------------------------------------
#float properties: (encompasses ints)
    #round(number[, ndigits] --> round a number to the nearest int. You can specify which decimal place you want to be rounded to
    # // print(f"{var:.2f}") --> does the same as round on 2 places
        # (if you choose one bigger than 0 you get a float // if you use negative numbers you take places before decimal point)
    #bound: float can represent up to 15-17 decimal places (64-bit) or 6-9 (32-bit) --> 64-bit/32-bit is maximal capacity which a computer can address simultaneously
    # automatic format for numbers: print(f"{variable:,}") --> seperates number with , --> 1,000,000

#------------------------------------------------------------------------
#function properties (def):
    #parameters: what you can pass into a function , arguments: specific values you passed to a function
    #you can nest functions: e.g. int(input("...")) --> inner function becomes argument of outer function
    #functions always use ()

    #when defining a function the parameters are just placeholders --> if you use a function afterwards you choose which exact arguments you want to use for this function

    #set default for function: def function-name (parameter="default action") --> if function is called without specific argument, default action is executed

    #method --> integrated/build into python functions: object.method() --> e.g. variable = variable.strip() --> (connected by . )
        #you can chain methods --> e.g. name = name.strip().title() // name = input("What's your name? ").strip().title() --> get executed in order (first strip, then title)

    #return: returns a specific value of the function --> eg. def square(n): return n*n --> makes values from functions usable in other functions
        #needs to be used bc. of defining main function and structure program accordingly (put defined functions are at the EOF)
