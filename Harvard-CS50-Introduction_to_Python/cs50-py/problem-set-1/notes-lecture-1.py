
#general
    # you can use methods/functions on your own functions and methods/functions in general as long as you use the datatype each sepcific function/method needs

#------------------------------------------------------------------------

# python specific:

    #---instead of checking four lines:

    #if(condition):
    #    output
    #else:
    #    output

    #---you can use all in one line:

    #return True if n % 2 == 0 else False  // even shorter, perform operation right after return --> return n % 2 == 0 (you can do similar to other operations/data-types, e.g. return (a+b))
        #close to english language

#------------------------------------------------------------------------

# conditionals (can only be booleans --> binary True/False)
    #operators: <, =>, >, =<, ==, !=
    # if you use multiple if's, all get checked which results in inordinate use of space/computing power and bigger complexity--> use if,elif,else (once we get a true answer, no more questions are answered)
        #if: for asking, elif: for asking questions after if, else: used if logically there is only one potion left/when if/elif-questions are false, a specific output is desired
    #or : compare multiple conditions (as soon one condition if true, the following do net get checked)
    #and: compare multiple conditions (all have to be true. If one is false, the whoel is not true)
    #try to always use the most efficient way with the least questions by knowing which output you want --> faster program and less complex
#------------------------------------------------------------------------

#remainder (%)
    # e.g. even number : if x % 2 == 0 // odd number: if x % 2 != 0

#------------------------------------------------------------------------
#boolean
    #data-type: True/False

#match
    # can make program tighter and better readable --> intead of : if "name1" or "name2" or "name3" --> #match can't handle functions directly only bare outputs
        # eg.
        # name = input("What's your name? ")
        #match name:
            #case "name1" | "name2" | "name3":
                #print("output")
            #case "name4":
                #print("output2")
            #case _:
                #print("output3")

# --> case _:  --> catches all other/nt known inputs and returns output3
