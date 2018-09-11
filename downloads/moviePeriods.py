# This program connects to the modified movie database, queries it
# for all movies, figures out how many movies from the results fall
# into each of three time periods, and prints the results to an output file

import sqlite3
# assuming movie.sqlite is in the same folder
db = sqlite3.connect('movie_modified.sqlite')
outfile = open('results.txt', 'w')

cursor = db.cursor()
command = '''
    SELECT year
    FROM Movie'''
# only grabbing year column for efficiency,
# but works the same if we grab all columns
cursor.execute(command)

period1 = 0;
period2 = 0;
period3 = 0;
for tuple in cursor:
    year = tuple[0]
    if year < 1960:
        period1 = period1 + 1
    elif 1960 <= year and year <=2000:
        period2 = period2 + 1
    else:
        period3 = period3 + 1

print("Year Range", "Number of Movies", sep = "\t", file = outfile)
print("Before 1960", period1, sep = "\t", file = outfile)
print("1960-2000", period2, sep = "\t", file = outfile)
print("After 2000", period3, sep = "\t", file = outfile)

outfile.close()
db.close()
