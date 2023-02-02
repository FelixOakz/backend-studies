import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE testing (
                   first_name text,
                   last_name text,
                   email text
               )
               """)

conn.commit()

conn.close()

conn.execute("SELECT * from test")
conn.fetchone()
conn.fetchmany(3)
conn.fetchall()
