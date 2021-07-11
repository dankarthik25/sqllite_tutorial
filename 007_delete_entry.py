import sqlite3

dbase = sqlite3.connect('test_01.db')

def read_data():
    data = dbase.execute("SELECT * FROM employees_records ")
    l = 11
    print('-'*40)
    print("Id " + "Name".ljust(l,' ')+ 'Division'.ljust(l,' ')+ 'Stars'.ljust(l,' '))
    print('-'*40)
    for record in data:
        print(f"{record[0]} {record[1].ljust(l,' ')} {record[2].ljust(l,' ')} {record[3]}")
    print('-'*40)

def delete_record():
    dbase.execute("""DELETE FROM employees_records WHERE Id = 1 """)
    dbase.commit()

read_data()
delete_record()
print("Deleted Id = 1")

read_data()
