import sqlite3
import json

conn = sqlite3.connect('raw_content_metorite_landing.sqlite')
cur = conn.cursor()

cur.executescript('''
    CREATE TABLE IF NOT EXISTS metorite_landing_data (
        name TEXT UNIQUE,
        id INTEGER UNIQUE,
        name_type TEXT,
        rec_class TEXT,
        mass INTEGER,
        fall TEXT,
        year TEXT,
        rec_lat INTEGER,
        rec_long INTEGER
    );
''')

conn.commit()

json_fname = input('Enter file name: ')
if (len(json_fname) < 1):
    json_fname = 'data.json'

str_data = open(json_fname).read()
json_data = json.loads(str_data)

for data in json_data:
    name = data.get('name')
    id = data.get('id')
    name_type = data.get('nametype')
    rec_class = data.get('recclass')
    mass = data.get('mass')
    fall = data.get('fall') 
    year = str(data.get('year'))[:4]
    rec_lat = data.get('reclat')
    rec_long = data.get('reclong')

    cur.execute('''INSERT OR IGNORE INTO metorite_landing_data ( name, id, name_type, rec_class, mass, fall, year, rec_lat, rec_long )
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ? )''', ( name, id, name_type, rec_class, mass, fall, year, rec_lat, rec_long ))

conn.commit()
print('Data collection completed, view sqlite file in sql.')
conn.close()