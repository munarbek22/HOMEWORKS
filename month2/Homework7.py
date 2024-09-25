import sqlite3
with sqlite3.connect('student') as con:
    cursor = con.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS student(
    hobby TEXT NOT NULL,
    full_name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    year_of_birth INT,
    points_for_hm INT
    )''')

    cursor.execute('''INSERT INTO student(hobby, full_name, surname, year_of_birth, points_for_hm)
        VALUES ('football', 'munarbek', 'baialiev', 2009, 34),
        ('valleyball', 'aziz', 'usenov', 2008, 40),
        ('basketball', 'aimir', 'baltabaev', 2010, 50),
        ('socccer', 'alex', 'john', 2006, 9),
        ('tennis', 'emma', 'radukanu', 2002, 30),
        ('kok-boru', 'askar', 'aliev', 2005, 8),
        ('badminton', 'safia', 'kovalevskaya', 2003, 7),
        ('swimming', 'elena', 'novikova', 2006, 7),
        ('running', 'atai', 'sharabidinov', 2000, 5),
        ('boxing', 'bekaman', 'kudaiberdiev', 2009, 11)''')

    cursor.execute('''SELECT * FROM student
    WHERE LENGTH(surname) >= 10''')

    cursor.execute('''UPDATE student SET full_name = "genius"
    WHERE points_for_hm > 10''')

    cursor.execute('''SELECT * FROM student
    WHERE full_name = "genius"''')

    cursor.execute('''DELETE FROM student
    WHERE rowid % 2 = 0''')
    for i in cursor.fetchall():
        print(i)
con.commit()