import sqlite3
conn = sqlite3.connect('person.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Departments(
DepartmentID INTEGER PRIMARY KEY,
DepartmentName TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Employees(
EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
FirstName TEXT NOT NULL,
LastName TEXT NOT NULL,
DepartmentID INTEGER,
FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
)''')

# cursor.execute('''INSERT INTO Departments(DepartmentID, DepartmentName)
# VALUES (101, 'HR'),
# (102, 'IT'),
# (103, 'Sales')
# ''')
#
# cursor.execute('''INSERT INTO Employees(FirstName, LastName, DepartmentID)
# VALUES ('cris', 'ron', 101),
# ('ney', 'jr', 101),
# ('leo', 'messi', 102),
# ('fede', 'valverde', 102),
# ('arda', 'guller', 103),
# ('bobby', 'endrick', 103)
# # ''')

cursor.execute('''SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName FROM Employees
JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
''')
print()
for name in cursor.fetchall():
    print(name)

cursor.execute(''' SELECT Employees.FirstName, Employees.LastName
FROM Employees
JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
WHERE Departments.DepartmentName = "IT"''')
print()
for name in cursor.fetchall():
    print(name)
conn.commit()