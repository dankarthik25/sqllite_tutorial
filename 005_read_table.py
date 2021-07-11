import sqlite3

dbase = sqlite3.connect('test_01.db')

def read_data():
    # data = dbase.execute("SELECT * FROM employees_records ")
    data = dbase.execute("SELECT * FROM employees_records ORDER BY Name")
    # print(data)
    l = 11
    print("Id " + "Name".ljust(l,' ')+ 'Division'.ljust(l,' ')+ 'Stars'.ljust(l,' '))
    print('-'*40)
    for record in data:
        # print(record)
        # print(f"Id :{record[0]} Name :{record[1].ljust(l,' ')} Division : {record[2].ljust(l,' ')} Stars : {record[3]}")
        print(f"{record[0]} {record[1].ljust(l,' ')} {record[2].ljust(l,' ')} {record[3]}")
        # for item in record:
            # print( item, end=" | ")

# cursor.execute("SELECT * FROM employees_records ")
# print(cursor.fetchall())
# dbase.commit()

read_data()

dbase.close()
