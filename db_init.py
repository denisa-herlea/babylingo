import sqlite3

conn = sqlite3.connect('babylingo.db')
cursor = conn.cursor()



cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT
)
''')

cursor.execute('''
       CREATE TABLE IF NOT EXISTS babies (
           id INTEGER PRIMARY KEY,
           user_id INTEGER,
           baby_name TEXT,
           date_of_birth DATE,
           hour_of_birth TIME,
           birth_weight REAL,
           birth_height REAL,
           FOREIGN KEY(user_id) REFERENCES users(id)
)
''')

conn.commit()
conn.close()