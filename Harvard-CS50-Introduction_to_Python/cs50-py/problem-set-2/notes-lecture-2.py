
#general:
    #for more complex problems you can use loop nesting, string multiplication and other intermediate techniques (e.g. print bricks of mario-2d-world)
    #in addition to try/except blocks, return ""/return None is also a way to "ignore" invalid input/output nothing



#------------------------------------------------------------------------
#loops

#while: while (statement) --> while statement is true do the following... (end infinite loop --> strg+c) --> you have to use a boolean statement
    #e.g.:
       # i = 0
       # while i < 3:
        #    print("meow")
        #    i = i+1 // i += 1 (--> no ++,-- possible in python)
    #print meow three times

#for: (simpler than while loop)
    #use function similar to list in python --> range: sets number where you want to count to but not through the number --> e.g. for i in range(3) will repeat three times (0,1,2)
        #further additions to range possible, e.g. you can choose strating element and how big the step-size shall be each step
    #if you use a variable just for counting/iterating through the loop and nowhere else, use an underscore --> e.g. for _ in range(3)
        #--> exception, when it provides important info, e.g.: for student in students ....
    #iteration over lists is also possible --> e.g.: students = ["a","b","c"], for student in students: ...

    #use of range:
    #range is most suitable for simple counting problems with a large amount of samples/elements
        # --> accepts only integers (but objects can be assigned int-indexes by using len --> makes range useful in some cases that go beyond simple counting)

    #every data that is iterable can be used with a for-loop --> lists,arrays,range ... --> pick of datatype depends on individual case/goal

#------------------------------------------------------------------------

#list [] (data-type)
    #indexed at 0 (starts at 0)
    #encompasses a number of variables
    #there are further special propertes of lists (which item you can pick, etc.)
    #choose specific element list-name[element-number]
    #elements-indexes are only numeric, can't use strings for indexing into list

    #disadvantages:
    #lists can hold multiple data types simultaneously and have very little built-in-constraints --> can be a danger for safety and can hinder processes which expect uniform data types
    #not good for fast lookups (linear search)--> use dicts or the like
#------------------------------------------------------------------------

#print
    #you can print something multiple times by multiply it: e.g.: print("meow\n" * 3, end="") --> prints three lines with meow on each --> (without \n it would print everything inside one line)
#------------------------------------------------------------------------

#typical paradigmns:

    #get certain input from user: while true loop (question until wanted input is provided) (-->could be more restricted with try/except --> depends on use case)
        #e.g.
        #while True:
            #n = int(input("What's n? "))
           # if n < 0:
                #break (breaks out of loop/ends loop when condition is satisfied)
                #// if you do this inside of a seperate function you can also use return instead of break to return the value and automatically exit the function.

#------------------------------------------------------------------------
#len:
    #get length of something (allows you to go through something by using numbers --> as iteration for for lops e.g.)
        #e.g. number of objects in string-list -->  for i in range (len(students)): #print(i+1,students[i]) (-->use iteration variable student to look up the specific keys and print the values)

#------------------------------------------------------------------------
#dicts {} (data type):
    #associate one thing with another (key:value)
    # can also use strings to index into dict
    # for-loop by default iterates over keys of dict --> for student in students: print(student)
    #usage example: print single key and value
        #--> for student in students: print(student,students[student], sep=", ") --> prints keys and values seperated by a comma (--> student -variable is used to access values of each key)
    #usage example: print multiple key values/have multiple traits
        #--> create a list of dictionaries
            #students = [
                       # {"name": "a", "house": "blue", ...}
                       # {"name": "b", "house" : "yellow", ...}
                       # ...
                       # ]
            #-->pick the data you want to be printed
            #for student in students:   (-->use iteration variable student to look up the specific keys and print the values)
                #print(student["name"], student["house"], ..., sep=", ")

#------------------------------------------------------------------------
#None (data type)
    #symbolizes the abscence of a value



