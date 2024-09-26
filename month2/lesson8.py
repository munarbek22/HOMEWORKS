# sql
# субд
# relation noRelation
# crud

import sqlite3
conn = sqlite3.connect('memory.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
userid INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(255) NOT NULL,
age INTEGER DEFAULT 16
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS checks(
checkid INTEGER PRIMARY KEY AUTOINCREMENT,
money INTEGER DEFAULT 0,
userid INTEGER,
FOREIGN KEY (userid) REFERENCES users(userid)
)''')
# cursor.execute('''INSERT INTO users(name, age) VALUES ('beka',21),('bekbolot',30),
# ('AIMIR',40),('BAKAI',50)
# ''')
# cursor.execute('''INSERT INTO checks (money, userid) VALUES (10000,1),(3141592,3),(20,4)''')
# cursor.execute('''INSERT INTO checks(money, userid) VALUES (20,4)''')
cursor.execute('''SELECT * FROM users''')
for row in cursor.fetchall():
    print(row)
print()
cursor.execute('''SELECT * FROM checks''')
for row in cursor.fetchall():
    print(row)

cursor.execute(''' SELECT users.userid, users.name, checks.money FROM  users
JOIN checks ON checks.userid = users.userid ORDER BY users.userid 
''')
print()
for row in cursor.fetchall():
    print(row)


conn.commit()
conn.close()
