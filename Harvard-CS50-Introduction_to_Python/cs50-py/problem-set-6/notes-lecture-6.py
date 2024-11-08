#------------------------------------------------------------------File I/O (input/output of files)--------------------------------------------------------------------------

#load and save data persistently in files instead of memory

#open("file-name.suffix",type of open (e.g. "w","r","a")) --> write,read,append (if omitted, "r" is the default)

     #---> e.g. for appending names to a new program:
                # file = open("names.txt","a")
                #file.write(f"{name}\n") --> write to file
                #file.close() --> close and save file

                    #--> more easy and pythonic way (automatically closes file  for you):
                        #with open("names.txt","a") as file:
                            #file.write(f"{name}\n")

    #--->e.g. read all lines from file:
                #with open("names.txt","r") as file:
                    #lines = file.readlines() --> returns a list
                    #for line in lines:
                        #print("hello,", line.rstrip()) --> remove double new lines


                    #--->more easy and pythonic way:
                        #with open("names.txt", "r") as file:
                            #for line in file:
                                #print("hello,", line.rstrip())

        #alter data from file and print it afterwards:
                #1.create variable
                #2.fill variable with wanted data
                #3.perform actions on variable
                    #--> e.g.
                            #names = []
                            #with open("names.txt") as file:
                                #for line in file:
                                    #names.append(line.rstrip())

                            #for name in sorted(names):
                                #print(f"hello, {name}")


#----------------------CSVs------------------------
#use csv-files for multiple data in one file (comma seperated values)
    #--> seperated values by split(",") and save them in one or multiple variables to use them later on

    #turn different values which are conjuncted with each other to dictionaries, sort them by a specific parameter and print the outcome


        #e.g. sort after names and gove back the name and the corresponding house
        # students = []

        #with open("students.csv") as file:
           # for line in file:
            #    name,house = line.rstrip().split(",")
            #    student = {"name": name, "house": house}
             #   students.append(student)       --> will encompass all dictionaries (each dictionary stays intact) --> e.g. three entries in name and house (three lines) = three dicts

           # def get_name(student):
            #    return student["name"]

           # for student in sorted(students, key=get_name):     --> sorts dictionaries by the key ("name" in this case) --> sorted calls function for you
             #   print(f"{student['name']} is in {student['house']}")



    #------------------------------------------------>elementary structures can be combined with conditionals, etc. to tackle more sophisticated tasks (all files: txt,csv,...)


#--> if function just needed once, you can use a lamba function (anonymus function)
	#-->instead of extra function for key value, tighten up code further: key=lambda paramter/parameters, wanted return value --> e.g. key=lambda student: student["name"]

#if commas in the entries of csvs make the program crash/lead to unwanted behaviour --> mark eentries by "..." and use csv library
	#--> use reader instead of defining everything yourself --> reader handles parsing of commas, new lines , etc. (all operations/functions needed --> for more info/varieties look into documentation)
		#--> reader returns lists for every row (entry)

		#--> code (for sorting after key: name) with lambda and csv reader:
    # Reads a CSV file using csv.reader and prints the content

    #import csv

    #students = []

    #with open("students1.csv") as file:
    #   reader = csv.reader(file)
    #   for row in reader:
    #     students.append({"name": row[0], "home": row[1]})

    #for student in sorted(students, key=lambda student: student["name"]):
    #   print(f"{student['name']} is from {student['home']}")

#------------------------------

    #more robust version: use dict reader --> add column names sepearted by comma in first line --> dict reader returns dictionaries
    #(-->code breaks much less)

    # Reads a CSV file using csv.DictReader

    #import csv

    #students = []

    #with open("students2.csv") as file:
        #reader = csv.DictReader(file)
        #for row in reader:
           # students.append({"name": row["name"], "home": row["home"]})

    #for student in sorted(students, key=lambda student: student["name"]):
        #print(f"{student['name']} is from {student['home']}")

#--------------------------

    #create csv with dict writer:

        ## Writes a CSV file using csv.DictWriter

        #import csv

        #name = input("What's your name? ")
        #home = input("Where's your home? ")

        #with open("students2.csv", "a") as file:
        #   writer = csv.DictWriter(file, fieldnames=["name", "home"])      --> fieldnames are the columns which are in this file (order doesn't matter)
        #    writer.writerow({"name": name, "home": home})


#---------------------------------

#other file formats:
    #binary files (0s and 1s)
    # audio, video, etc.
    # image files --> (library PIL (pillow)) to alter/animate/...
        #--> e.g. creating a gif
            #select pictures you want to use (e.g. costum1.gif, costume2.gif)

            #import sys
            #from PIL import Image

            #images = []

            #for arg in sys.argv[1:]:       --> add all pictures needed for gif to list, typed into command line
                #image = Image.open(arg)
                #images.append(image)

            #images[0].save(                            -> save first image as "costumes.gif" and append second image to it, save_all --> safe all images in costumes.gif, duration --> how many milisec. image is shown, loop=0 --> loops forever
            #    "costumes.gif", save_all=True, append_images= [images[1]], duration=200, loop=0
            #)

#--------------------------------------------------------------

#------> look videos on pillow and working with csvs if needed
