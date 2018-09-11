# This program connects to the movie database, asks the user for
# a director name, queries the database for all films by that
# director, and prints the results to an output file 

import sqlite3
# assuming movie.sqlite is in the same folder
db = sqlite3.connect('movie.sqlite')
outfile = open('results.txt', 'w')

director_name = input("Please enter a director name: ")

cursor = db.cursor()
command = '''
    SELECT M.name, M.runtime
    FROM Movie M, Person P, Director D
    WHERE M.id = D.movie_id
    AND D.director_id = P.id
    AND P.name = ? '''
cursor.execute(command, [director_name])

count = 0
for tuple in cursor:
    print(tuple[0], '...', tuple[1], file=outfile)
    count = count + 1

if count > 0:
    print("Printed", count, "movies directed by", director_name, "to results.txt")
else:
    print("There are no movies directed by", director_name, "in our database")

outfile.close()
db.close()
