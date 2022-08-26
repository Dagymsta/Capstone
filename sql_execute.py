
import sqlite3

def create_schema(cursor):
    with open('comp_schema.sql','r') as infile:
        schema=infile.read()
        cursor.executescript(schema)
        connection.commit()
connection = sqlite3.connect('comp_track.db')
cursor = connection.cursor()

result = create_schema(cursor)