

#description: create a new file with specific headers/columns based on an old file with some constraints (exits with error message if not exactly three cmd-line arguments and if input file can't be read)


#to get input data/file run: wget https://cs50.harvard.edu/python/2022/psets/6/scourgify/before.csv

import sys
import csv

def main():

    file1, file2 = check_number_arguments()
    create_csv(file1, file2)



















def check_number_arguments():

    if len(sys.argv) != 3:
        sys.exit("Invalid number of arguments")

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    return file1, file2


def create_csv(file1, file2):

    try:
        with open(file1, 'r') as infile, open(file2, 'w') as outfile:   #--> open two files simultaneously in different modes
            reader = csv.DictReader(infile)     #-->reads from input file
            fieldnames = ["first","last","house"]
            writer = csv.DictWriter(outfile,fieldnames=fieldnames) #--> writes to output file
            writer.writeheader()    #--> needed to "know" the column names --> writes fieldnames in first row

            for row in reader:
               lastname, firstname = row["name"].split(',')

               firstname = firstname.strip("\"").strip()    #--> save as variable what should be written
               lastname = lastname.strip("\"").strip()      #--> save as variable what should be written
               writer.writerow({'first': firstname, 'last': lastname, 'house': row["house"]})       #-->use the variables to write the values to the specific columns

    except:         #--> if first file can not be read or something else goes wrong
        sys.exit("File error")



if __name__ == "__main__":
    main()

