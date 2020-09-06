# This file has the purpose of serving as a roster. The program will go through a JSON file
# and classify the entries with the purpose of building a database with a data model containing a role table
# accessible to other tables, in order to increase the data retrieval efficiency.


# Initiated the import of the libraries required for this program.
import json
import sqlite3

# This cursor will enable me to navigate into my database.
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Doing some setup and re-creating the data model from the ground up.
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Here I need to initiate the file handle to retrieve the JSON file or just hit enter.
# The program will locate the file in the project folder for me.
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# The data structure into the JSON file will look like this.
# Name, course name, and role code (either 0 or 1).
# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

# JSON library in action. It is opening and loading the data.
str_data = open(fname).read()
json_data = json.loads(str_data)

# Here I am fetching each of the indexes in the JSON file and assigning them to variables.
for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

# However, I want to print the contents that will be inserted into the database.
# Just trying to display the name of the role, because the user matters.
    if role == 1:
        rolename = "Instructor"
    else:
        rolename = "Student"

    print((name, title, rolename))

# SQLite3 Library in action (again). Putting it all together into the database.
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', (name,))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
                (user_id, course_id, role))

# Commit operation inside of the loop, remember that the variables are constantly changing.
# I need to commit the changes, one at the time.
    conn.commit()
