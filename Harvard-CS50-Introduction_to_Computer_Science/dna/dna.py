import csv
import sys


def main():

    # TODO: Check for command-line usage

    if len(sys.argv) != 3:  # index starts at 1, programname(dna.py)
        print("Usage: python dna.py data.csv sequence.txt")
        return 0

    # TODO: Read database file into a variable

    database = []  # different data structures: [] = list, {} = dictonary
    with open(sys.argv[1], newline="") as csvfile:  # index starts at 0. (3 elements = index 0,1,2)
        reader = csv.DictReader(csvfile)
        for row in reader:
            database.append(row)

    # TODO: Read DNA sequence file into a variable

    # first you need to activate the mode of a file, then you can execute the command
    with open(sys.argv[2], "r") as dnaSequence:
        sequence = dnaSequence.read()

    # TODO: Find longest match of each STR in DNA sequence

    subSequences = list(database[0].keys())[1:]  # create list, which lists all key and afterwards excludes first key (name).
    # [0] addresses first element in database, the first ro where keys are saved. Adressing the values of the following rows would be also possible, because their values have the same keys.
    # But row could play an important role when looking at different key:value pairs, so row (specific localization) must be addressed.
    # in the list only values get saved, no keys, because of the used function.

    STRs = {}  # compare list elements with "sequence" and insert longest_match with its "subSequence" into dictonary
    for subSequence in subSequences:  # durch Liste iterieren
        STRs[subSequence] = longest_match(sequence, subSequence)
        # compare every key with the sequence. Result will be saved as [key:value] pair of the specific subsequence in STRs Dict.
        # key is the subsequence and value is the result of longest_match. Allocation of values by [key] = value.

    # TODO: Check database for matching profiles

    for i in database:  # rows of database are choosen
        match = 0  # counter-Variable for matches
        # nested for-loop to get access on both datasets. This way, you can choose the single elements in the rows of the database. (two-stage-array)
        for j in subSequences:
            if int(i[j]) == STRs[j]:  # compare values of "database" & "STRs". Convert string of database into int, so we can compare int to int.
                # goes row by row over every element and compares each elements with the elements of the STRs Dict. If keys and values are equal --> match +1.
                # if the value of the key of the specific row-element(j) of row(i) from the database ist the same as value of the keys(j) in the STRs Dict --> number of sequence must be equal.
                # depends if the calue even is in the STRs Dict at all, not if it lies at the same place as the counting-variable.
                # For the list the exact position of the couting-variable is used, for the cit the whole dict is searched for the key.

                # in general: single elements in row of list can be addressed by row[0],row[1],... . Dicts function by [key:value] pairs.

                # if an element is included in a dict/list you can find out with in ... / not ... .
                # if you need to compare specific positions in a list you have to iterate over the list (can pick specific elements after formula).
                # in a dict you can't find the specific position. If you want to find specific positions, you have to first create a list out of the specific dict-area which can then be accessed.
                match = match +1

        # if match equals length of subSequence, there is a 100% match.
        if match == len(subSequences):
            print(i["name"])
            return 0

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
