infile = open("children_per_woman.csv","r")
outfile = open("result.csv","w")

# Write a header line in the output file
print("Country,1989,2009",file=outfile)

for line in infile:
    # cut the "\n" in the end of the line
    line = line[:-1]
    # YOUR CODE HERE: split up line

    # YOUR CODE HERE: There are four cases to consider:
    #   - both values are empty, don't write anything
    #   - value for 1989 is empty: use the value from 2009
    #   - value for 2009 is empty, use the value from 1989
    #   - neither value is empty, use btoh given values
    #
    # NOTE:
    #   - use appropriate if statements to handle the above cases
    #   - for the last three cases, write to the results file
    #   - to see if a value is empty use: = ""
    #   - when writing to the results file, output should be in this format
    #       "<Country>,<1989 value>,<2009 value>"
    #   - make sure that this .py file is in the same directory as
    #       children_per_woman.csv

infile.close()
outfile.close()
