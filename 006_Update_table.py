import sqlite3

dbase = sqlite3.connect('test_01.db')
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

def read_data():
    data = dbase.execute("SELECT * FROM employees_records ")
    l = 11
    print('-'*40)
    print("Id " + "Name".ljust(l,' ')+ 'Division'.ljust(l,' ')+ 'Stars'.ljust(l,' '))
    print('-'*40)
    for record in data:
        print(f"{record[0]} {record[1].ljust(l,' ')} {record[2].ljust(l,' ')} {record[3]}")
    print('-'*40)

insert_record(1,'Lenny','Software',3)
insert_record(2,'Cynthia','Manager',5)
insert_record(3,'Harrison','Mechanics',4)
insert_record(4, 'Joan', 'Electonics',3)
insert_record(5,'James', 'Maintenance',4)
insert_record(6,'Ramesh', 'Maintenance',4)
read_data()



def update_record():
    dbase.execute(""" UPDATE employees_records SET Stars=3 WHERE ID=6 """)
    dbase.commit

update_record()
read_data()
