# This program reads in data from a file line by line, and
# prints only a subset of the data to an output file

# assuming both files are in the same directory as this file
infile = open("movie.txt", 'r')
outfile = open("movie_processed.txt", 'w')

for line in infile:
    components = line.split("|")
    print(components[1], components[2], components[4], file=outfile)    

infile.close()
outfile.close()
