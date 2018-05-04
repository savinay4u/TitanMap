import sqlite3

def login():
    while True:
        username = input("Please Enter your Username: ")
        password = input("Please Enter your Password: ")
        with sqlite3.connect("TitanMapDatabase.db") as db:
            cursor=db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(username),(password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("Welcome "+i[2])
                break

        else:
            print("Username and Password not recognised")
            again = input("Do you want to try again ? (y/n): ")
            if again.lower() =="n":
                print("GoodBye")
                time.sleep(1)
                break

login()
