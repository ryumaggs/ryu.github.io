# This program connects to the movie database, queries it for all people,
# and prints the results into an output file after reformating the dob's

import sqlite3
# assuming movie.sqlite is in the same folder
db = sqlite3.connect('movie_modified.sqlite')
outfile = open('people.txt', 'w')

cursor = db.cursor()
command = '''
    SELECT id, name, dob, pob
    FROM Person
    WHERE dob IS NOT NULL'''
cursor.execute(command)

for tuple in cursor:
    components = tuple[2].split("-")
    formatted_dob = components[1]+"/"+components[2]+"/"+components[0]
    print(tuple[0], tuple[1], formatted_dob, tuple[3], file=outfile)

outfile.close()
db.close()
