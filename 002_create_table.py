import sqlite3

dbase = sqlite3.connect('test_01.db')


print("CREATE TABLE")
dbase.execute(""" CREATE TABLE IF NOT EXISTS employees_records(
        Id INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        STARS INT NOT NULL
            )""")

dbase.close()
