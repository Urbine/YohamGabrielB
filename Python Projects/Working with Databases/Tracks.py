# I have a similar project called Bill Evans Library. The main difference is that, for some Jazz lovers,
# the album chronology is very important. For that reason, I created a different project with a "year" table
# and a refined string extraction technique using Regular Expressions.

# Initiated imports and, in the case of ElementTree library, I am using an alias.
# So that I can call out the methods easily.
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;


CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER
)
''')

# Here I need to initiate the file handle to retrieve the XML file or just hit enter.
# The program will locate the file in the project folder for me.

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# The tree structure of the XML file looks like this.
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

# Here a function was defined to extract the tags and see if they actually exist.
# This is a way to clean the data and avoid entering blanks into the data database.
# This function enables a tree lookup in an efficient manner.
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

# File handle in order to parse, clean, and define data.
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')

    if name is None or artist is None or album is None or genre is None :
        continue

# This line will output to the screen the entire library.
    print(name, artist, album, genre)

# SQLite3 Library in action (again). Entering all the information one by one.
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', (artist, ))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', (genre, ))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id) 
        VALUES ( ?, ?, ?)''', (name, album_id, genre_id))
# Commit operation inside of the loop, remember that the variables are constantly changing.
# I need to commit the changes, one at the time.
    conn.commit()
