
#description: transform and print csv file into pretty printed table using function of library tabulate.
            # Error, when file is not a csv, when not the right amount of cmd-line arguments or if file doesn't exist.

#run in cmd to get files:
    # wget https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv
    # wget https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv

#run in cmd for libraries:
    #pip install tabulate

import csv
import sys
import tabulate #use required by exercise

def main():
    print(transform_csv())



















def transform_csv():

    if len(sys.argv) != 2:
        sys.exit("Invalid number of arguments")

    filename = sys.argv[1]

    if not filename.endswith('.csv'):
        sys.exit("Invalid file type")

    try:
        with open(filename) as file:    #default mode is read
            reader = csv.reader(file)   #returns a variable of the csv.reader of type csv.reader, where each row is included as a seperate list (specific type, very user friendly/designed for csvs)
            table = list(reader)        #transform csv.reader into type list (also works without, but more clean this way) --> table is list of lists

            ascii_art = tabulate.tabulate(table, headers="firstrow", tablefmt="grid")   #transform csv-file into pretty-print table, (table needed to be list of lists, headers = first row of file)

            return ascii_art

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
