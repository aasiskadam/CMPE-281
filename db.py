import sqlite3

conn = sqlite3.connect('Deliverable3.db')

print("Opened database successfully")

c = conn.cursor()

# c.execute('''CREATE TABLE farmers
#              (firstname text, lastname text, username text, email text, password text, usertype text) ''')


c.execute('''CREATE TABLE IF NOT EXISTS staffmembers
             (firstname text, lastname text, employeeID text, username text, email text, password text, usertype text) ''')

conn.commit()

conn.close()
