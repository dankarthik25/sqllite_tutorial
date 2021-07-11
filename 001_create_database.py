import sqlite3

dbase = sqlite3.connect('test_01.db')
print(" CREATE/OPEN  DATABASE")

dbase.close()
print("CLOSE DATABASE")

# cursor = dbase.cursor()
#
# # cursor.execute(""" CREATE TABLE employees(
# #             first text,
# #             last text,
# #             pay integer
# #             )""")
#
#
# # cursor.execute ("INSERT INTO employees VALUES ('Corey', 'Schafer',5000)")
#
# # cursor.execute ("INSERT INTO employees VALUES ('Mary', 'Schafer',5000)")
#
# cursor.execute("SELECT * FROM employees WHERE first = 'Corey'")
#
# print(cursor.fetchall())
#
# dbase.commit()
