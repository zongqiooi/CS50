import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Read database file into a variable
    nameToSTR = {}
    fileCSV = open(sys.argv[1], "r")
    reader = csv.reader(fileCSV)
    next(reader)
    for row in reader:
        nameToSTR[row[0]] = []
        for STR in row[1:]:
            nameToSTR[row[0]].append(int(STR))
    fileCSV.close()

    # Read DNA sequence file into a variable
    fileDNA = open(sys.argv[2], "r")
    DNA = fileDNA.read()
    fileDNA.close()

    # Read STR subsequence into a variable
    STR = []
    fileCSV = open(sys.argv[1], "r")
    reader = csv.reader(fileCSV)
    for i in list(reader)[0][1:]:
        STR.append(i)
    fileCSV.close()

    # Find longest match of each STR in DNA sequence and check database for matching profiles
    for i in nameToSTR:
        diff = 0
        for j in range(len(STR)):
            longest = longest_match(DNA, STR[j])
            if longest != (nameToSTR[i])[j]:
                diff += 1
        # No difference in the number of STR 
        if diff == 0:
            print(i)
            return

    print("No match")
    return


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
