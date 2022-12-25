import sqlite3

conn = sqlite3.connect("sandeep.db")
print("Database connected succesfully")

str = ''' CREATE TABLE COMPANY1
        (
            EMPID INT PRIMARY KEY ,
            NAME TEXT NOT NULL,
            AGE INT NOT NULL,
            ADDRESS CHAR(50),
            SALARY REAL
        ); '''

conn.execute(str)

print("Table created")
conn.close()
