import sqlite3

conn = sqlite3.connect('sandeep.db')
print("Database connected succesfully")

cursor = conn.execute("SELECT EMPID, NAME, AGE, ADDRESS, SALARY from COMPANY1")

for i in cursor:
    print(i)
print("Operation dine ")
conn.close()
