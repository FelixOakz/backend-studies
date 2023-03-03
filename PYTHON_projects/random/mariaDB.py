# python create_a_database.py
# import the library
import mysql.connector
# creating connection with local expected parameters
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='PASSWORD'
)
#print the connection
print(conn)
# import the mycursor from the connection (conn)
cursor = conn.cursor()
#print the mycursor
print(cursor)
cursor.execute('create database dbTest')
"""
<mysql.connector.connection_cext.CMySQLConnection object at 0x7f9023a0fb50>
CMySQLCursor: (Nothing executed yet)

"""
#######################
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='PASSWORD',
    database='dbTest'
)
print(conn)
"""
<mysql.connector.connection_cext.CMySQLConnection object at 0x7f3bf2643b50>
"""
#######################
#python create_table.py

#import the library
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='PASSWORD',
    database='dbTest'
)
# we create a mycursor object using the conn.cursor()
mycursor = conn.cursor()
mycursor.execute("DROP TABLE IF EXISTS MOVIE")
# we write a query to create a table
query = "create table movie(id int PRIMARY KEY,name varchar(30), year INT)"
# We execute the query here
mycursor.execute(query)
# after process is done, we should close the connection
conn.close()
""""""
#######################
#python create_table.py
#import the library
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='PASSWORD',
    database='dbTest'
)
# we create a mycursor object using the conn.cursor()
mycursor = conn.cursor()

query = 'insert into movie(id, name, year)' \
        'values (1, "bruce almighty", 2003)'
# We execute the query here
mycursor.execute(query)
# after process is done, we should close the connection
conn.commit()
"""movie table had values inserted on the database, check terminal"""
#######################
# inserting multiple records at once

#import the library
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='PASSWORD',
    database='dbTest'
)
# we create a mycursor object using the conn.cursor()
mycursor = conn.cursor()

query = 'insert into movie (id, name, year) VALUES (%s, %s, %s)'
val = [
    (2, "kung fu panda", 2014),
    (4, "frozen", 2014),
    (5, "frozen 2", 2020),
    (6, "iron man", 2013)
]
mycursor.executemany(query, val)
# we commit(save) the records to the table
conn.commit()
print(mycursor.rowcount, "record(s) inserted.")
"""
4 record(s) inserted.
"""
#######################
# selecting records from tables
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='PASSWORD',
    database='dbTest'
)
mycursor = conn.cursor()
# execute the query and fetch all the records
query = 'SELECT * FROM movie'

mycursor.execute(query)
result = mycursor.fetchall()
# printing our result
print(result)
# now, doing iterations on each record and printing
for record in result:
    print(record)
# CAUTION because names of database, tables, etc, are case sensitive: MOVIES != movies
"""
[(1, 'bruce almighty', 2003), (2, 'kung fu panda', 2014), (4, 'frozen', 2014), (5, 'frozen 2', 2020), (6, 'iron man', 2013)]
(1, 'bruce almighty', 2003)
(2, 'kung fu panda', 2014)
(4, 'frozen', 2014)
(5, 'frozen 2', 2020)
(6, 'iron man', 2013)
"""
