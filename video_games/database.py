import csv
import sqlite3


from flask import Flask, request, g
from video_games import app

DATABASE = 'videogame.db'

def create_database():
    conn = sqlite3.connect('videogame.db')
    conn.text_factory = str
    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS videogame""")
    cur.execute("""CREATE TABLE videogame
        (Rank integer, Name text, Platform text, Year integer not null,
        Genre text, Publisher text, NA_Sales float, EU_Sales float,
        JP_Sales float,Other_Sales float, Global_Sales float)""")

    with open('Data/vgsales2.csv', 'r') as f:
        reader = csv.reader(f.readlines()[1:1000])  # exclude header line
    cur.executemany("""INSERT INTO videogame VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
        (row for row in reader))
    conn.commit()
    conn.close()


def connect_to_database():
    create_database()    
    return sqlite3.connect(app.config['DATABASE'])

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = connect_to_database()
    db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def execute_query(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


