# This program will parse an iTunes Library XML file
# and insert its contents into a SQL Database.
# I am using my personal library which contains part of the Bill Evans' discography.
import xml.etree.ElementTree as ET
import sqlite3
import re
# Import what we need, connect the database, and enable a cursor ;-)
conn = sqlite3.connect('BillEvansdb.sqlite')
cur = conn.cursor()

# Making some fresh tables using executescript()
cur.executescript(
    '''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Year;


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
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    year_id INTEGER
);

CREATE TABLE Year (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    released TEXT UNIQUE
);
''')

fname = input('Enter file name: ')
if len(fname) < 1: fname = 'BE - Library.xml'
# It prompts me to enter file name, but I added the file to the project folder already.
# Just hit 'Enter'

# The data is similar to this:
# <key>Track ID</key><integer>77</integer>
# <key>Name</key><string>Emilly</string>
# <key>Artist</key><string>Bill Evans</string>
# <key>Album</key><string>1967 - Further Conversations With Myself</string>
# <key>Genre</key><string>Jazz, Cool, Modal</string>
def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

# I start to parse the XML with ElementTree and the lookup function
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Total Found:', len(all))
for entry in all:
    if lookup(entry, 'Track ID') is None: continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')

# Here the control structure might seem confusing, I am using regular expressions to clean
# the data to be inserted into the database fields. If you look at the XML file, the albums have
# the year in the same sentence and I wanted to keep track of the year in a separate table.
# The try-except structure is to prevent a traceback generated by the index related to the
# extractions with regular expressions, "list out of range" at the end of the execution.
# This is the best way I thought of to resolve that issue.

# By the way, these operations below involve some SQL. Please stay aware that queries like
# INSERT OR REPLACE work here because we're using SQLite3. This might not be that common
# in other SQL database engines. Last but not least, I made a query for you to look
# at the final result in DB Browser for SQLite or similar applications.
    if name is None or artist is None or album is None or genre is None:
        continue
    else:
        try:
            extractYear = re.findall('\d{4}', album)
            noYearinAlbum = re.findall('(\s\w.*$)', album)
            cleanAlbum = str(noYearinAlbum[0])

            print(name, artist, noYearinAlbum[0], genre, extractYear[0])

            cur.execute('''INSERT OR IGNORE INTO Artist (name) 
            VALUES ( ? )''', (artist,))
            cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
            artist_id = cur.fetchone()[0]

            cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
            VALUES ( ?, ? )''', (cleanAlbum, artist_id))
            cur.execute('SELECT id FROM Album WHERE title = ? ', (cleanAlbum,))
            album_id = cur.fetchone()[0]

            cur.execute('''INSERT OR IGNORE INTO Genre (name) 
            VALUES ( ? )''', (genre,))
            cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
            genre_id = cur.fetchone()[0]

            cur.execute('''INSERT OR IGNORE INTO Year (released) 
            VALUES ( ? )''', (extractYear[0],))
            cur.execute('SELECT id FROM Year WHERE released = ? ', (extractYear[0],))
            year_id = cur.fetchone()[0]

            cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, genre_id, year_id) 
            VALUES ( ?, ?, ?, ?)''', (name, album_id, genre_id, year_id))

            conn.commit()
        except:
            break
