# SQL - язык структур запросов
# DATAbase
# CRUD - create,update,read,delete
# СУБД - система управления баз данных
# субд делитеся на два: relation, noRelation
# relation - таблицы, noRelation - все что не относится к таблицам
# SQLite



import sqlite3
with sqlite3.connect('holodilnik.db') as con:
    cursor = con.cursor()
    # cursor.execute('''DROP TABLE IF EXISTS eat''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    full_name VARCHAR(104) NOT NULL,
    age INTEGER DEFAULT 8,
    hobby TEXT NOT NULL
    )''')
#     create
#     cursor.execute('''INSERT INTO users(full_name,age,hobby)
#     VALUES ('aimir',14,'basket') ''')
#     update
#     cursor.execute('''UPDATE users SET full_name='bakai'
#     WHERE full_name='aimir' ''')

    cursor.execute('''UPDATE users SET full_name='akel' 
    WHERE rowid=2 ''')

    cursor.execute('''SELECT rowid,* FROM users ''')

    for i in cursor.fetchall():
        print(i)