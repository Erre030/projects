
#-------------------------------------------------exceptions---------------------------------------------------------------------------



#general
    #python is more of the mindset: try if it works, just be sure to handle the errors/exceptions --> can be more efficient, but doesn't need to be
    #if you want to throw different error messages for specific e.g. ValueErrors, you would have to build individual except-statements with specific conditions
        #--> sometimes an error stands for multiple errors, in this case you can address the single errors of this family by naming them (e.g. ArithmeticError encompasses OverflowError, ZeroDivisionError, FloatingPointError)

#---------------------------------------------------

# try/except/else blocks (statements):
    #try: things you want to try / except: things you want to do if an error in general or a specific error occurs /else block is carried out after try block if there is no error in the try block
        #just put in the part of the code into the try block, that could cause the error (--> less code to check for program / more efficient)
        # --> if you  do not know the specific error, you can do "except" for everything by only using "except". With time you will get better and can adress specific errors
        #--> you want to address specific errors to knwo what is/could go wrong in yout ptogram and do not leave some bugs unknown --> fix them
        #--> you can address multiple different errors at once

#types of errors:
    #ValueError: wrong value/other expected value
    #NameError: something used is not defined (e.g. variable)
        #--> e.g.
                #try:
                 #   x = int(input("What's x?"))
                #except ValueError:
                 #   print("x is not an integer")

                #else:
                    # print(f"x is {x}")
                #--> if you wouldn't use else, there would be a name error, because the conversion of the wrong input (e.g. "cat") into an int does throw an error already, so there will be no value for x, so x can't be called later on


        #--> e.g. (prompt user for correct input until correct input is provided). if try throws no errors else is performed.
            #While True:
                #try:
                 #   x = int(input("What's x?"))
                #except ValueError:
                 #   print("x is not an integer")
                #else:
                    #break

                # print(f"x is {x}")

#---------------------------------------------------

# pass (statement):
    # catch something (e.g. error), but do not say anything about it (can make program more secure)
    # can be a placeholder as well, while constructing architecture of program (loops, placeholder etc. can't be empty --> "pass" needed)
    #e.g.
        #function_one():
            #While True:
                #try:
                 #   return int(input("What's x?"))
                #except ValueError:
                 #   pass

#---------------------------------------------------

# prompt for functions:
    #use prompt instead of a needed parameter for a function, which is shown to the user
        #e.g.
            #def main():
                # x = function_one("prompt of choice")
                # print(f"x is {x}")

            #function_one(prompt):
                #While True:
                    #try:
                  #   return int(input(prompt))
                 #except ValueError:
                  #   pass

            #main()

#---------------------------------------------------

#raise
    #raise exceptions yourself --> create individualized constraints (e.g. if variable > 100: raise ValueError)
    #all errors you raise with a specific type, will result in the configurated except message for this error
        # --> e.g. (a by definition ValueError will throw the same message as a raised one)
                   #raise ValueError
                   # except ValueError:
                       # print("Ivalid")

#-------------------------------------------------debugging---------------------------------------------------------------------------


# print : use print function to print out certain values and check them


#when program become more complicated or are not written by yourself:

# breakpoints: set breakpoint/breakpoints at the line where before the program should be stopped, then run the debugger (good choice: set at main() --> stops before whole program is run)
    #continue: execute code normally until end
    #step over: step over the current line while still running it
    #step into/out: step into / out of the current function
    #   --> debugger shows your variables / what actually happens
