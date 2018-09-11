infile = open("children_per_woman.csv","r")
outfile = open("result.csv","w")

# Write a header line in the output file
print("Country,1989,2009",file=outfile)

for line in infile:
    # cut the "\n" in the end of the line
    line = line[:-1]
    components = line.split(",")

    # if the value for 1989 is empty, use the value for 2009
    if components[1] == "":
        components[1] = components[2]

    # if the value for 2009 is empty, use the value for 1989
    if components[2] == "":
        components[2] = components[1]

    # now we could check if both are non empty, write to file
    if components[1] != "" and components[2] != "":
        newline =  ",".join([ components[0], components[1], components[2]])
        print(newline,file=outfile)

infile.close()
outfile.close()
