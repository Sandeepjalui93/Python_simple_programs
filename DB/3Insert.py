import sqlite3

conn = sqlite3.connect('sandeep.db')
print("Database connected succesfully")

conn.execute("INSERT INTO COMPANY1 (EMPID, NAME, AGE, ADDRESS, SALARY)\
            VALUES(101, 'Sandeep', 20, 'Malad', 5000.00) ");

conn.execute(" INSERT INTO COMPANY1 (EMPID, NAME, AGE, ADDRESS, SALARY)\
            VALUES(102, 'Prianca', 22, 'Malad', 7000.00) ");

conn.execute(" INSERT INTO COMPANY1 (EMPID, NAME, AGE, ADDRESS, SALARY)\
            VALUES(103, 'kremar', 30, 'andheri', 5000.00)");

conn.execute(" INSERT INTO COMPANY1 (EMPID, NAME, AGE, ADDRESS, SALARY)\
            VALUES(104, 'Neha', 35, 'goregoan', 7200.00)");

conn.commit()

print('rows inserted')
conn.close()
