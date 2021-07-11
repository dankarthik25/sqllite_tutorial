import sqlite3

dbase = sqlite3.connect('test_01.db')


# print("CREATE TABLE")
dbase.execute(""" CREATE TABLE IF NOT EXISTS employees_records(
        Id INT PRIMARY KEY NOT NULL,
        Name TEXT NOT NULL,
        Division TEXT NOT NULL,
        Stars INT NOT NULL)
            """)
# def inset_record( )
dbase.execute('''INSERT INTO employees_records(Id,Name,Division,Stars)
            VALUES(1,'Lenny','Software',3)
        ''')
#             VALUES(2,'Cynthia','Manager',5)
#             VALUES(3,'Harrison','Mechanics',4)
#             VALUES(4, 'Joan', 'Electonics',3)
#             VALUES(5,'James', 'Maintenance',4)
# #
# dbase.execute('''INSERT INTO employees_records(Id,NAME,STARS)
#             VALUES(1,'Lenny','Software',3)
#         ''')

# cursor.execute("SELECT * FROM employees_records ")
# print(cursor.fetchall())
dbase.commit()


dbase.close()
