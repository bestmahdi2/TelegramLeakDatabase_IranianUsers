import sqlite3
conn = sqlite3.connect('./databases/LightDB_no_dup.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS People (UID integer PRIMARY KEY, id integer NOT NULL, phone integer NOT NULL, username text)")
# c.execute("CREATE TABLE IF NOT EXISTS People (id integer NOT NULL, phone integer NOT NULL, username text)")
conn.commit()