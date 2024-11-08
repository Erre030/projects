#styleguide specific to python

#PEP 8 (Python Enhancement Proposal) --> try to standardize how code should look like
    #readability counts
    #consistency counts
    #PEP 8 prescirbes how you shall use: indentation, maximum line length, nlank lines between code, imports,... --> website


    #libraries to check for appropriate style (pip install ...)
        #pylint --> very noisy, just points at things you've done wrong
        #pycodestyle --> standard --> reformates code for you
        #black --> oppinionated in the style code gets formatted
        #--> every company/etc. may have their own preference of style/own styleguide



# always write if__name__ = "__main__" before the execution of the main-function at the bottom of the program


# always let a specific function return a value and let the main function print the value --> this makes the program testable by using unit tests
