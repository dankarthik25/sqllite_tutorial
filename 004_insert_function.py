import sqlite3

dbase = sqlite3.connect('test_01.db')


print("CREATE TABLE")
dbase.execute(""" CREATE TABLE IF NOT EXISTS employees_records(
        Id INT PRIMARY KEY NOT NULL,
        Name TEXT NOT NULL,
        Division TEXT NOT NULL,
        Stars INT NOT NULL)
            """)

def insert_record(Id,Name,Division,Stars ):
    dbase.execute('''INSERT INTO employees_records(Id,Name,Division,Stars)
            VALUES(?,?,?,?)''',(Id,Name,Division,Stars))
    dbase.commit()
    print("Recorded Inserted")

# insert_record(1,'Lenny','Software',3)
# insert_record(2,'Cynthia','Manager',5)
# insert_record(3,'Harrison','Mechanics',4)
# insert_record(4, 'Joan', 'Electonics',3)
# insert_record(5,'James', 'Maintenance',4)


# cursor.execute("SELECT * FROM employees_records ")
# print(cursor.fetchall())


dbase.close()
