import sqlite3

with sqlite3.connect("TitanMapDatabase.db") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
FirstName VARCHAR(20) NOT NULL,
LastName VARCHAR(20) NOT NULL,
Email VARCHAR(30) NOT NULL,
username VARCHAR(20) NOT NULL,
Password VARCHAR(20) NOT NULL,
CPassword VARCHAR(20) NOT NULL);
''')

cursor.execute("""
INSERT INTO user(FirstName,LastName,Email,username,password,CPassword)
VALUES ("Vanchhit", "Khare", "Khare.van08@gmail.com","Savinay","Vani","Vani")
""")
db.commit()

cursor.execute("SELECT * FROM user")
print(cursor.fetchall())
