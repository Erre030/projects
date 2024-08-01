# unit tests --> keep tests as simple as possible

    #writing own code to test the code you have written (most representative cases)
        # --> if __name__ == "__main__": main() needed, since we use another program to test the program we've written

    #unit test structure:
        # new file: test_filename,py
        # import specific function/functions you want to test

    #first approach:
        # def test_functionname() --> use conditionals to check expected function outputs (--> e.g. if square(3) != 9: print("3 squared was not 9") )
        #--> always test multiple cases, you might get lucky on some cases and oversee failure/dysfunctionality

        #--> use assert to make testing more convenient and robust than tedious method using conditionals

    #second approach:
        #using assert:
            #claims something is true. If it isn't it throws an error (--> e.g. assert square(3) == 9 --> assert shows which line the error is from)
                #--> use try/except to try assertions and except AssertionError

    #third/final and best approach:
        #Use pytest(or some other library designed for testing), so you do not have to write this much code: (pip install ...)
        #-->you just have to write the tests themself (e.g. assert square(2) == 4) and pytest will do the rest --> pytest test_filename (shows you the test that is incorrect)
        #pytest will only run the tests included in a function until it runs into the first error --> seperate different areas to test into different functions, so all will be tried (e.g. test positve numbers, ngeative numbers and 0 seperately)
        #(you can also use loops and the like to automize the testing even further)
        #(you can test not only files, but even whole directories)

        #if type of variable is wrong (e.g. str instead of int) --> do another test_function, where you use functionality of pytest to raise a TypeError if this happens
            #def test_str():
                #with pytest.raises(TypeError):
                    #square("cat") --> generic term for all strings in this case

        #(recursive functions can be also tested with unit tests in a similar way)

        #--> overall: your functions need to return something to be tested, not printing it directly --> assert tests the return value of a function == smth.

        #run folder with multiple test files --> create a file called __init__.py to tell python that it should treat the folder where the file is included as a package and searches whole folder for possible tests
            #use: pytest foldername

        #no main() function needed for the points above --> pytest takes care of that too



