#reading and writing csvs

#use csv library

#example  comands (not specifically ordered, just for functionality purposes)

    #with open("filename.suffix", mode) as file:
        #reader = csv.DictReader(file)      --> reads every row and outputs every row as a dict
        #writer = csv.DictWriter(file, fieldnames= reader.fieldnames)      --> writes dicts into file with specific keys(fieldnames)
        #writer.writeheader()       --> writes headers to file
        #writer.writerow({keys and values for keys})          -->writes new row to file
        #for row in reader:
            #row["key"]             --> add new key/columns to csv
            #print(row["key"])       -->prints value for key


#open two files simultaneuosly:
    #with open("filename.suffix", mode) as file, open("filename.suffix", mode) as file2:
