# The purpose of this program is to look at e-mail headers from a file
# extract the addresses, then count the top 10 most frequent organizational domains

# Imported required libraries: SQLite3 and RegEx (Regular Expressions)
import sqlite3
import re

# Then I connect the database. If the file does not exists, the program will create it for me.
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
# This will help me navigate our SQL Database

cur.execute('DROP TABLE IF EXISTS Counts')        # If the table "Counts" exists, I am dropping it

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')  # Then I start from the ground up, I'm creating the table.

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'            # I placed the file in the project folder
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue     # Making sure that I am extracting the emails
    pieces = line.split()                          # Then making it a list to address the index 1
    email = pieces[1]
    fin = re.findall('@(.*)$', email)              # Used RegEx to extract the domain string
    domain = str(fin[0])                           # To make sure it works with my schema, I typecast the extraction
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    # Used a placeholder and gave it the domain variable
    row = cur.fetchone()
    # I am fetching the values one by one and passing them through a loop
    # This loop inserts the values and corroborates if the value is repeated, if so, the count will increment by 1
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain,))

conn.commit()
# I need to speed up the process by placing the commit out of the loop
# If I place it inside of the loop, it will be much slower

# https://www.sqlite.org/lang_select.html
# The SELECT operation, in the intended usage, will work only if we're working with SQLite

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
# This will sort the top 10 values to be printed, starting with the highest one. (descending order)

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])      # I'm actually printing the org and count columns with a loop

cur.close()                         # Finally, I'm closing the connection with the database
